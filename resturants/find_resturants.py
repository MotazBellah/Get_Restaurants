# from geocode import getGeocodeLocation
import json
import httplib2

import requests



import sys
import codecs
# sys.setdefaultencoding('utf-8')



foursquare_client_id = "GPNIKHBZJTOV43AVINUWDROR124MWFEOI1DI4BPJZH20IXGF"
foursquare_client_secret = "MHDO5POADIQTWC5G332RN2HLMCHE10HOGTS0RXNVFHX12NTD"
def findAResturant(mealType, location=0):
    latitude, longitude = 30.0443879, 31.2357257
    restaurantInfo = []

    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20182611&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret,latitude,longitude,mealType))

    y = requests.get(url)
    result = y.json()


    all = result['response']['venues']
    explore = False
    if not all:
        url2 = ('https://api.foursquare.com/v2/venues/explore?client_id=%s&client_secret=%s&v=20182611&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret,latitude,longitude,mealType))
        y = requests.get(url2)
        result = y.json()
        explore = True

        all = result['response']['groups'][0]['items']

    for i in all:

        if explore:
            i = i['venue']

        venue_id = i['id']
        restaurant_name = i['name']
        restaurant_address = i['location']['formattedAddress']
        location = i['location']
        distance = location['distance']
        lat_lng = location['lat'], location['lng']

        url_img = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
        z = requests.get(url_img)
        v = z.json()
        imageURL = ''
        if 'photos' in v['response']:
            if v['response']['photos']['items']:
                first = v['response']['photos']['items'][0]
                pre = first['prefix']
                suff = first['suffix']
                imageURL = pre + "300x300" + suff


        url_like = ('https://api.foursquare.com/v2/venues/%s/likes?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
        likes = requests.get(url_like)
        likes_json = likes.json()
        no_of_liks = likes_json['response']['likes']['count']

        # url_menu = ('https://api.foursquare.com/v2/venues/%s/menu?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
        # menu = requests.get(url_menu)
        # menu_json = menu.json()
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print(menu_json)

        restaurantDict = {'name': restaurant_name, 'address': "".join(restaurant_address),
                          'img': imageURL, 'distance': distance, 'lat_lng': lat_lng,
                          'likes': no_of_liks}

        restaurantInfo.append(restaurantDict)

    return restaurantInfo

print(findAResturant("Falafel"))

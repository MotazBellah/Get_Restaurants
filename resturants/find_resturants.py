import json
import httplib2
import requests
import sys
import codecs
from requests_futures.sessions import FuturesSession

from flickrapi import FlickrAPI
from yelpapi import YelpAPI

foursquare_client_id = "GPNIKHBZJTOV43AVINUWDROR124MWFEOI1DI4BPJZH20IXGF"
foursquare_client_secret = "MHDO5POADIQTWC5G332RN2HLMCHE10HOGTS0RXNVFHX12NTD"

flicker_api = "fe0ed62e4e7921c6f413d8d237cae744"
flicker_secret = "83855df34390897b"

yelp_api_key = "EfGWOgYw0nC303Y6ZT6iLWIAdvVhg6mhutUcIu1vixCJJ1ZyL6EUwbytUmRiDlFmxnlraowD1g5MZN4inZm2q5WqyEuf_2UOTmROhstLehrRT_TO_5rGddpYFhgLYHYx"

zomato_api = '4b246d4d35c826771d1a3ef4bb06770b'

def findAResturant(mealType, location):
    # latitude, longitude = 30.0443879, 31.2357257

    latitude, longitude = location
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
        # z = requests.get(url_img)
        # v = z.json()
        # imageURL = ''
        # if 'photos' in v['response']:
        #     if v['response']['photos']['items']:
        #         first = v['response']['photos']['items'][0]
        #         pre = first['prefix']
        #         suff = first['suffix']
        #         imageURL = pre + "300x300" + suff


        # url_like = ('https://api.foursquare.com/v2/venues/%s/likes?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
        # likes = requests.get(url_like)
        # likes_json = likes.json()
        # no_of_liks = likes_json['response']['likes']['count']
        no_of_liks = 0

        # url_menu = ('https://api.foursquare.com/v2/venues/%s/menu?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
        # menu = requests.get(url_menu)
        # menu_json = menu.json()
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print(menu_json)

        restaurantDict = {'name': restaurant_name, 'address': "".join(restaurant_address).strip(),
                          'img': url_img, 'distance': distance/1000, 'lat_lng': lat_lng,
                          'likes': no_of_liks}

        restaurantInfo.append(restaurantDict)

    return restaurantInfo

# def get_photo(mealType, location=(30.0443879, 31.2357257)):
#     resturants_info = findAResturant(mealType, location)
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
#             AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
#
#     for i in resturants_info:
#         z = requests.get(i['img'])
#         v = z.json()
#         print(v)

    # with FuturesSession(max_workers=1) as session:
    #     futures = [session.get(i['img']) for i in resturants_info]
    #     print(futures)
    #     for future in futures:
    #         response = future.result()
    #         print(response)

# def find_photos(keyward):
#     # yelp_api = YelpAPI(yelp_api_key)
#     # latitude, longitude = 30.0443879, 31.2357257
#     # search_results = yelp_api.search_query(term='burger', latitude=30.0443879, longitude=31.2357257, sort_by='rating', limit=5)
#     # print(search_results)
#     flickr = FlickrAPI(flicker_api,flicker_secret,cache=True)
#
#     photos = flickr.walk(text=keyward,
#                          tag_mode='all',
#                          tags=keyward,
#                          extras='url_c',
#                          per_page=50,
#                          sort='relevance')
#     print(photos)
#
#     for photo in photos:
#         try:
#             url=photo.get('url_c')
#             print(url)
#
#         except Exception as e:
#             print('failed to download image')
#
#
#
#
#
# print(get_photo('Burger'))

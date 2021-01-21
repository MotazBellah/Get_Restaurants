# from geocode import getGeocodeLocation
import json
import httplib2

import requests



import sys
import codecs
# sys.setdefaultencoding('utf-8')



foursquare_client_id = "GPNIKHBZJTOV43AVINUWDROR124MWFEOI1DI4BPJZH20IXGF"
foursquare_client_secret = "MHDO5POADIQTWC5G332RN2HLMCHE10HOGTS0RXNVFHX12NTD"

print('XXXXXXXXXXXXXXXXXXXXXXXXX')
    #
latitude, longitude = 30.0443879, 31.2357257
    #
	# #2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	# #HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20182611&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret,latitude,longitude,"Falafel"))
# h = httplib2.Http()
# print(h)
# r = h.request(url,'GET')[1]
# print(str(r).encode('utf8').decode('ascii', 'ignore'))
# x = str(r).encode('utf8').decode('ascii', 'ignore')
# print(type(str(r)))
# print(type(str.encode(x)))
# result = json.loads(str.encode(x), strict=False)
# print(result)

y = requests.get(url)
result = y.json()
# print(result)

all = result['response']['venues']
# print(all)

for i in all:
    # restaurant = i['response']['venues']
    venue_id = i['id']
    restaurant_name = i['name']
    restaurant_address = i['location']['formattedAddress']
    location = i['location']
    distance = location['distance']

    url_img = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
    z = requests.get(url)
    v = z.json()
    # firstpic = v['response']

    # if v['response']['photos']['items']:
	# firstpic = v['response']['photos']['items'][0]
	# prefix = firstpic['prefix']
    # suffix = firstpic['suffix']
    # imageURL = prefix + "300x300" + suffix
    print('<<<<<<<<>>>>>>>>')
    # print(firstpic)
    print(venue_id)
    print(restaurant_name)
    print(restaurant_address)
    print(location)
    print(distance)


    #
	# if result['response']['venues']:
	# 	#3.  Grab the first restaurant
	# 	restaurant = result['response']['venues'][0]
	# 	venue_id = restaurant['id']
	# 	restaurant_name = restaurant['name']
	# 	restaurant_address = restaurant['location']['formattedAddress']
	# 	address = ""
	# 	for i in restaurant_address:
	# 		address += i + " "
	# 	restaurant_address = address
	# 	#4.  Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	# 	url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
	# 	result = json.loads(h.request(url, 'GET')[1])
	# 	#5.  Grab the first image
	# 	if result['response']['photos']['items']:
	# 		firstpic = result['response']['photos']['items'][0]
	# 		prefix = firstpic['prefix']
	# 		suffix = firstpic['suffix']
	# 		imageURL = prefix + "300x300" + suffix
	# 	else:
	# 		#6.  if no image available, insert default image url
	# 		imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"
	# 	#7.  return a dictionary containing the restaurant name, address, and image url
	# 	restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':imageURL}
    #

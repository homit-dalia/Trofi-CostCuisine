import requests
import json


f = open('placesAPI.json')
data = json.load(f)
api_key = data['key']
f.close()


location = ['21.229260919850972', '72.77912414622021']   #lat long
radius = '3000'   #meters


url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location[0]}%2C{location[1]}&radius={radius}&type=restaurant&key={api_key}"

# print(url)

payload={}
headers = {}

response = []
response.append(json.loads(requests.request("GET", url, headers=headers, data=payload).text)['results'])

#implement logic to fetch a total of 100 nearby restaurants. One request fetches 20.  
# Visit https://developers.google.com/calendar/api/guides/pagination



for collection in response:
    for place in collection:
        try:
            print(place['name'])
        except:
            continue
        try:
            print(str(place['rating']) + " - average rating from " + str(place['user_ratings_total']) + " reviews")
        except:
            print("Rating not found")
        try:
            print(place['price_level'])
        except:
            print("Price level not found")
        print('##\n')





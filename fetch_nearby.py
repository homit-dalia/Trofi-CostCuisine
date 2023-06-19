import requests
import json


f = open('placesAPI.json')
data = json.load(f)
api_key = data['key']
f.close()


location = ['21.229260919850972', '72.77912414622021']   #lat long
radius = '1000'   #meters


url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location[0]}%2C{location[1]}&radius={radius}&type=restaurant&key={api_key}"

# print(url)

payload={}
headers = {}
response = []

response.append(json.loads(requests.request("GET", url, headers=headers, data=payload).text)['results'])

#implement logic to fetch a total of 100 nearby restaurants. One request fetches 20.  
# Visit https://developers.google.com/calendar/api/guides/pagination

output = {}
output['results'] = []
output['total'] = 0

for collection in response:
    for place in collection:
        if(place['business_status'] == 'OPERATIONAL'):
            temp = {}
            try:
                temp['name'] = place['name']
                print(place['name'])
            except:
                continue
            try:
                temp['rating'] = place['rating']
                temp['user_ratings_total'] = place['user_ratings_total']

                print(str(place['rating']) + " - average rating from " + str(place['user_ratings_total']) + " reviews")
            except:
                temp['rating'] = None
                temp['user_ratings_total'] = None

                print("Rating not found")
            try:
                temp['price_level'] = place['price_level']
                print(place['price_level'])
            except:
                temp['price_level'] = None
                print("Price level not found")
            output['results'].append(temp)
            output['total'] += 1
            print('##\n')

print(output)



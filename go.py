import urllib
import json

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

api_key = "AIzaSyCgZBlNZbfJmv7ubK6ChTWpbkfsH2C3_6g"

origin = raw_input('Enter your location: ').replace(' ','+')

destination = raw_input('Destination Location: ').replace(' ','+')

request = endpoint+"origin="+origin+"&destination="+destination+"&key="+api_key

response = urllib.urlopen(request).read()
directions = json.loads(response)
print json.dumps(directions,indent=4,sort_keys=True)


import requests as requests
import json

url_bonn = "https://stadtplan.bonn.de/geojson?Thema=17238"
url = "https://www.stadt-muenster.de/ows/mapserv706/poiserv?REQUEST=GetFeature&SERVICE=WFS&VERSION=2.0.0&TYPENAME=ms:glascontainer&OUTPUTFORMAT=GEOJSON&EXCEPTIONS=XML&MAXFEATURES=10000&SRSNAME=EPSG:4326"
data = requests.get(url_bonn)
data_set = []
for i in data.json()['features']:
  lng = i['geometry']['coordinates'][0]
  lat = i['geometry']['coordinates'][1]
  val = {"lng": lng, "lat": lat}
  data_set.append(val)

with open('../src/assets/locations.json', 'r') as jsonfile:
  try:
    current_data = json.load(jsonfile)
  except:
    print("Failed to read current data")
    current_data = []
with open('../src/assets/locations.json', 'w') as outfile:
  json.dump(data_set + current_data, outfile)

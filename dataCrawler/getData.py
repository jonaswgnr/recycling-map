from glob import glob

import requests as requests
import json

def data_muenster():
  #url_bonn = "https://stadtplan.bonn.de/geojson?Thema=17238"
  url = "https://www.stadt-muenster.de/ows/mapserv706/poiserv?REQUEST=GetFeature&SERVICE=WFS&VERSION=2.0.0&TYPENAME=ms:glascontainer&OUTPUTFORMAT=GEOJSON&EXCEPTIONS=XML&MAXFEATURES=10000&SRSNAME=EPSG:4326"
  data = requests.get(url)
  data_set = []
  city = "muenster"
  outfile = "../src/assets/locationfiles/locations_" + city + ".json"
  for i in data.json()['features']:
    lng = i['geometry']['coordinates'][0]
    lat = i['geometry']['coordinates'][1]
    val = {"lng": lng, "lat": lat}
    data_set.append(val)

  with open(outfile, 'w') as outfile:
    json.dump(data_set, outfile)

#https://geo.sv.rostock.de/download/opendata/glascontainer/glascontainer.json

def data_rostock():
  url = "https://geo.sv.rostock.de/download/opendata/glascontainer/glascontainer.json"
  data = requests.get(url)
  data_set = []
  city = "rostock"
  outfile = "../src/assets/locationfiles/locations_" + city + ".json"
  for i in data.json()['features']:
    lng = i['geometry']['coordinates'][0]
    lat = i['geometry']['coordinates'][1]
    val = {"lng": lng, "lat": lat}
    data_set.append(val)

  with open(outfile, 'w') as outfile:
    json.dump(data_set, outfile)

def data_bonn():
  url = "https://stadtplan.bonn.de/geojson?Thema=17238"
  data = requests.get(url)
  data_set = []
  city = "bonn"
  outfile = "../src/assets/locationfiles/locations_" + city + ".json"
  for i in data.json()['features']:
    lng = i['geometry']['coordinates'][0]
    lat = i['geometry']['coordinates'][1]
    val = {"lng": lng, "lat": lat}
    data_set.append(val)

  with open(outfile, 'w') as outfile:
    json.dump(data_set, outfile)


def merge_data():
  result = []
  for f in glob('../src/assets/locationfiles/*.json'):
    print(f)
    with open(f, "r") as infile:
      injson = json.load(infile)
      result = result + injson
  print(result)
  with open("../src/assets/locations.json", "w") as outfile:
    json.dump(result, outfile)

#data_muenster()
#data_bonn()
data_rostock()
merge_data()

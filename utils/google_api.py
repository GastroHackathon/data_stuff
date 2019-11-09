#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:05:27 2019

@author: drx
"""

import json
import requests
import os

os.chdir('../../media/shareddata/gastrohackathon')
os.getcwd()

# google api key
#  AIzaSyAyQOGzb30ztSLLFHA0A32_B4GW9KH8Hss 

# place search
url = 'https://maps.googleapis.com/maps/api/place/'
action = 'findplacefromtext/json?'
input_data = 'input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&'
fields = 'fields=photos,formatted_address,name,rating,opening_hours,geometry'
key = '&key=AIzaSyAyQOGzb30ztSLLFHA0A32_B4GW9KH8Hss'

r = requests.get(url+action+input_data+fields+key)
r.json()


# nearby search
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
lat = '47.822080,'
lon = '13.027010'
radius = '&radius=1500'
establishment_type = '&type=restaurant'
key = '&key=AIzaSyAyQOGzb30ztSLLFHA0A32_B4GW9KH8Hss'

r = requests.get(url+lat+lon+radius+establishment_type+key)
restaurants = r.json()
restaurants = restaurants['results']

with open('data/restaurants.json', 'w') as f:
    json.dump(restaurants, f)


with open('data/restaurants.json') as f:
    restaurants = json.load(f)

for r in restaurants:
    print(r['name'],
          #r['vicinity'],
          r['place_id'],
          #r['opening_hours'],
          r['rating'])
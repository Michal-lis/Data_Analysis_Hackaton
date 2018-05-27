from __future__ import print_function
import json
import requests


def google_elevation(lat, lng):
    apikey = ""
    url = "https://maps.googleapis.com/maps/api/elevation/json"
    request = requests.get(url + "?locations=" + str(lat) + "," + str(lng) + "&key=" + apikey)
    try:
        results = json.loads(request.text).get('results')
        if 0 < len(results):
            elevation = results[0].get('elevation')
            # resolution = results[0].get('resolution') # for RESOLUTION
            return elevation
        else:
            print('HTTP GET Request failed.')
    except ValueError as e:
        print('JSON decode failed: ' + str(request) + str(e))


def free_open_elevation(lat=41.161758, lng='-8.583933'):
    url = 'https://api.open-elevation.com/api/v1/lookup?locations='
    request = requests.get(url + str(lat) + ',' + str(lng))
    try:
        results = json.loads(request.text).get('results')
        if 0 < len(results):
            elevation = results[0].get('elevation')
            # resolution = results[0].get('resolution') # for RESOLUTION
            return elevation
        else:
            print('HTTP GET Request failed.')
    except ValueError as e:
        print('JSON decode failed: ' + str(request) + str(e))


print(free_open_elevation())

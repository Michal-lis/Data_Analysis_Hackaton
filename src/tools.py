import json
import requests


def parser_krzys(a):
    l = []
    for pair in a[0].split('(((')[1].split(')))')[0].split(','):
        a = float(pair.split(' ')[0])
        b = float(pair.split(' ')[1])
        l.append((a, b))
    return l


def free_open_elevation(lat, lng):
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

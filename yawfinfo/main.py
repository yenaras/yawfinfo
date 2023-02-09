#!/usr/bin/env python3

import screen_reader
import requests

drops = screen_reader.relic_drops()
plat_val = []
for i in drops:
    i_string = "{}".format(i)
    response = requests.get(
        'https://api.warframe.market/v1/items/' +
        i_string.lower().replace(' ', '_')
        + '/orders')
    json_response = response.json()
    plat_val.append(json_response['payload']['orders'][-1]['platinum'])

data = dict(zip(drops, plat_val))

#!/usr/bin/env python3
import requests
from requests.exceptions import HTTPError


def get_market_data():
    try:
        response = requests.get('https://api.warframe.market/v1/items')
        response.raise_for_status()
        json_response = response.json()
        dict = json_response['payload']['items']

    except HTTPError as http_err:
        print(f'HTTP Error occured: {http_err}')
    except Exception as err:
        print(f'Other error occured: {err}')
    return dict


print(get_market_data())

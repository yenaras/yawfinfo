#!/usr/bin/env python3
import requests
from requests.exceptions import HTTPError
import pandas as pd
import numpy as np

try:
    response = requests.get('https://api.warframe.market/v1/items')
    response.raise_for_status()
    json_response = response.json()
    df = pd.DataFrame.from_dict(json_response['payload']['items'])
    df = df.drop(df.columns[[1, 2, 4]], axis=1)
    print(df)


except HTTPError as http_err:
    print(f'HTTP Error occured: {http_err}')
except Exception as err:
    print(f'Other error occured: {err}')

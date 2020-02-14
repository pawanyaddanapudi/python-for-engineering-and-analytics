# https://min-api.cryptocompare.com/
# Login to https://min-api.cryptocompare.com/, create account if you don't have one.
# Understand the pricing constraints
# Get your API key
# Extract BTC to USA and GBP details for every 30 seconds
# Transform data as needed to create csv file
# Write the data into flat files

import schedule # pip3 install schedule
import requests # pip3 install request
import time
import json


def pull_currency_data(site_url, apikey, file_name):
    """
    :param site_url: URL to which requests get should hit
    :param apikey: Key from your account
    :param file_name: location and file name where output should be saved/appended
    """
    global data
    data = requests.get(url=site_url+apikey)
    file = open(file_name, "a")
    currency = json.loads(data.content)
    output = data.headers['Date'] + '|' + '1' + '|' + str(currency['USD']) + '|' + str(currency['JPY']) + '|' + \
             str(currency['EUR']) + '\n'
    file.write(output)
    file.close()


key = '2447285030a725a86d4ef48ea1336edb9c67189caa0750fb8ab4697799861dc8'
url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR&api_key='
file_name = './Track 4 | Python Data Engineering | Real-time data | Extract & Transform/currency_extract.csv'
schedule.every(30).seconds.do(pull_currency_data, url, key, file_name)

# Run in  loop to extract data for every 30 seconds
while True:
    schedule.run_pending()
    time.sleep(1)

# Verify data after a minute or two to find multiple records in the file

# Exercise:
# - Understand what are the other keys available in data object inside the function
# - For daily historical data, extract and transform all the array elements in the data object





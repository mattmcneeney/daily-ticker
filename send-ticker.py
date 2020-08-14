#!/usr/local/bin/python3

import sys
import requests
import os
import re
import json

def getFundData():
    r = requests.get('https://api.vanguard.com/rs/gre/gra/1.7.0/datasets/urd-product-details.jsonp?path=[id=vanguard-ftse-global-all-cap-index-fund-gbp-acc][0]')
    jsonData = json.loads(re.match(r'callback\((.*)\)', r.text).group(1))
    return {
        'date': jsonData['navPrice']['asOfDate'],
        'value': jsonData['navPrice']['value'],
        'amountChange': jsonData['navPrice']['amountChange'],
        'percentChange': jsonData['navPrice']['percentChange']
    }

def sendTicker(data, iftttApiKey):
    print('Sending ticker info in push notification')
    data = {
        'value1': 'Vanguard FTSE Global All Cap Index Fund (%s)' % (data['date']),
        'value2': 'Value: %s\nChange: %s (%s)' % (data['value'], data['amountChange'], data['percentChange']),
        'value3': 'https://cdn-static.findly.com/wp-content/uploads/sites/11/2015/02/CareersSite_FeaturedImage_Home_640x480.jpg'
    }
    requests.post('https://maker.ifttt.com/trigger/daily_ticker/with/key/%s' % iftttApiKey, data=data)

def main():
   # Check for the required environment variables
   try:
       iftttApiKey = os.environ['IFTTT_API_KEY']
   except KeyError as e:
       print('Please set the %s environment variable' % e.args[0])
       sys.exit(1)

   # Get fund data
   data = getFundData()

   # Send the notification
   sendTicker(data, iftttApiKey)

if __name__ == '__main__':
   main()

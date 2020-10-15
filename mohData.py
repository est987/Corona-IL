import urllib.request


with urllib.request.urlopen("https://data.gov.il/api/action/datastore_search?resource_id=d337959a-020a-4ed3-84f7-fca182292308") as url:
    s = url.read()
    # I'm guessing this would output the html source code ?
    print(s)

    url = 'https://data.gov.il/api/action/datastore_search?resource_id=d337959a-020a-4ed3-84f7-fca182292308'
fileobj = urllib.urlopen(url)
print fileobj.read()


import requests

print('Beginning file download with requests')

url="https://data.gov.il/dataset/covid-19/resource/9eedd26c-019b-433a-b28b-efcc98de378d/download/5-isolation-per-day-data.xlsx"
r = requests.get(url)

with open('data/isolation_per_day.xlsx', 'wb') as f:
    f.write(r.content)



# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)

with open('/Users/scott/Downloads/cat2.jpg', 'wb') as f:
    f.write(datatowrite)

import pandas as pd
import os

os.getcwd()

import urllib.request

print('Beginning file download with urllib2...')

urllib.request.urlretrieve(url, 'data')
import io
import requests
import xlrd
# url="https://data.gov.il/dataset/f54e79b2-3e6b-4b65-a857-f93e47997d9c/resource/9eedd26c-019b-433a-b28b-efcc98de378d/download/5-isolation-per-day-data.xlsx"
c=pd.read_excel(url)

urllib.request.urlretrieve(url, 'data/isolation_per_day.xlsx')



import requests
from   bs4 import BeautifulSoup
import os
import pandas as pd
from scrape_functions import scrape, getFormData
import time

# Set Parameters
dir = 'C:/Users/rmadhok/Dropbox (Personal)/EnvironmentalClearances/scrape/test'
url1 = 'http://environmentclearance.nic.in/gotosearch.aspx?pid=ECGranted'
url2 = 'http://environmentclearance.nic.in/Search.aspx'

# Initiate Master Data List
data = []

# Start Session
s = requests.Session()
s.headers.update({'user-agent': 'Mozilla/5.0'})

# Scrape Page 1
print 'Scraping Page:', str(1)
r = s.get(url1) 
data += scrape(r.content)

# Get Form Data for Page 1
VIEWSTATE, GENERATOR, VALIDATION = getFormData(r.content)

# Scrape All Pages
lastPage = 300
for page in range(2, 4):
    try:
        print "Scraping Page:", page
        # Post form Data for subsequent page
        r = s.post(
            url2,
            data={ 
                'ww':                   'rr|GridView1',
                'a':                    'rb1',
                'ddlstatus':            'UPEChome',
                'ddlyear':              '-All Years-',
                'ddlcategory':          '-All Category-',
                'ddlstate':             '-All State-',
                'textbox2':             '',
                'DropDownList1':        'UPEC',
                #'__ASYNCPOST': 'true',
                '__EVENTTARGET':        'GridView1',
                '__EVENTARGUMENT':      'Page${}'.format(page),
                '__VIEWSTATE':          VIEWSTATE,
                '__VIEWSTATEGENERATOR': GENERATOR,
                '__EVENTVALIDATION':    VALIDATION,
                '__LASTFOCUS':          ''
                }
            )
        with open('page-{}.html'.format(page), 'w') as log:
            log.write(r.content)

        # Scrape Page
        data += scrape(r.content)

        # Get Form Data
        VIEWSTATE, GENERATOR, VALIDATION = getFormData(r.content)

    # Exit loop when reach last page    
    except:
        print "Could Not Scrape."
        break

# Write to CSV
data_full = pd.DataFrame(data)
data_full.to_csv('ec_data.csv', encoding = 'utf-8')


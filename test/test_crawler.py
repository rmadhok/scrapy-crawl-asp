import requests
from   bs4 import BeautifulSoup
import os
import pandas as pd
from   scrape_functions import *

# Set Parameters
dir = 'C:/Users/rmadhok/Dropbox (Personal)/EnvironmentalClearances/data'
url_a1 = 'http://environmentclearance.nic.in/gotosearch.aspx?pid=ECGranted'
url_a2 = 'http://environmentclearance.nic.in/Search.aspx'
url_b = 'http://environmentclearance.nic.in/onlinesearch_state_main.aspx?type=EC&status=1'


# Initiate Master Data List
data = []

# Start Session
s = requests.Session()
s.headers.update({'user-agent': 'Mozilla/5.0'})

# Scrape Page 1
print 'Scraping Page: ' + str(1) + '...'
#r = s.get(url_a1) 
r = s.get(url_b)
data += scrape_state(r.content)

# Get Form Data for Page 1
VIEWSTATE, GENERATOR, VALIDATION = getFormData(r.content)

# Scrape All Pages
lastPage = 320
for page in range(2, 4):
    try:
        print "Scraping Page: " + str(page) + "..."
        # Post form Data for subsequent page
        r = s.post(
            url_b,
            data={ 
                'ww':                   'rr|GridView1',
                'a':                    'rb2',
                #'a':                    'rb1',
                'ddlstatus':            'EC',
                #'ddlstatus':            'UPEChome',
                'ddlyear':              '-All Years-',
                'ddlcategory':          '-All Category-',
                'ddlstate':             '-All State-',
                'textbox2':             '',
                #'DropDownList1':        'UPEC',
                #'__ASYNCPOST': 'true',
                '__EVENTTARGET':        'GridView1',
                '__EVENTARGUMENT':      'Page${}'.format(page),
                '__VIEWSTATE':          VIEWSTATE,
                '__VIEWSTATEGENERATOR': GENERATOR,
                '__EVENTVALIDATION':    VALIDATION,
                '__LASTFOCUS':          ''
                }
            )

        # Scrape Page
        data += scrape_state(r.content)

        # Get Form Data
        VIEWSTATE, GENERATOR, VALIDATION = getFormData(r.content)

    # Exit loop when reach last page    
    except:
        print "Reached last page."
        break

# Write to CSV
os.chdir(dir)
data_full = pd.DataFrame(data)
data_full.to_csv('ec_state.csv', encoding = 'utf-8')


"""
=== Web Scraper for pulling environmental clearance data ===
The scraper cycles through every page on the start url
and builds a useable dataset. The website runs on ASP.net
so each page is reached using a form request and posting
javascript arguements. 

USE: 
* For scraping central data, set page 1 to url_a1 and
    post to url_a2, and use the scrape_central function 
* For scraping state data, set page 1 and post to url_b
    and use the scrape_state function.
"""
# META
__author__ = "Raahil Madhok"
__copyright__ = "Copyright 2016"
__version__ = "1.0"
__maintainer__ = "Raahil Madhok"
__email__ = "raahil_madhok@hks.harvard.edu"
__status__ = "Production"


# Import Libraries
import requests
from   bs4 import BeautifulSoup
import os
import pandas as pd
from   scrape_functions import *

## Set Parameters
# Set Directory for Writing Data
dir = 'C:/Users/rmadhok/Dropbox (Personal)/EnvironmentalClearances/data'
# Set URLs to follow and scrape
url_a1 = 'http://environmentclearance.nic.in/gotosearch.aspx?pid=ECGranted'                 #Start url for central data
url_a2 = 'http://environmentclearance.nic.in/Search.aspx'                                   #Post url for next page central data                    
url_b = 'http://environmentclearance.nic.in/onlinesearch_state_main.aspx?type=EC&status=1'  #Start and post url for state data

# Initiate session object
# Persist header for validating next page call
s = requests.Session()
s.headers.update({'user-agent': 'Mozilla/5.0'})

# Initiate Master Data list
data = []

# Scrape Start Page
# --- FOR CENTRAL DATA use url_a1
# --- FOR STATE DATA use url_b
print 'Scraping Page: ' + str(1) + '...'
#r = s.get(url_a1) 
r = s.get(url_b)
data += scrape_state(r.content)

# Get Form Data for Page 1
VIEWSTATE, GENERATOR, VALIDATION = getFormData(r.content)

# Scrape All Pages
# --- FOR CENTRAL DATA post to url_a2
# --- FOR STATE DATA post to url_b
lastPage = 320
for page in range(2, lastPage):
    try:
        print "Scraping Page: " + str(page) + "..."
        # Use form data from current page to get next page data
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

        # Add page data to master 
        data += scrape_state(r.content)

        # Get Current page Form Data
        VIEWSTATE, GENERATOR, VALIDATION = getFormData(r.content)

    # Exit loop when reach last page    
    except:
        print "Reached last page."
        break

# Write to CSV
os.chdir(dir)
data_full = pd.DataFrame(data)
data_full.to_csv('ec_state.csv', encoding = 'utf-8')


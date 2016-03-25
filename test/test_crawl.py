import os
from bs4 import BeautifulSoup
import urllib
import requests
import mechanize
import pandas as pd

# Directory
dir_write = '/Users/rmadhok/Dropbox (Personal)/EnvironmentalClearances/data'

# top url
url = 'http://environmentclearance.nic.in/gotosearch.aspx?pid=ECGranted'

# Read page and Soup
br = mechanize.Browser()
br.open(url)
html = br.response().read()
soup = BeautifulSoup(html, 'html.parser')

table = soup.find("table", {"class" : "ez1"})
rows = table.findAll('tr')
currentPage = table.find('tr', {'class': 'black'}).span.text

master = []
for row in rows[1:len(rows)-1]:

	my_dict = {}
	cols = row.findAll('td')
	
	if len(cols) == 38:
		my_dict['state'] = cols[14].text.strip()
		my_dict['district'] = cols[17].text.strip()
		my_dict['village'] = cols[20].text.strip()
		my_dict['proponent'] = cols[35].text.strip()
		my_dict['proposal_no'] = cols[4].text.strip()
		my_dict['file_no'] = cols[7].text.strip()
		my_dict['proposal_name'] = cols[10].text.strip()
		my_dict['sector'] = cols[34].text.strip()
		my_dict['date_tor_apply'] = cols[24].text.strip()
		my_dict['date_tor_granted'] = cols[27].text.strip()
		my_dict['date_ec_receipt'] = cols[24].text.strip()
		my_dict['date_ec_granted'] = cols[33].text.strip()
		compliances = cols[37].findAll('img', {'src': 'images/ec.png'})
		my_dict['comp_submit'] = len(compliances)

		master.append(my_dict)

	if len(cols) == 29:
		my_dict['state'] = cols[14].text.strip()
		my_dict['district'] = cols[17].text.strip()
		my_dict['village'] = cols[20].text.strip()
		my_dict['proponent'] = cols[26].text.strip()
		my_dict['proposal_no'] = cols[4].text.strip()
		my_dict['file_no'] = cols[7].text.strip()
		my_dict['proposal_name'] = cols[10].text.strip()
		my_dict['sector'] = cols[25].text.strip()
		my_dict['date_tor_apply'] = None
		my_dict['date_tor_granted'] = None
		my_dict['date_ec_receipt'] = None
		my_dict['date_ec_granted'] = cols[24].text.strip()
		compliances = cols[28].findAll('img', {'src': 'images/ec.png'})
		my_dict['comp_submit'] = len(compliances)

		master.append(my_dict)

data = pd.DataFrame(master)
os.chdir(dir_write)
data.to_csv('ec_data.csv')
from   bs4 import BeautifulSoup
import os
import requests
import pandas as pd
from unidecode import unidecode

dir = 'C:/Users/rmadhok/Dropbox (Personal)/EnvironmentalClearances/scrape/test'
url = 'http://environmentclearance.nic.in/onlinesearch_state_main.aspx?type=EC&status=1'
top = 'http://environmentclearance.nic.in/'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find("table", {"class" : "ez1"})
rows = table.findAll('tr')

data = []
for row in rows[1:]:
	item = {}
	cols = row.findAll('td')

	if len(cols) == 33:
		item['state'] = cols[14].text.strip()
		item['district'] = cols[17].text.strip()
		item['teshil'] = cols[20].text.strip()
		item['proponent'] = cols[29].text.strip()
		item['proposal_no'] = cols[4].text.strip()
		item['file_no'] = cols[7].text.strip()
		item['proposal_name'] = cols[10].text.strip()
		item['sector'] = cols[28].text.strip()
		item['date_tor_submit'] = cols[24].text.strip()
		item['date_ec_submit'] = cols[27].text.strip()
		item['status'] = cols[30].text.strip()
		eia = cols[31].findAll('img', {'src': 'images/eia.png'})
		ph = cols[31].findAll('img', {'src': 'images/pub.png'})
		risk = cols[31].findAll('img', {'src': 'images/Risk.gif'})
		add = cols[31].findAll('img', {'src': 'images/add.png'})
		cl = cols[31].findAll('img', {'src': 'images/coverletter1.jpg'})
		clearance = cols[31].findAll('img', {'src': 'images/ec.png'})
		item['eia_report'] = len(eia)
		item['pub_hearing_report'] = len(ph)
		item['risk_report'] = len(risk)
		item['additiona_report'] = len(add)
		item['cover_letter'] = len(cl)
		item['clearance_report'] = len(clearance)

		time_relative_url = cols[32].findAll('a', href = True)[0]['href']
		newurl = str(top + time_relative_url)
		timeline = requests.get(newurl)
		soup_time = BeautifulSoup(timeline.content, 'html.parser')
		table_time = soup_time.findAll('table')[1]
		rows_time = table_time.findAll('tr')
		for row_time in rows_time:
			cols_time = row_time.findAll('td')
			if len(cols_time) == 9:
				item['timeline_submitted1'] = unidecode(cols_time[0].text.strip())
				item['timeline_query_seiaa2'] = unidecode(cols_time[1].text.strip())
				item['timeline_resubmission3'] = unidecode(cols_time[2].text.strip())
				item['timeline_accept_seiaa4'] = unidecode(cols_time[3].text.strip())
				item['timeline_query_seac5'] = unidecode(cols_time[4].text.strip())
				item['timeline_resubmission6'] = unidecode(cols_time[5].text.strip())
				item['timeline_accept_seac7'] = unidecode(cols_time[6].text.strip())
				item['timeline_forward_seiaa8'] = unidecode(cols_time[7].text.strip())
				item['timeline_ec_granted9'] = unidecode(cols_time[8].text.strip())

		data.append(item)

os.chdir(dir)
data_full = pd.DataFrame(data)
data_full.to_csv('ec_state.csv', encoding = 'utf-8')





		
	
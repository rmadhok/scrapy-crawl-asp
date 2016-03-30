from bs4 import BeautifulSoup
from unidecode import unidecode
import requests

def scrape_central(page):
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find("table", {"class" : "ez1"})
    rows = table.findAll('tr')
    page = int(table.find('tr', {'class': 'black'}).span.text)

    data_page = []
    for row in rows[1:]:
        item = {}
        cols = row.findAll('td')

        if len(cols) == 38:
            item['page'] = page
            item['state'] = cols[14].text.strip()
            item['district'] = cols[17].text.strip()
            item['village'] = cols[20].text.strip()
            item['proponent'] = cols[35].text.strip()
            item['proposal_no'] = cols[4].text.strip()
            item['file_no'] = cols[7].text.strip()
            item['proposal_name'] = cols[10].text.strip()
            item['sector'] = cols[34].text.strip()
            item['date_tor_apply'] = cols[24].text.strip()
            item['date_tor_granted'] = cols[27].text.strip()
            item['date_ec_receipt'] = cols[24].text.strip()
            item['date_ec_granted'] = cols[33].text.strip()
            clearance = cols[37].findAll('img', {'src': 'images/ec.png'})
            tor = cols[37].findAll('img', {'src': 'images/tor.png'})
            pfr = cols[37].findAll('img', {'src': 'images/pfr.png'})
            forms = cols[37].findAll('img', {'src': 'images/forms.png'})
            com = cols[37].findAll('img', {'src': 'images/com.png'})
            mon = cols[37].findAll('img', {'src': 'images/mon.png'})
            add = cols[37].findAll('img', {'src': 'images/add.png'})
            item['clearance_report'] = len(clearance)
            item['tor_report'] = len(tor)
            item['pf_report'] = len(pfr)
            item['form1'] = len(forms)
            item['compliance_report'] = len(com)
            item['monitor_report'] = len(mon)
            item['additional_report'] = len(add)
            data_page.append(item)
          

        if len(cols) == 29:
            item['page'] = page
            item['state'] = cols[14].text.strip()
            item['district'] = cols[17].text.strip()
            item['village'] = cols[20].text.strip()
            item['proponent'] = cols[26].text.strip()
            item['proposal_no'] = cols[4].text.strip()
            item['file_no'] = cols[7].text.strip()
            item['proposal_name'] = cols[10].text.strip()
            item['sector'] = cols[25].text.strip()
            item['date_tor_apply'] = None
            item['date_tor_granted'] = None
            item['date_ec_receipt'] = None
            item['date_ec_granted'] = cols[24].text.strip()
            clearance = cols[28].findAll('img', {'src': 'images/ec.png'})
            tor = cols[28].findAll('img', {'src': 'images/tor.png'})
            pfr = cols[28].findAll('img', {'src': 'images/pfr.png'})
            forms = cols[28].findAll('img', {'src': 'images/forms.png'})
            com = cols[28].findAll('img', {'src': 'images/com.png'})
            mon = cols[28].findAll('img', {'src': 'images/mon.png'})
            add = cols[28].findAll('img', {'src': 'images/add.png'})
            item['clearance_report'] = len(clearance)
            item['tor_report'] = len(tor)
            item['pf_report'] = len(pfr)
            item['form1'] = len(forms)
            item['compliance_report'] = len(com)
            item['monitor_report'] = len(mon)
            item['additional_report'] = len(add)
            data_page.append(item)
    
    return data_page 

def scrape_state(page):
    top = 'http://environmentclearance.nic.in/'
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find("table", {"class" : "ez1"})
    rows = table.findAll('tr')
    page = int(table.find('tr', {'class': 'black'}).span.text)

    data_page = []
    for row in rows[1:]:
        item = {}
        cols = row.findAll('td')

        if len(cols) == 33:
            item['page'] = page
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

            data_page.append(item)

    return data_page

def getFormData(page):
    soup = BeautifulSoup(page, 'html.parser')
    viewstate  = soup.find('input', {'id': '__VIEWSTATE'         })['value']
    generator  = soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value']
    validation = soup.find('input', {'id': '__EVENTVALIDATION'   })['value']
    return (viewstate, generator, validation)

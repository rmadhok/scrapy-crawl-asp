from bs4 import BeautifulSoup

def scrape(page):
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

def getFormData(page):
    soup = BeautifulSoup(page, 'html.parser')
    viewstate  = soup.find('input', {'id': '__VIEWSTATE'         })['value']
    generator  = soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value']
    validation = soup.find('input', {'id': '__EVENTVALIDATION'   })['value']
    return (viewstate, generator, validation)

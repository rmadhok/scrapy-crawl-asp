import urllib
import os
import mechanize
import requests
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from eccrawler.items import EccrawlerItem
from scrapy.http import FormRequest, Request
from scrapy.utils.response import open_in_browser
from bs4 import BeautifulSoup

class ECSpider(CrawlSpider):
	name = 'EC'
	start_urls = ['http://environmentclearance.nic.in/gotosearch.aspx?pid=ECGranted']

	def parse(self, response):
		
		open_in_browser(response)
		soup = BeautifulSoup(response.body_as_unicode(), 'html.parser')

		table = soup.find("table", {"class" : "ez1"})
		rows = table.findAll('tr')

		for row in rows[1:]:
			item = EccrawlerItem()
			cols = row.findAll('td')

			if len(cols) == 38:
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
				compliances = cols[37].findAll('img', {'src': 'images/ec.png'})
				item['comp_submit'] = len(compliances)

				yield item

		 	if len(cols) == 29:
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
				compliances = cols[28].findAll('img', {'src': 'images/ec.png'})
				item['comp_submit'] = len(compliances)

	 			yield item	

	def parse_page(self, response):

		currentPage = 1
		while (currentPage < 4):
			nextPage = currentPage + 1

			EVENTVALIDATION = response.xpath("//*[@id='__EVENTVALIDATION']/@value").extract()
			VIEWSTATE = response.xpath("//*[@id='__VIEWSTATE']/@value").extract()
			#nextPage = currentPage + 1
			data = {
			#	'ww': 'rr|GridView1',
			#	'a': 'rb1',
				'ddlstatus': 'UPEChome',
				'ddlyear': '-All Years-',
				'ddlcategory': '-All Category-',
				'ddlstate': '-All State-',
				'textbox2': '',
				'DropDownList1': 'UPEC',
				'__EVENTTARGET': 'GridView1',
				'__EVENTARGUMENT': "'Page$" + str(nextPage) + "'",
			#	'__LASTFOCUS': '',
				'__VIEWSTATE': VIEWSTATE, 
			#	'__VIEWSTATEGENERATOR': 'BBBC20B8',
				'__EVENTVALIDATION': EVENTVALIDATION,
			#	'__ASYNCPOST': 'true',
			#	'': ''
				}
			yield FormRequest.from_response(response, 
				formname = 'form1', 
				formdata=data, 
				callback= self.parse
				 )

		






from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from eccrawler.items import EccrawlerItem
from scrapy.http import FormRequest, Request
from scrapy.utils.response import open_in_browser
from bs4 import BeautifulSoup

class ECSpider(CrawlSpider):
	name = 'EC'
	allowed_domains = ['http://environmentclearance.nic.in']
	#start_urls = ['http://environmentclearance.nic.in/gotosearch.aspx?pid=ECGranted']
	start_urls = ['http://environmentclearance.nic.in/Search.aspx']

	def parse(self, response):
		EVENTVALIDATION = response.xpath("//*[@id='__EVENTVALIDATION']/@value").extract()
		VIEWSTATE = response.xpath("//*[@id='__VIEWSTATE']/@value").extract()
		for i in range(1, 5):
			yield FormRequest(
				'http://environmentclearance.nic.in/Search.aspx',
				headers = {'user-agent': 'Mozilla/5.0'},
				formdata = {
					'ww': 'rr|GridView1',
					'__LASTFOCUS': '',
					'__EVENTTARGET': 'GridView1',
					'__EVENTARGUMENT': 'Page${}'.format(i),
					'__VIEWSTATE': VIEWSTATE, 
					'__EVENTVALIDATION': EVENTVALIDATION,
					'a': 'rb1',
					'dd1status': 'UPEChome',
					'ddlyear': '-All Years-',
					'ddlcategory': '-All Category-',
					'ddlstate': '-All State-',
					'textbox2': '',
					'DropDownList1': 'UPEC'
					}, 
				callback = self.parse_item
			) 

	def parse_item(self, response):
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

	 	
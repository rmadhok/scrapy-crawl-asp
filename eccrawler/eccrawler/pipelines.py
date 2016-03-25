# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from eccrawler import settings

def write_to_csv(item):
	writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
	writer.writerow([item[key] for key in item.keys()])

class EccrawlerPipeline(object):
    def process_item(self, item, spider):
    	write_to_csv(item)
    	return item

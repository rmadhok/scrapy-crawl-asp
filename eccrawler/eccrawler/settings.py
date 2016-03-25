# -*- coding: utf-8 -*-

# Scrapy settings for eccrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'eccrawler'

SPIDER_MODULES = ['eccrawler.spiders']
NEWSPIDER_MODULE = 'eccrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'eccrawler (+http://www.yourdomain.com)'

ITEM_PIPELINES = {'eccrawler.pipelines.EccrawlerPipeline' : 300}
csv_file_path = 'C:/Users/rmadhok/Dropbox (Personal)/EnvironmentalClearances/data/ec_data.csv'
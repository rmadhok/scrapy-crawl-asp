# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EccrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    proposal_no = scrapy.Field()
    file_no = scrapy.Field()
    proposal_name = scrapy.Field()
    state = scrapy.Field()
    district = scrapy.Field()
    village = scrapy.Field()
    date_tor_apply = scrapy.Field()
    date_tor_granted = scrapy.Field()
    date_ec_receipt = scrapy.Field()
    date_ec_granted = scrapy.Field()
    sector = scrapy.Field()
    proponent = scrapy.Field()
    comp_submit = scrapy.Field()

    pass

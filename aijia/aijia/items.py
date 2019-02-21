# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AijiaItem(scrapy.Item):
    house_title = scrapy.Field()
    house_price = scrapy.Field()
    house_manager = scrapy.Field()

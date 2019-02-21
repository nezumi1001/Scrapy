# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    d1_name = scrapy.Field()
    d2_level = scrapy.Field()
    d3_loc = scrapy.Field()
    d4_shop = scrapy.Field()
    d5_deal = scrapy.Field()

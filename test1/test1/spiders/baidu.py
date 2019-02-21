# -*- coding: utf-8 -*-
import scrapy
from test1.items import Test1Item


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        item = Test1Item()
        item['title'] = response.xpath('//*[@id="u1"]/a[1]/text()').extract_first()
        item['url'] = response.xpath('//*[@id="u1"]/a[1]/@href').extract_first()
        print('='*100)
        print(item['title'])
        print(item['url'])
        print('=' * 100)
        yield item

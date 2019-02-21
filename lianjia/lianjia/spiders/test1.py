# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem

class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['m.lianjia.com']
    start_urls = ['https://m.lianjia.com/sh/jingjiren/?page_size=15&_t=1&offset={}'.format(i) for i in range(0, 16, 15)]

    def parse(self, response):
        member_list = response.xpath('//ul[@class="lists q_agentlist"]/li')
        for member in member_list:
            item = LianjiaItem()
            item['d1_name'] = member.xpath('div/div[2]/div[1]/span[1]/a/text()').extract_first().strip()
            item['d2_level'] = member.xpath('div/div[2]/div[1]/span[2]/text()').extract_first().strip()
            item['d3_loc'] = member.xpath('div/div[2]/div[2]/span[1]/text()').extract_first().strip()
            item['d4_shop'] = member.xpath('div/div[2]/div[2]/span[3]/text()').extract_first().strip()
            member_urls = member.xpath('div/div[2]/div[1]/span[1]/a/@href').extract_first()
            member_urls = response.urljoin(member_urls)
            yield scrapy.Request(member_urls, meta={'item': item}, callback=self.detail)

    def detail(self, response):
        item = response.meta['item']
        item['d5_deal'] = response.xpath('//div[@class="data_info tab_bar flexbox"]/div[1]/div[1]/text()').extract_first()
        yield item

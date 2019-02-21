# -*- coding: utf-8 -*-
import scrapy
from aijia.items import AijiaItem


class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['sh.5i5j.com']
    start_urls = ['https://sh.5i5j.com/zufang/n1']

    def parse(self, response):
        house_list = response.xpath('//ul[@class="pList"]/li')
        for house in house_list:
            item = AijiaItem()
            item['house_title'] = house.xpath('div[2]/h3/a/text()').extract_first()
            item['house_price'] = house.xpath('div[2]/div[1]/div/p[1]/strong/text()').extract_first()
            # 详情页
            detail_url = house.xpath('div[2]/h3/a/@href').extract_first()
            detail_url = response.urljoin(detail_url)
            yield scrapy.Request(detail_url, meta={'item': item}, callback=self.detail)

        # 下一页
        next_url = response.xpath('//div[@class="pageBox"]/div[2]/a[1]/@href').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)

    def detail(self, response):
        item = response.meta['item']
        item['house_manager'] = response.xpath('//div[@class="daikansty "]/ul/li[2]/h3/a/text()').extract_first()
        yield item


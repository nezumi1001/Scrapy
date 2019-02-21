# -*- coding: utf-8 -*-
import scrapy
from yaozhi.items import YaozhiItem


class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['yaozh.com']
    # start_urls = ['https://www.yaozh.com/']
    cookie = {
        'acw_tc': '2f624a6815501301861053056e74427cb2f886f2b11d34f41184a993aafe47',
        'PHPSESSID': '1ufn6ub1dvst2qdcng88vestp3',
        'UtzD_f52b_saltkey': 'uIr9JT1U',
        'UtzD_f52b_lastvisit': '1550126757',
        'yaozh_uidhas': '1',
        'MEIQIA_VISIT_ID': '1HC92sfE1HaS1aSjtFUd4nqebfj',
        'Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94': '1550130187%2C1550130280%2C1550130323',
        'UtzD_f52b_ulastactivity': '1550130356%7C0',
        'yaozh_userId': '693114',
        'UtzD_f52b_creditnotice': '0D0D2D0D0D0D0D0D0D638152',
        'UtzD_f52b_creditrule': '%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95',
        'yaozh_mylogin': '1550195046',
        'UtzD_f52b_creditbase': '0D0D2D0D0D0D0D0D0',
        'yaozh_logintime': '1550195763',
        'yaozh_user': '693114%09pashanhu1001',
        'db_w_auth': '638152%09pashanhu1001',
        'UtzD_f52b_lastact': '1550195764%09uc.php%09',
        'UtzD_f52b_auth': '0480bOVtKSBbgybH4sclbZn3QZfG1xUw4%2BfkCeDeCluj9wS1kNw3DotXs4CS6vi6omyNE%2FVqBBrRw7AdAKZZVABVlA8',
        'Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94': '1550195768'
    }

    def start_requests(self):
        '''由于需要爬取登录后的网站，必须重写 start_requests'''
        url_login = 'https://www.yaozh.com/login/'
        yield scrapy.Request(url_login, cookies=self.cookie, callback=self.parse_login)

    def parse_login(self, response):
        '''验证是否已经登录'''
        name = response.xpath('//div[@class="header"]/div/div[2]/a/text()').extract_first()
        print('='*100)
        print('First time: {}'.format(name))
        print('='*100)
        url_home = 'https://www.yaozh.com/'
        yield scrapy.Request(url_home, cookies=self.cookie, callback=self.parse_home)

    def parse_home(self, response):
        '''转至主页再次验证是否已经登录'''
        name = response.xpath('//div[@class="header"]/div/div[2]/a/text()').extract_first()
        print('=' * 100)
        print('Second time: {}'.format(name))
        print('=' * 100)

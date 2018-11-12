# -*- coding: utf-8 -*-
import scrapy

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://zhihu.com/']


    # def parse(self, response):
    #     pass

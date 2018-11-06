# -*- coding: utf-8 -*-
import scrapy


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    def parse(self, response):
        pass

# -*- coding: utf-8 -*-
import scrapy
import json,re

from scrapy import Selector
class QunarSpider(scrapy.Spider):
    name = 'qunar'
    allowed_domains = ['qunar.com']
    start_urls = ['https://tuan.qunar.com/vc/index.php?category=all_r&limit=0%2C30',
                  'https://tuan.qunar.com/vc/index.php?category=all_i&limit=0%2C30',
                  'https://tuan.qunar.com/vc/index.php?category=all_o&limit=0%2C30']
    def parse(self, response):
        if response.url.find('all_r') > 0:
            print('周边游')
        elif response.url.find('all_i') > 0:
            print('国内游')
        elif response.url.find('all_o') > 0:
            print('国外游')
        json_str = response.xpath('.').re_first('<script>pageLoader\(({"id":"tuan-list".*?)\);</script>')

        html_str = json.loads(json_str)['html']

        selector_obj = Selector(text=html_str)

        detaileUrl_list = selector_obj.css('ul.cf li a::attr(href)').extract()
        for detaileUrl in detaileUrl_list:
            yield response.follow(url=detaileUrl,callback=self.detaile_link)

    def detaile_link(self,response):
        full_url = response.xpath('.').re_first("= '(.*?)' +")
        yield response.follow(url=full_url,callback=self.detaile_data)


    def detaile_data(self,response):
        print(response.status)
        dataDict = {}
        # dataDict['title'] = ''.join(response.xpath('//div[@class="summary"]/h1//text()').extract()).replace('\n','').strip()
        dataDict['title'] = ''.join(response.css('div.summary h1 ::text').extract()).replace('\n','').strip()

        print(dataDict['title'])


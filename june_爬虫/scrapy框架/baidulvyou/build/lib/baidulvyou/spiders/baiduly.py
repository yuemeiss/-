# -*- coding: utf-8 -*-
import scrapy


class BaidulySpider(scrapy.Spider):
    name = 'baiduly'
    allowed_domains = ['lvyou.baidu.com']
    start_urls = ['https://lvyou.baidu.com/scene/t-all_s-all_a-all_l-all?rn=12&pn=0']

    def parse(self, response):
        print(response.status)
        # with open('data.html','w') as file:
        #     file.write(response.text)
        #提取详情页链接
        detaile = response.xpath('//li[@class="filter-result-item "]//h3/a/@href').extract()
        for i in detaile:
            yield scrapy.Request()
        #获取下一页
        pageurl = response.xpath('//span[@class="pagelist"]//a[@class="nslog"]/@href').extract_first()

        print(detaile)


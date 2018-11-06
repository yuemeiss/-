# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from baidulvyou.items import BaidulvyouItem


class Baidulvyou1Spider(CrawlSpider):
    name = 'baidulvyou1'
    allowed_domains = ['lvyou.baidu.com']
    start_urls = ['https://lvyou.baidu.com/scene/t-all_s-all_a-all_l-all?rn=12&pn=0']

    rules = (
        #下一页
        Rule(LinkExtractor(allow=r'\?rn=\d+&pn=\d+',restrict_xpaths=('//span[@class="pagelist"]//a[@class="nslog"]',)), follow=True),
        #详情页
        Rule(LinkExtractor(allow=r'/\w+/', restrict_xpaths=('//li[@class="filter-result-item "]//h3/a',)),
             callback='parse_data',),

    )

    # def parse_item(self, response):
    #     # print(response.status)
    #     pass

    def parse_data(self,response):
        # print(response.status)
        # response
        baidu = BaidulvyouItem()
        baidu['address'] = response.xpath('//div[@class="dest-name "]//a/text()').extract_first()
        baidu['img_url'] = response.xpath('//ul[@id="J_pic-slider"]//a/img/@src').extract()
        baidu['grade'] = ''.join(response.xpath('//div[@class="main-score"]/text()').extract()).replace('\n','').replace(' ','')
        baidu['comment_num'] = response.xpath('//div[@class="main-score"]/a[@class="remark-count"]/text()').extract_first()
        baidu['intro'] = response.xpath('//div[@class="main-info-wrap"]//div[@class="main-desc"]/p/text()').extract_first().strip()
        baidu['best_offer'] = '-'.join(response.xpath('//div[@class="main-intro"]//text()').extract()).replace('\n','').replace(' ','')
        baidu['comment_list'] = []
        comment_list = response.xpath('//div[@class="remark-list"]/div')
        for com in comment_list:
            comdict = {}
            comdict['com_content'] = com.xpath('.//div[@class="ri-body"]//text()').extract()
            comdict['com_userName'] = com.xpath('.//div[@class="ri-avatar-wrap"]/a/@title').extract()
            comdict['com_pub_time'] = com.xpath('.//div[@class="ri-header"]/div[@class="ri-time"]/text()').extract_first()
            comdict['available'] = com.xpath('.//a[@class="ri-dig ri-dig-available"]/span/text()').extract()
            comdict['replynums'] = com.xpath('.//a[@class="ri-comment"]/span/text()').extract()
            baidu['comment_list'].append(comdict)
        yield baidu
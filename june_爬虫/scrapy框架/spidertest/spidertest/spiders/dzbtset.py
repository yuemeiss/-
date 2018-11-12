# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from spidertest.items import SpidertestItem,Dzb_ClassName


class DzbtsetSpider(CrawlSpider):
    name = 'dzbtset'
    allowed_ = ['top.chinaz.com']
    start_urls = ['http://top.chinaz.com/']
    # / hangye / index_yule_yinyue.html

    rules = (
        Rule(LinkExtractor(allow=r'/.*html',restrict_xpaths=('//div[@class="MainWebClass clearfix"]/dl//a',)), callback='parse_item', follow=False),
    )
    def parse_start_url(self, response):
        cls_list = response.xpath('//div[@class="MainWebClass clearfix"]//dd/a')
        for cls in cls_list:
            clsdata = Dzb_ClassName()
            # 分类名
            clsdata['dzb_cname'] = cls.xpath('./text()').extract_first('未知')
            # print(dzb_cname)
            # 分类URL
            clsdata['dzb_curl'] = 'http:' + cls.xpath('./@href').extract_first('未知')
            # print(dzb_curl)
            yield  clsdata

    def parse_item(self, response):
        dat_list = response.xpath('//ul[@class="listCentent"]/li')
        for dat in dat_list:
            data = SpidertestItem()
            # 标题
            data['dzb_title']= dat.xpath('.//h3[@class="rightTxtHead"]/a/text()').extract_first('未知')
            # print(dzb_title)
            # 图片地址
            data['dzb_imgurl'] = 'http:' + dat.xpath('.//div[@class="leftImg"]/a/img/@src').extract_first('未知')
            # print(dzb_imgurl)
            # 域名
            data['dzb_domains'] = dat.xpath('.//h3[@class="rightTxtHead"]/span/text()').extract_first('未知')
            # print(dzb_domains)
            # 周排名
            data['dzb_rank'] = dat.xpath('.//p[@class="RtCData"][1]/a/text()').extract_first('未知')
            # 反链数
            data['dzb_number'] = dat.xpath('.//p[@class="RtCData"][4]/a/text()').extract_first('未知')
            # print(dzb_number)
            # 得分
            data['dzb_score'] = dat.xpath('.//div[@class="RtCRateCent"]/span/text()').extract_first('未知')
            # print(dzb_score)
            # 得分排名
            data['dzb_srank'] = dat.xpath('.//div[@class="RtCRateCent"]/strong/text()').extract_first('未知')
            data['dzb_intro'] =''.join(dat.xpath('.//p[@class="RtCInfo"]/text()').extract())
            yield data
        #下一页
        page_url = response.xpath('//div[@class="ListPageWrap"]/a[last()]/@href').extract_first()
        if page_url:
            yield response.follow(url=page_url,callback=self.parse_item)

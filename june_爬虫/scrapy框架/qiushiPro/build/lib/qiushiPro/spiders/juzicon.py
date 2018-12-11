# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qiushiPro.items import JuziconproField


class JuziconSpider(CrawlSpider):
    name = 'juzicon'
    allowed_domains = ['juzicon.com']
    # start_urls = ['https://www.juzicon.com/channels']
    sort_url = ['movies', 'novels', 'proses', 'animes', 'series']
    start_urls = ['https://www.juzicon.com/categories/works/{}'.format(i) for i in sort_url]
    # start_urls = ['https://www.juzicon.com/categories/works/movies']
    #解析内容列表
    flag = []
    rules = [
        # 作品分类
        # Rule(LinkExtractor(
        #     allow=r'.*?/.*',
        #     restrict_xpaths=('//div[@class="_3FDJg_weCbraNe1bRP_zLR_0"]//a',),
        # ), callback='parse_page',follow=False),
        # 详情链接
        Rule(LinkExtractor(
            allow=r'/.*',
            restrict_xpaths=('//div[@class="_1SM0XE6W8MbPeLmDragFJD_0"]/a')
        ), callback='parse_detaile', follow=False),
        # 下一页
        Rule(LinkExtractor(
            allow=r'.*=\d+',
            restrict_xpaths=('//ul[@class="el-pager"]//a',),
        ), follow=True),

    ]

    # 作品分类
    def parse_detaile(self, response):
        con_list = response.xpath('//section[@class="_3kJ_X8s2Fl1RMezfKtlens_0"]')
        for con in con_list:
            con_dict = {}
            con_dict['content'] = ','.join(
                con.xpath('.//div[@class="_1M-w2BKM75D4AvckCH596S_0"]//span/text()').extract()).replace(' ', '')
            con_dict['like'] = con.xpath('.//span[@class="_2NoMli8aRzS3nQig3U2aBr_0"]/text()').extract_first()
            con_dict['comment'] = con.xpath('.//span[@class="_3buMK5elpnD6oocG5zL0Z_0"]/text()').extract_first()
            self.flag.append(con_dict)
        page_url = response.xpath('//button[@class="btn-next"]/a/@href').extract_first()
        print(page_url)
        if page_url:
            yield response.follow(url=page_url, callback=self.parse_detaile)
        else:
            works = JuziconproField()
            works['img_url'] = response.css('div._12JB9cYBJJtNu0BHFnevFy_0 img::attr(src)').extract_first('0')
            works['title'] = response.css('h1._1lVYxFyFRSdZb9fMTHn0dt_0::text').extract_first('0')
            data = response.xpath('//script[@type="text/javascript"]/text()').re('"intro":(.*?),.*"tags":\[(".*?)\],')
            works['intro'] = data[0]
            works['tags'] = data[1]
            print(works['tags'])
            works['clsid_id'] = 1
            works['content_list'] = str(self.flag)
            print('==================================',len(works['content_list']))
            self.flag = []
            yield works

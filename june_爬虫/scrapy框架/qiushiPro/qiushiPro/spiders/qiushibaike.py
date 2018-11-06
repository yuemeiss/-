# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class QiushibaikeSpider(CrawlSpider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/',
                  # 'https://www.qiushibaike.com/hot/',
                  # 'https://www.qiushibaike.com/text/',
                  # 'https://www.qiushibaike.com/history/',
                  # 'https://www.qiushibaike.com/pic/',
                  # 'https://www.qiushibaike.com/textnew/'
                  ]
    # https://ishuo.cn/duanyu
    # http://www.shuoshuokong.com/ 说说控
    # https://www.juzicon.com/mip/authors/fd144490-0be2-453e-b708-3811539a3d20 句子控
    # 心理学吧

    rules = (
        #分类url
        Rule(LinkExtractor(allow=r'm/.+/$',restrict_css=('div#menu a')), callback='parse_item', follow=False),
        # 下一页
        Rule(LinkExtractor(allow=r''))
    )
    a = 0
    def parse_item(self, response):
        print(response.url)
        self.a += 1
        print(self.a)




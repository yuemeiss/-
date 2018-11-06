from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#只是用到了redis的去重和保存功能,并不能实现分布式
class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/']

    rules = [
        # 分类url
        Rule(
            LinkExtractor(
                allow=r'm/.+/$',
                restrict_css=('div#menu a',)
            ),
            # callback='parse_item',
            follow=False
        ),
        # # 下一页
        # Rule(
        #     LinkExtractor(
        #         allow=r'/.*/$',
        #         restrict_xpaths='//ul[@class="pagination"]/li/a'
        #     ),
        #     follow=True
        # ),
        #提取详情页
        Rule(
            LinkExtractor(
                allow=r'/a.*',
                restrict_xpaths='//div[@id="content-left"]//a[@class="contentHerf"]'
            ),
            callback='parse_detaile',
            follow=False
        ),
    ]

    def parse_detaile(self,response):
        print(response.url)


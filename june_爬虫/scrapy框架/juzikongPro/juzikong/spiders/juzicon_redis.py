from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider
from scrapy import Request

class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    allowed_domains = ['juzicon.com']
    name = 'juzicon_redis'
    redis_key = 'juzi:start_urls'  # 'https://www.juzicon.com/channels'


    rules = (
        # 作品分类
        Rule(LinkExtractor(
            allow=r'.*?/.*',
            restrict_xpaths=('//div[@class="_3FDJg_weCbraNe1bRP_zLR_0"]//a',),
        ), callback='parse_page', follow=False),
        # 下一页
        Rule(LinkExtractor(
            allow=r'.*=\d+',
            restrict_xpaths=('//ul[@class="el-pager"]//a',),
        ), follow=True),
    )

    #作品分类
    count = 0
    def parse_start_url(self, response):
        aa_list = response.xpath('//div[@class="_3FDJg_weCbraNe1bRP_zLR_0//dd"]')
        for aa in aa_list:
            title = aa.xpath('.//a/@title').extract_first()
            urls = aa.xpath('.//a/@href').extract_first()
            print(title,urls)
    def parse_page(self, response):
        pass
        # yield Request(url=response.url,callback=self.parse_next)
    def parse_next(self,response):
        pass
        # print(response.url)
    # def chenge_rules(self):
    #     self.ruler = (
    #
    # )


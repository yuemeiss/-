from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider


class MyCrawler(RedisCrawlSpider):
    """
    爬虫文件中只有两个地方跟我们单机版爬虫不一样
    1.继承的类不一样
    2.少了一个start_urls参数,多了一个redis_key:可根据这个key从redis数据库中获取爬虫的起始任务
    Spider that reads urls from redis queue (myspider:start_urls).
    """
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'

    rules = (
        # follow all links
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )
    #动态获取要爬取的域 ,一般不使用它 我们会使用allowed_domains
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MyCrawler, self).__init__(*args, **kwargs)

    def parse_page(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }

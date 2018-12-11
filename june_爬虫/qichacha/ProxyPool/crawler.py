# -*- coding:utf-8 -*-
# @time  :18-11-3 下午3:48    
# @Author :董振兵                
# @File   :crawler.py
import time,re
from utils import get_page
from lxml import etree


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self,callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理',proxy)
            proxies.append(proxy)
        return proxies
    def crawl_daili66(self,page_count=6):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(2,page_count + 1)]
        for url in urls:
            time.sleep(1)
            print('Crawling',url)
            html = get_page(url)
            if html:
                doc = etree.HTML(html)
                trs = doc.xpath('//div[contains(@class,"containerbox")]//table//tr[1]/following-sibling::tr')
                for tr in trs:
                    ip = tr.xpath('.//td[1]/text()')[0].strip()
                    port = tr.xpath('.//td[2]/text()')[0].strip()
                    yield ':'.join([ip,port])

    def crawl_swei360(self,page_count=7):
        """
        获取Proxy360
        :return: 代理
        """
        start_url = 'http://www.swei360.com/free/?page={}'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            time.sleep(1)
            print('Crawling',url)
            html = get_page(start_url)
            if html:
                doc = etree.HTML(html)
                lines = doc.xpath('//div[@id="list"]//tbody/tr')
                for line in lines:
                    ip = line.xpath('.//td[1]/text()')[0].strip()
                    port = line.xpath('.//td[2]/text()')[0].strip()
                    yield ':'.join([ip, port])

    def crawl_ip3366(self):
        for page in range(1, 7):
            time.sleep(1)
            start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            html = get_page(start_url)
            ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
            # \s * 匹配空格，起到换行作用
            re_ip_address = ip_address.findall(html)
            for address, port in re_ip_address:
                result = address + ':' + port
                yield result.replace(' ', '')

    def crawl_kxdaili(self):
        for i in range(1, 11):
            time.sleep(2)
            start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(i)
            html = get_page(start_url)
            if html:
                doc = etree.HTML(html)
                lines = doc.xpath('//div[@id="list"]//tbody/tr')
                for line in lines:
                    ip = line.xpath('.//td[1]/text()')[0].strip()
                    port = line.xpath('.//td[2]/text()')[0].strip()
                    yield ':'.join([ip, port])


    def crawl_89ip(self):
        for i in range(1,7):
            time.sleep(1)
            start_url = 'http://www.89ip.cn/index_{}.html'.format(i)
            html = get_page(start_url)
            if html:
                doc = etree.HTML(html)
                lines = doc.xpath('//table[@class="layui-table"]/tbody/tr')
                for line in lines:
                    ip = line.xpath('.//td[1]/text()')[0].strip()
                    port = line.xpath('.//td[2]/text()')[0].strip()
                    yield ':'.join([ip, port])

    def crawl_xicidaili(self):
        for i in range(1, 18):
            time.sleep(1)
            start_url = 'http://www.xicidaili.com/nn/{}'.format(i)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTQxYWU4MTVjZWM0M2JiYmNlYTE0NjU3YzIwMGNhZWY5BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTN2Wm8zd21WL2FTSC9HNzYza0s4ZlozUHFFM1JuQUZNTWtYR0xGazRlajg9BjsARg%3D%3D--d07c041eb4059c3cbe03e7e088b78daf387f5135; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1541564789; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1541564821',
                'Host': 'www.xicidaili.com',
                'Referer': 'http://www.xicidaili.com/nn',
                'Upgrade-Insecure-Requests': '1',
            }
            html = get_page(start_url, options=headers)
            if html:
                find_trs = re.compile('<tr class.*?>(.*?)</tr>', re.S)
                trs = find_trs.findall(html)
                for tr in trs:
                    find_ip = re.compile('<td>(\d+\.\d+\.\d+\.\d+)</td>')
                    re_ip_address = find_ip.findall(tr)
                    find_port = re.compile('<td>(\d+)</td>')
                    re_port = find_port.findall(tr)
                    for address, port in zip(re_ip_address, re_port):
                        address_port = address + ':' + port
                        yield address_port.replace(' ', '')


# test = Crawler()
# ips = test.crawl_xicidaili()
# # print(ips)
# for i in ips:
#     print(i)

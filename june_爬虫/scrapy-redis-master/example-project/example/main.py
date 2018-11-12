#-*- coding:utf-8 -*-        
# @time  :18-11-6 上午10:50    
# @Author :董振兵                
# @File   :main
import sys,os
from scrapy.cmdline import execute
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy','crawl','dmoz'])
execute(['scrapy','crawl','mycrawler_redis'])


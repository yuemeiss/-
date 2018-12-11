#-*- coding:utf-8 -*-        
# @time  :18-11-30 上午11:47    
# @Author :董振兵                
# @File   :main
import os,sys
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','zhihu'])
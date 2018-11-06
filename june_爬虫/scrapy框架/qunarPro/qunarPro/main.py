#-*- coding:utf-8 -*-        
# @time  :18-11-2 上午10:27    
# @Author :董振兵                
# @File   :main.py
import sys,os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','qunar'])

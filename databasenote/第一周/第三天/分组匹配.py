# -*- coding:utf-8 -*-
import re

emails = ['ljhyigehaoren@sina.com','2295808193@qq.com','asncswncl@qq.cn']

for i in emails:
    ret = re.match('[a-z0-9]+@(sina|qq)\.(com|cn)',i)
    if ret:
        print(ret,i)

#<html>123456<html>

# ret = re.match('<(\w+)>\d+<\\1>','<html>123456<html>')
# # ret = re.match(r'<(\w+)>\d+<\1>','<html>123456<html>')
# print(ret.group(),ret.groups())

ret = re.findall('<(?P<name1>\w+)>\d+<(?P=name1)>','<html>123456<html>')
# ret = re.match(r'<(\w+)>\d+<\1>','<html>123456<html>')
print(ret)
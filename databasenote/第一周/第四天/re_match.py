# -*- coding:utf8 -*-
# match:从起始位置开始匹配，一旦
# 符合正则规则，则返回结果，如果不符合返回None
# 并且是一次匹配

import re

base_str = 'HZhaha1234567'

#pattern:是你构建的正则表达式对象，可以是个字符串
#string:你要匹配的字符串对象
#[A-Z]表示可以匹配　Ａ-Z 之间的任意大写字母
ret = re.match('[A-Z]',base_str)
print(type(ret))
#<class '_sre.SRE_Match'>　有一个group()
#方法返回结果
if ret:
    print(ret.group())
else:
    print('没有匹配到结果')

1.总结
１.从头开始匹配
２．只匹配一次
３．匹配到结果后立即返回，并且可以使用ｇｒｏｕｐ方法获取匹配结果
４．如果没有匹配到结果返回Ｎｏｎｅ

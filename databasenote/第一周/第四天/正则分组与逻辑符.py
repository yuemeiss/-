# ｜	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \num	引用分组num匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串

import re
sub_str = '2295808193@qq.com'
# sub_str１ = '2295808193@163.com'

# ｜匹配左右任意一个表达式
# ret = re.match('\d+@qq.com|\d+@163.com',sub_str1)


# (ab)	将括号中字符作为一个分组
ret = re.match('\d+@(qq|163).com',sub_str)

html_str = '<html><header>sbckd</header></html>'

# \w 范围：a-z A-Z 0-9 _
# 匹配上面字符串中的首、尾html值
ret = re.match('<(\w+)>.*><.(\w+)>',html_str)

print(ret.group())
print(ret.group(1),ret.group(2))
print(ret.groups())

# 匹配出img标签里面的id和链接
img_html = '<img id="onboarding-overlay-button-watermark-icon" role="presentation" src="resource://onboarding/img/watermark.svg">'
ret = re.match('<img\sid="(.*?)".*src="(.*?)">',img_html)
print(ret.groups())


# \num	引用分组num匹配到的字符串
# html_str = '<html><header>sbckd</header></html>'
# html_str = '<html>sbckd</html>'
# # \w a-z A-Z 0-9 _
# ret = re.match('<(\w+)>.*\\1>',html_str)
# # ret = re.match('<(\w+)>.*html>',html_str)
# print(ret.group(1))
# print(ret.groups())

# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串
html_str = '<html><header>sbckd</header></html>'
# \w a-z A-Z 0-9 _
ret = re.match('<(?P<htmlTag>\w+)><(?P<headerTag>\w+)>.*(?P=headerTag)>.*(?P=htmlTag)>',html_str)
# ret = re.match('<(\w+)>.*html>',html_str)
print(ret.group(1))
print(ret.groups())


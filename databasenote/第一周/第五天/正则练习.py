import re
### 1.手机号
phone_list = [
    '18086457360','17086453680',
    '18810197863','18810197962',
    '18810150385','16619999505',
    '1661999950','14619999505',
    ]

for i in phone_list:
    pattern = re.compile(r'^1[375869][0-9]{9}')
    ret = re.match(pattern,i)
    if ret:
        print(ret.group(),i+'合法')
    else:
        print(ret,i+'不合法')

### 2邮箱
emails = [
    "xiasd@163.com",'sdlfkj@.com',
    'sdflkj@sina.com','solodfdsf@123.cm',
    'sdlfjxiaori@qq.com','saldkfj＠sina.cn',
    'oisdfo@.sodf.com.com'
    ]

for i in emails:
    # ret = re.match('[a-z0-9]+@(sina|qq|163|123)\.(com|cn)',i)
    ret = re.match(r'\w+@\w+\.(com|cn)',i)
    if ret:
        print(ret.group(),i+'合法')
    else:
        print(ret,i+'不合法')

#https://blog.csdn.net/baidu_39416074/article/details/80927445

## 3.身份证号
# area = {"11": "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古", "21": "辽宁", "22": "吉林", "23": "黑龙江", "31": "上海",
#             "32": "江苏", "33": "浙江", "34": "安徽", "35": "福建", "36": "江西", "37": "山东", "41": "河南", "42": "湖北", "43": "湖南",
#             "44": "广东", "45": "广西", "46": "海南", "50": "重庆", "51": "四川", "52": "贵州", "53": "云南", "54": "西藏", "61": "陕西",
#             "62": "甘肃", "63": "青海", "64": "宁夏", "65": "新疆", "71": "台湾", "81": "香港", "82": "澳门", "91": "国外"}

if (len(idcard) == 15):
    # erg = re.compile(
    #     '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$'
    #     )  # //测试出生日期的合法性
  # 18位身份号码检测
14 2325 1998|2000 11 24 691 8(X｜x)
elif (len(idcard) == 18):
    ereg = re.compile(
        '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])[0-9]{3}[0-9Xx]$'
        )  # //合法性正则表达式


## 5,判断大小写
cis = ['ABCDxadf','abccdkcc','1257cjnkdjckd','nscdckdjckd']
small_ci = []
for ci in cis:
    ret = re.match(r'^[a-z]+$',ci)
    if ret:
        print('字符串全是小写字母')
        small_ci.append(ret.group())
    else:
        print('字符串不全是小写')

print(small_ci)


## 6.匹配一行文字中的所有开头的数字内容

s="i love you not because 12sd 34er 56df e4 54434"

ret = re.findall(r'\b\d',s)
print(ret)

#另一种方式，取数字字符串，然后在获取第一位


# 7.提取每行中完整的年月日和时间字段
s="""se234 1987-02-09 07:30:00
1987-02-10 07:25:00"""

pattern = re.compile(r'[1-2]\d[0-9]{2}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}')
ret = re.findall(pattern,s)
print(ret)


# ８、使用正则提取出字符串中的单词
s="""i love you not because of who 234 you are, 234 but 3234ser because of who i am when i am with you"""
ret = re.findall(r'\s*?[a-zA-Z]+\s*?',s)
print(ret)
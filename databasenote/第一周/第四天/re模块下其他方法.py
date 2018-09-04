# 1.match:
# 2.search:从头开始匹配，单次匹配，会在整个字符串中
# 找目标，一旦匹配到立即返回，如果整个字符串中都没有，返回None
# 3.findall:会根据你写的正则表达式，在字符串中匹配结果，会返回所有查找到的结果，返回的结果是一个列表。
# 4.sub:先根据正则表达式查找到要匹配的字符串，然后使用一个新的字符串，去替换查找到的字符串。
# 5.split:会根据你正则表达式里面的符号做字符串的分割，返回的是一个列表
# 6.finditer:跟ｆｉｎｄall很像，不过返回的结果是一个可迭代对象。
import re

## search:
sub_str = 'ljh123456@163.com'

ret = re.search('\d+',sub_str)
print(type(ret))
if ret:
    print(ret.group())

### findall
# sub_str = 'ljh123456@163.com'

# ret = re.findall('\d+',sub_str)
# #结果['123456', '163']
# print(ret)　

### sub
sub_str = 'ljh123456@163.com'
def substr():
    return '1234@'

ret = re.sub('\d+','sub',sub_str)
print(ret)
ret1 = re.sub('sub@',substr(),ret)
print(ret1)

### split
# sub_str = 'ljh123456@163.com: 3 nssvncd!!nssvncd!smvlkds?mcdo'
# ret = re.split('@|\.|:|!|\?|\s|2|1',sub_str)
# print(ret)

# finditer
# sub_str = 'ljh123456@163.com'

# ret = re.finditer('\d+',sub_str)
# print(type(ret)) #<class 'callable_iterator'>
# for i in ret:
#     print(type(i)) #<class '_sre.SRE_Match'>
#     print(i.group())

### compile
pattern = re.compile('\d.+',re.I)
pattern = re.compile('\d.+',re.S)
# 修饰符号 描述 
# re.I 使用匹配对大小写不敏感（不区分大小写） 
# re.S 使.匹配包括换行符在内的所有字符 
# re.M 多行匹配 
# re.L 做本地化识别
ret = re.finditer(pattern,sub_str)
print(type(ret)) #<class 'callable_iterator'>
for i in ret:
    print(type(i)) #<class '_sre.SRE_Match'>
    print(i.group())










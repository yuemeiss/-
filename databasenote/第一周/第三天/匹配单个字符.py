import re

# 下面这个正则不能够匹配到数字4，因此ret为None
# ret = re.match("[0-35-9]Hello Python","7Hello Python")
# print(ret)

# ret = re.match("\D","嫦娥1号发射成功") 
# print(ret.group())

# ret = re.match("\D娥\d\s\D","嫦娥1　号发射成功") 
# print(ret.group())

ret = re.match("\S娥\d\s\D","嫦娥1　号发射成功") 
print(ret.group())
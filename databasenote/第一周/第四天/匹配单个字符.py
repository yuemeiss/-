# .	匹配任意1个字符（除了\n）
# [ ]	匹配[ ]中列举的字符
# \d	匹配数字，即0-9
# \D	匹配非数字，即不是数字
# \s	匹配空白，即 空格，tab键
# \S	匹配非空白
# \w	匹配单词字符，即a-z、A-Z、0-9、_
# \W	匹配非单词字符

import re

#match 
# .匹配任意1个字符（除了\n）
sub_str = '\n'
sub_str = 'a'
ret = re.match('.',sub_str)

# [ ]	匹配[ ]中列举的字符
sub_str = '0-0'
# ret = re.match('[a]',sub_str)
ret = re.match('[a-zA-Z0-9]',sub_str)

# \d	匹配数字，即0-9 =>[0-9]
ret = re.match('\d',sub_str)

# \D	匹配非数字，即不是数字
sub_str = 'abd'
ret = re.match('\D',sub_str)

# \s	匹配空白，即 空格，tab键(空格　\t\r\n\f\v)
sub_str = 'abd'
ret = re.match('\s',sub_str)

# \w	匹配单词字符，即a-z、A-Z、0-9、_
ret = re.match('\w',sub_str)

# \W	匹配非单词字符(* > <.....)
sub_str = '>abd'
ret = re.match('\W',sub_str)
print(ret.group())












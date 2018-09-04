# ^:匹配开头
# $:匹配结尾
# \A:匹配开头
# \Z:匹配结尾

import re
# ^|\A:匹配开头
sub_str = 'ljhyigehaoren@qq.com'
ret = re.match('^l.*@.{2,8}\.com',sub_str)
ret = re.match('\Al.*@.{2,8}\.com',sub_str)
print(ret.group())

# $|\Z:匹配结尾
sub_str = 'ljhyigehaoren@qq.com'
ret = re.match('.*@.{2,8}\.com$',sub_str)
ret = re.match('.*@.{2,8}\.com\Z',sub_str)
print(ret.group())




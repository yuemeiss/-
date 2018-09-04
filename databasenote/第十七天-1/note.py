Redis：数据库
非关系型数据库，是一个基于key-values的存储
数据存储在缓存中，读取效率高
安装：方法二的安装
1.启动，进入到redis的文件夹下
执行：redis-server redis.conf

关于Redis的字符串操作
set field(键)　values(值)
get field(键)

#设置过期时间
setex(expire) key seconds(秒数)　value

#替换子字符串
setrange key offset(偏移量，从哪个位置开始替换) newvalue

#判断key是否存在，存在则不创建，不存在则创建
setnx key value

#设置多个键值
mset key value [....]

#获取多个值
mget key key ....

#追加
append key '要追加的值'

#删除
del key
#删除多个
del key　key ...

#查看字符串的长度
strlen key

#有计算的操作，但是必须是针对于数字

#关于key的操作

keys *

keys *b*

expire key seconds 

ttl key

randomkey

type key

rename key newkey

del key

hash 类型
hinfo - >
{
    name:'xcc',
    age:26
}

hset key field value

hget key field

hmset key  field value field value .....

hmget key field field ....

hdel key field field ....

hkeys key

hvals key

hgetall key

hlen key

#给hash数据类型中的域的数字值增加指定的值(处理的是数字类型)
hincrby key field 值　
hincrby key age 10

#判断键下是否存在某个域
hexists key field

#查看域对应的字符串的长度
hstrlen key field

list 数据类型

#从左边开始存，先存的在后面
lpush key value value ......

#从右开始存，先存的在前面
rpush key value value ....

#查看数据
lrange key strat(起始位置,从0开始) end（结束位置,-1）

#重新赋值（根据索引）
lset key index value 

#指定位置插入值
linsert key before|after value(给定一个值作为参照位置) newvalue

#取值(从左边开始取值，取到就删除)
lpop key 

#(从右边开始取值，取到就删除)
rpop key

#查看队列的长度
llen key

# 根据索引查找
lindex key index

#截取
1 2 3 4 5 6 7
ltrim key start stop

ltrim key 2 5 --> 5 4 3 2 

brpop 
blpop
brpoplpush
.....









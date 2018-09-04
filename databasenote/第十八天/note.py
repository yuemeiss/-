
# redis:key-value(键值存贮)

# 启动：
# redis-cli --raw(要显示中文加--raw)

# redis数据类型
# string: 二进制数据　512MB

# set key value
# get key 

# mset key value key value ....
# mget key key ....

# append key value

# setex key seconds value(可以是任意值，在有效期内，键对应的是这个value)

# setrange key offset newvalue (指定位置替换子串)


# setnx key  (判断键是否存在，存在则不创建，不存在则创建)

# ttl key  (查看过期时间)

# del key 

# del key key ....

# key 的操作命令

# keys *
# key　正则
# expire key seconds (给一个key设置过期时间)
# randomkey (随机返回一个key)
# type key (查看数据的类型)
# rename key newkey
# .....

# hash
# hset key feild value 
# hget key feild

# hmset key feild value feild value .....
# hmget key feild feild feild ....

# hkeys key
# hvals key
# hgetall key

# del key
# hdel key field

# hlen key
# ....

# list
# (从左插入，先插得在后边)
# lpush key value value value
# (从右插入，先插得在前边)
# rpush key value value value

# lrange key start(起始位置) end(结束位置)

# lpop key (从左边取出,取出后即删除)
# rpop key (从右边取出，取出后即删除)

# brpop key key1 seconds (
#     阻塞时间,为0则一直阻塞，知道key对应的list有值，
#     不为0,在设置的时间内，即使娶不到值，也结束)
# brpoplpush key key2 timeout (从key右边中取出值,从左边放入key2中)

# lindex key index  根据索引取值

# lset key index newvalue

# linsert key before|after 参照值　newvalue

# ltrim key start(从该位置开始截取) stop（到该位置截止）

# .....


# data = {1,2,3,4,5,6,6,6,7,7}
# print(data) #-> {1,2,3,4,5,6,7}

# print({i for i in {i for i in data if i > 2} if i > 5})

# data = (1,2,3,4,5,65,78)
# data1 = (i for i in data)
# print(type(data1))

#set　集合
sadd key member member ....

smembers key

srem key member ...

scard key 

sdiff key key1 .... key(1 2 3 4 5) key1(2 3 4 5 6) result -> (1)

sinter key key1 ... key(1 2 3 4 5) key1(2 3 4 5 6) result -> (2 3 4 5)

sunion key key1 .. key(1 2 3 4 5) key1(2 3 4 5 6) result -> (1 2 3 4 5 6)

sdiffstore skey3 key key1 .... key(1 2 3 4 5) key1(2 3 4 5 6) result -> skey3:(1)

sinterstore skey3 key key1 ... key(1 2 3 4 5) key1(2 3 4 5 6) result -> skey3:(2 3 4 5)

sunionstore skey3 key key1 .. key(1 2 3 4 5) key1(2 3 4 5 6) result -> skey3:(1 2 3 4 5 6)

spop key (取出值,并且删除值)

srandmember key count(随机获取的数量)


zset 总结：

#添加有序集合的成员
zadd key score(分数|权重) value score(分数|权重) value ....

#根据索引查看指定范围的成员
zrange key start(0开始) stop(结束位置-1表示最后一个)

#删除指定的成员
zrem key member 

#删除多个指定的成员
zrem key member ...

#根据指定索引的范围删除成员
zremrangebyrank key start stop
zremrangebyrank key 0 3
1 2 3 4 54 6 7 8 89 -> 54 6 7 8 89
 

#根据权重（分数）的范围来删除指定成员
zremrangebyscore key min max
zremrangebyscore key 2 7
值：  1 2 3 4 54 6 7 8 89 -> 1 8 89
权重：1 2 3 4 5  6 7 8  9

#查看某个成员的权重
zscore key member

#返回成员在有序集合中的位置（索引值）
zrank key member 

#返回有序集合中成员的数量
zcard key 

#给有序集合中的成员增加权重，改变位置
zincrby key 10(权重增量) member

#统计有序集合中指定权重(分数)范围内的成员数量
zcount key min max 

使用zrevrange命令
1 one
2 two
3 three
4 four　
zrevrange key member 执行这个命令
１．
4 four
3 three
2 two
1 one
2.在根据查找出member在排序后的索引

#数据的类型告一段落（zinterscore）????

redis的发布与订阅
订阅一个频道
subscribe channel(频道名称) ...

发布消息：
publish channel(频道) message(消息)

取消订阅
unsubscribe channel(频道名称)

#总结一下：
事务的特性都存在
multi :开启一个事务
exec : 提交一个事务
discard : 取消事物
watch : 监听
unwatch : 取消监听


备份：
save 使用这个命令之后，会保存一个dump.rdb 

#主从备份
１．配置要有一个主节点　
　　　进入redis.conf 修改bind 为主机ip
     保存退出，重新开启redis服务
     启动redis-cli -h 主节点的ip -p 主节点的port 连接主节点（redis服务）

２．配置从节点
     进入redis.conf 修改bind 为主机ip
     可以修改端口号
     设置主节点信息（２８２行）
     保存退出，重新开启redis服务
     启动redis-cli　-h 从节点的ip -p 从节点的port 连接从节点（redis服务）

可以实现主从备份


安全：
查看密码
config get requirepass

设置
congig set requirepass　‘密码’

认证
auth 密码

取消密码：
congig set requirepass ''






　








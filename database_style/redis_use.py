#redis与python的交互
#sudo　pip3 install redis

import redis
import time

#创建连接
# host='localhost', ip
# port=6379, 端口
# db=0, 指定数据库
# password=None,　密码
redis_conn = redis.StrictRedis(host='localhost',port=6379,db=2)
#redis_conn = redis.Redis(host='localhost',port=6379)

#字符串的操作：
#string
# set 、setex、mset、append、get、mget、
def do_string():
    #存
    redis_conn.set('class1804',28)
    #存多个数据
    # redis_conn.mset({'1804':27,'1806':17})
    #取
    # result = redis_conn.get('class1804')
    #取多个值
    # result = redis_conn.mget(['1804','1806'])
    # print(result)
    # print(result.decode('utf8'))
    #设置过期时间
    # result = redis_conn.setex('1804',30,'new')
    # print(result)
    #拼接
    # result = redis_conn.append('1806','new')
    # print(result)
    #查看长度
    # result = redis_conn.strlen('1806')
    # print(result)
    #删除key,返回结果0或则是１
    # result = redis_conn.delete('1806')
    # print(result)



#　key
# keys、exists、type、delete、expire　、getrange、ttl
def do_key():
    #pattern='*'
    #获取数据库中(符合条件)的键
    # keys = redis_conn.keys('*z')
    # print(keys)
    #判断某个键是否存在
    # result = redis_conn.exists('zzz1')
    # print(result)
    #判断键的值的类型
    # result = redis_conn.type('zzz')
    # print(result)
    #设置过期时间
    # result = redis_conn.expire('zzz',30)
    # print(result)
    #查看存活时间
    # result = redis_conn.ttl('zzz')
    # print(result)
    #返回指定范围的值
    # result = redis_conn.getrange('class1804',0,10)
    # print(result)
    pass



#　hash
# hset、hmset、hkeys、hget、hmget、hvals、hdel

#　list
# lpush、rpush、linsert、lrange、lset、lrem


#set
# sadd、smembers、srem

#zset
# zadd、zrange、zrangebyscore、zscore
# 、zrem、zremrangebyscore

def do_pipeline():
    #返回一个管道对象
    pipe = redis_conn.pipeline()
    #开启事务
    pipe.multi()
    #存值
    pipe.set('age',10)
    pipe.lpush('list',(1,2,3,4,5,6,7,8))
    pipe.hset('students','name','xxx')
    time.sleep(30)
    #提交
    pipe.execute()

### 订阅发布
def do_subscribe():
    # Return a Publish/Subscribe object. With this object, you can
    # subscribe to channels and listen for messages that get published to
    # them.
#     返回一个发布/订阅对象。这个对象,你可以
# 　　订阅发布通道和侦听消息他们。
    pubsub = redis_conn.pubsub()
    #订阅频道
    pubsub.subscribe('1804')
    
    print(pubsub.parse_response())
    #返回的消息类型如下[b'subscribe', b'1804', 1]，表示订阅成功

    print('等待消息')

    while True:
        #监听频道发布的消息
        print(pubsub.parse_response())


# 发布端
def do_publish():
    #发布频道消息
    redis_conn.publish('1804','这个好难理解啊')

if __name__ == '__main__':
    # do_string()
    #do_key()
    #do_pipeline()
    # do_subscribe()
    #do_publish()
    

    
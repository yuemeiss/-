import redis,time

#创建连接
redisConn = redis.StrictRedis('localhost',6379,2)
# redisConn = redis.Redis()


#字符串的操作
def do_string():
    #存
    #redisConn.set('class1804',23)
    #redisConn.mset({'1804':17,'1806':24})
    #取
    # result = redisConn.get('class1804')
    #取多个值　返回一个列表
    #result = redisConn.mget('1804','1806')
    # print(result.decode('utf8'))
    #设置过期时间
    #result = redisConn.setex('1804',30,'new')
    #拼接
    # result = redisConn.append('1806','new')
    # 查看长度
    # result = redisConn.strlen('1806')
    #删除
    # result = redisConn.delete('1806')
    # print(result)
    pass



def do_key():
    #获取数据库中(符合条件)的键
    #keys = redisConn.keys()
    #print(keys)
    #判断键值的类型
    #result = redisConn.type('zzz')
    #print(result)
    #返回指定范围的值
    #判断keys存在
    result = redisConn.exists('zzz')
    #查看数据类型
    result = redisConn.type('1806')
    #设置键的过期时间
    result = redisConn.expire('1806',30)
    #查看有效时间
    result = redisConn.ttl('1806')
def do_hash():
    #添加
    result = redisConn.hset('xxx','nna',123)
    #添加多个
    # result = redisConn.hmset('fxd','sdfsdf',123,'wer','adf')
    #查看所有语
def do_pipeline():
    pipe = redisConn.pipeline()
    #开启事务
    pipe.multi()
    pipe.set('age',10)
    pipe.lpush('list',(22,34))
    pipe.hset('setswe','wer',110)
    pipe.sadd('sdf',{234,23423,34})
    time.sleep(30)
    #提交
    pipe.execute()
#定义订阅发布
def do_subscribe():
    pubsub = redisConn.pubsub()
    #订阅频道
    pubsub.subscribe('1804')
    #返回的消息类型如下[b'subscribe', b'1804', 1] , 表示订阅成功 1：表示订阅频道的数量
    print('等带消息')
    while True:
        #监听 频道发布的消息
        print(pubsub.parse_response())
#发布端
def do_publish():
    #发布频道消息
    redisConn.publish('1804','你能看懂英语')

if __name__ == '__main__':
    # do_string()
    # do_key()
    # do_pipeline()
    # do_subscribe()
    # do_publish()
    pass

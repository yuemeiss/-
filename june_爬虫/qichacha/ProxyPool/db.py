"""
存储模块:使用Redis的有序集合,用来做代理的去重和状态标识,同时也是中心模块和基础模块,将其他模块串联起来
"""
import redis,re
from error import PoolEmptyError
from setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY
from setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from random import choice
# # Redis数据库地址
# REDIS_HOST = '127.0.0.1'
#
# # Redis端口
# REDIS_PORT = 6379
#
# # Redis密码，如无填None
# REDIS_PASSWORD = None
#
# REDIS_KEY = 'proxies'
#
# # 代理分数
# # 状态 100 是最佳 越低越差
# MAX_SCORE = 100
# MIN_SCORE = 0
# INITIAL_SCORE = 10
class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis IP地址
        :param prot:  Redis 端口
        :param password: Redis密码
        """
        # decode_responses = True  这样从数据库取出就不用解码了,默认False 取出 的是二进制数据
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """
        if not re.match('\d+\.\d+\.\d+\.\d+:\d+', proxy):
            print('代理不符合规范', proxy, '丢弃')
            return
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score, proxy)

    def random_proxy(self):
        """
        随机获取有效代理,首先尝试获取最高分数的代理,如果最高分数不存在,则按照排名获取,否则异常
        :return:  随机代理
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

    def decrease(self, proxy):
        """
        decrease /dɪ'kriːs/ : 减少
        代理值减一分,分数小于最小值,则代理删除
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self,proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        return not self.db.zscore(REDIS_KEY,proxy) == None
    def max(self,proxy):
        """
        将代理设置为 MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """
        print('代理',proxy,'可用,设置为',MAX_SCORE)

        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)
    def count(self):
        """
        获取数量
        :return:数量
        """
        return self.db.zcard(REDIS_KEY)
    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)

    def batch(self, start, stop):
        """
        批量获取
        :param start: 开始索引
        :param stop: 结束索引
        :return: 代理列表
        """
        return self.db.zrevrange(REDIS_KEY, start, stop - 1)




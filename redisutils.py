# -*- coding: utf-8 -*-
# @Time : 2022/4/7 17:10
# @Author : O·N·E
# @File : redisutils.py
import redis


# 普通连接方式
class RedisClient:
    def __init__(self, host, password, port, db):
        """
        :param host:ip地址
        :param password:redis密码
        :param port:端口号 默认为6379
        :param db:数据库库名
        :param decode_responses:redis取出的结果默认是字节,设定 decode_responses=True 改成字符串。
        """
        # 实例化redis
        self.redis_client = redis.StrictRedis(
            host=host,
            password=password,
            port=port,
            db=db,
            decode_responses=True
        )


# 连接池连接
class RedisClientPool:
    def __init__(self, host, password, port, db):
        self.redisclientpool = redis.ConnectionPool(
            host=host,
            password=password,
            port=port,
            db=db,
            decode_responses=True
        )
        self.redisclientpoolconn = redis.Redis(connection_pool=self.redisclientpool)

# -*- coding: utf-8 -*-
# @Time : 2022/4/11 11:33
# @Author : O·N·E
# @File : 05.zset.py
from redisutils import RedisClientPool


class RedisClientPoolset(RedisClientPool):
    # zset:有序集合，在集合的基础上，为每元素排序；元素的排序需要根据另外一个值来进行比较.
    # 所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。
    def redis_zadd(self, name, *args, **kwargs):
        """
        :param args:值
        :param kwargs:分数
        :return:在name对应的有序集合中添加元素
        """
        return self.redisclientpoolconn.zadd(name, *args, **kwargs)

    def redis_zcard(self, name):
        """
        :return:获取name对应的有序集合元素的数量
        """
        return self.redisclientpoolconn.zcard(name)

    def redis_zrange(self, name, start, end, desc=False, withscores=False, score_cast_func=float):
        """
        :param start:有序集合索引起始位置（非分数）
        :param end:有序集合索引结束位置（非分数）
        :param desc: 排序规则，默认按照分数从小到大排序
        :param withscores:是否获取元素的分数，默认只获取元素的值
        :param score_cast_func:对分数进行数据转换的函数
        :return:按照索引范围获取name对应的有序集合的元素
        """
        return self.redisclientpoolconn.zrange(name, start, end, desc, withscores, score_cast_func)

    def redis_zrangebyscore(self, name, min, max, start=None, num=None, withscores=False, score_cast_func=float):
        """
        :param min: 最小值
        :param max: 最大值
        :param start:有序集合索引起始位置（非分数）
        :return:按照分数范围获取name对应的有序集合的元素(默认情况下是降序)
        """
        return self.redisclientpoolconn.zrangebyscore(name, min, max, start, num, withscores, score_cast_func)

    def redis_zscan(self, name, cursor=0, match=None, count=None, score_cast_func=float):
        """
        :return:获取所有元素–默认按照分数顺序排序
        """
        return self.redisclientpoolconn.zscan(name, cursor, match, count, score_cast_func)

    def redis_zscan_iter(self, name, match=None, count=None, score_cast_func=float):
        """
        :return:获取所有元素–迭代器
        """
        return self.redisclientpoolconn.zscan_iter(name, match, count, score_cast_func)

    def redis_zrem(self, name, values):
        """
        :param values:
        :return:删除name对应的有序集合中值是values的成员
        """
        return self.redisclientpoolconn.zrem(name, values)

    def redis_zremrangebyscore(self, name, min, max):
        """
        :return:根据排行范围删除，按照索引号来删除
        """
        return self.redisclientpoolconn.zremrangebyscore(name, min, max)


if __name__ == '__main__':
    redisclientpoolset = RedisClientPoolset(host="121.40.18.239", password=123456, port=6379, db=1)
    """zset操作"""
    """zadd"""
    # print(redisclientpoolset.redis_zadd("zset1", {'m1': 22, 'm2': 44, 'm3': 30, 'm4': 10, 'm5': 55}))
    """zcard"""
    # print(redisclientpoolset.redis_zcard("zset_text"))
    """zrange"""
    # print(redisclientpoolset.redis_zrange("zset_text",0,1,desc=True))
    """zrevrangebyscore"""
    # print(redisclientpoolset.redis_zrangebyscore("zset1", 10, 30))
    """zscan"""
    # print(redisclientpoolset.redis_zscan("zset1"))
    """zscan_iter"""
    # for i in redisclientpoolset.redis_zscan_iter("zset1"):
    #     print(i)
    """zrem"""
    # print(redisclientpoolset.redis_zrem("zset_text", "t1"))
    """zrevrangebyscore"""
    print(redisclientpoolset.redis_zremrangebyscore("zset1", 50, 60))

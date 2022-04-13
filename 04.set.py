# -*- coding: utf-8 -*-
# @Time : 2022/4/11 11:14
# @Author : O·N·E
# @File : 04.set.py
from redisutils import RedisClientPool


class RedisClientPoolset(RedisClientPool):
    # set操作:Set集合就是不允许重复的列表，本身是无序的。
    def redis_sadd(self, name, *values):
        """
        :param values:
        :return:添加元素到集合中,若插入已有元素，则不自动插入
        """
        return self.redisclientpoolconn.sadd(name, *values)

    def redis_scard(self, name):
        """
        :return: 获取name对应的集合中元素个数
        """
        return self.redisclientpoolconn.scard(name)

    def redis_smembers(self, name):
        """
        :return:获取集合中的所有元素
        """
        return self.redisclientpoolconn.smembers(name)

    def redis_sdiff(self, name, *others_name):
        """
        :param name: 指定的集合名字
        :param others_name: 指定的集合
        :return:差集sdiff(keys, *args)在第一个name对应的集合中且不在其他name对应的集合的元素集合
        """
        return self.redisclientpoolconn.sdiff(name, *others_name)

    def redis_sinter(self, name, *others_name):
        """
        :return:sinter(keys, *args) 获取多个name对应集合的并集
        """
        return self.redisclientpoolconn.sinter(name, *others_name)

    def redis_smove(self, src, dst, value):
        """
        :param src:初始集合
        :param dst:目标集合
        :return: smove(src, dst, value) 将某个元素从一个集合中移动到另外一个集合
        """
        return self.redisclientpoolconn.smove(src, dst, value)

    def redis_sunion(self, *args):
        """
        :param args:集合名称
        :return:Set sunion 返回一个集合与其他集合的并集
        """
        return self.redisclientpoolconn.sunion(*args)

    def redis_srem(self, name, value):
        """
        :return:删除指定值
        """
        return self.redisclientpoolconn.srem(name, value)


if __name__ == '__main__':
    redisclientpoolset = RedisClientPoolset(host="121.40.18.239", password=123456, port=6379, db=1)
    """set操作"""
    """sadd"""
    # print(redisclientpoolset.redis_sadd("set_text", "a", "b", "c", "one", "two", "a"))
    """scard"""
    # print(redisclientpoolset.redis_scard("set_text"))
    """smembers"""
    # print(redisclientpoolset.redis_smembers("set_text"))
    """sdiff"""
    # print(redisclientpoolset.redis_sdiff("set_text", "set_text2"))
    """sinter"""
    # print(redisclientpoolset.redis_sinter("set_text", "set_text2"))
    """smove"""
    # print(redisclientpoolset.redis_smove("set_text", "set_text2", "one"))
    """sunion"""
    # print(redisclientpoolset.redis_sunion("set_text", "set_text2"))
    """srem"""
    # print(redisclientpoolset.redis_srem("set_text", "one"))

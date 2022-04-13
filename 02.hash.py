# -*- coding: utf-8 -*-
# @Time : 2022/4/7 16:14
# @Author : O·N·E
# @File : 02.hash.py

from redisutils import RedisClientPool


class RedisClientPoolhash(RedisClientPool):
    # hash操作:redis中的Hash 在内存中类似于一个name对应一个dic来存储
    def hset(self, name, key, value):
        """
        :return: hset name对应的hash中设置一个键值对（不存在，则创建，否则，修改）
        """
        return self.redisclientpoolconn.hset(name, key, value)

    def hmset(self, name, hmset_mappings):
        """
        :return:批量设置键值对
        """
        return self.redisclientpoolconn.hmset(name, hmset_mappings)

    def hmget(self, name, key_list):
        """
        :return:在对应的hash中获取多个key的值
        """
        return self.redisclientpoolconn.hmget(name, key_list)

    def hgetall(self, name):
        """
        :return: 获取name对应hash的所有键值
        """
        return self.redisclientpoolconn.hgetall(name)

    def hkeys(self, name):
        """
        :return:获取name对应的hash中所有的key的值
        """
        return self.redisclientpoolconn.hkeys(name)

    def hvals(self, name):
        """
        :return:获取name所有的value的值
        """
        return self.redisclientpoolconn.hvals(name)

    def hdel(self, name, keys):
        """
        :return:key删除
        """
        return self.redisclientpoolconn.hdel(name, keys)

    def hincrbyfloat(self, name, key, amount):
        """
        :return:将key做加法， 加上amount(浮点数,整数都可以)
        """
        return self.redisclientpoolconn.hincrbyfloat(name, key, amount)

    def redisscan(self, course=0, match=None, count=None):
        """
         scan命令采用基于游标的迭代器。
        每次调用 scan 命令，Redis 都会向用户返回一个新的游标以及一定数量的 key。下次再想继续获取剩余的 key，需要将这个游标传入 scan 命令， 以此来延续之前的迭代过程。
        简单来讲，scan 命令使用分页查询 redis。
        虽然 scan 命令时间复杂度与 keys一样，都是 O(N)，但是由于 scan 命令只需要返回少量的 key，所以执行速度会很快。
        :param name:redis的name
        :param course:游标（基于游标分批取获取数据）
        :param match:匹配指定key，默认None 表示所有的key
        :param count:每次分片最少获取个数，默认None表示采用Redis的默认分片个数
        :return:tuple类型:(扫描位置，所有dict数据)
        """
        return self.redisclientpoolconn.scan(course, match, count)

    def redishscan_iter(self, name, match=None, count=None):
        """
        :return:利用yield封装hscan创建生成器，实现分批去redis中获取数据
        """
        return self.redisclientpoolconn.hscan_iter(name, match, count)


if __name__ == '__main__':
    redisclientpoolhash = RedisClientPoolhash(host="121.40.18.239", password=123456, port=6379, db=0)
    """hash操作"""
    """hset"""
    # print(redisclientpoolhash.hset("one", "k8", 8))
    # hmset_mappings = {"k1": 1, "k2": 2}
    # print(redisclientpoolhash.hmset("two", hmset_mappings))
    """hmget"""
    # key_list = ["k1", "k2"]
    # print(redisclientpoolhash.hmget("two", key_list))
    """hgetall"""
    # print(redisclientpoolhash.hgetall("two"))
    """hkeys"""
    # print(redisclientpoolhash.hkeys("two"))
    """hvals"""
    # print(redisclientpoolhash.hvals("two"))
    """hdel"""
    # print(redisclientpoolhash.hdel("two", "k2"))
    """hincrbyfloat"""
    # print(redisclientpoolhash.hincrbyfloat("two", "k1", amount=0.1))
    """scan"""
    # print(redisclientpoolhash.redisscan(course=0,match="k1?", count=3))
    """hscan_iter"""
    for i in redisclientpoolhash.redishscan_iter("two", match="k?", count=3):
        print(i)

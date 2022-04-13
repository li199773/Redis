# -*- coding: utf-8 -*-
# @Time : 2022/4/7 17:34
# @Author : O·N·E
# @File : 01.string.py
from redisutils import RedisClientPool


class RedisClientPoolstring(RedisClientPool):
    def set(self, key, value, ex=None, px=None, nx=False):
        """
        :param key:键
        :param values:值
        :param ex:过期时间（秒）
        :param px:过期时间（毫秒）
        :param nx:如果设置为True，则只有name不存在时，当前set操作才执行
        :return:
        """
        return self.redisclientpoolconn.set(key, value, ex, px, nx)

    def setnx(self, key, value):
        """
        :return:设置值，只有name不存在时，执行设置操作（添加）
        """
        return self.redisclientpoolconn.setnx(key, value)

    def setex(self, key, value, time):
        """
        :return:设置值，time - 过期时间（数字秒 或 timedelta对象）
        """
        return self.redisclientpoolconn.setex(key, value, time)

    def mset(self, dicts):
        """
        :return: 批量设置值
        """
        return self.redisclientpoolconn.mset(dicts)

    def get(self, key):
        """
        :return:获取值
        """
        return self.redisclientpoolconn.get(key)

    def mget(self, mget_list):
        """
        :return:批量获取值
        """
        return self.redisclientpoolconn.mget(mget_list)

    def getrange(self, key, start, end):
        """
        :param key:
        :param start: 开始位置
        :param end: 结束位置
        :return:
        """
        return self.redisclientpoolconn.getrange(key, start, end)

    def append(self, key, value):
        """
        :return: append在key对应的值后面追加内容
        """
        return self.redisclientpoolconn.append(key, value)

    def strlen(self, key):
        """
        :return:返回key对应值的字节长度（一个汉字3个字节）我爱中国输出为12
        """
        return self.redisclientpoolconn.strlen(key)

    def incr(self, key, amount):
        """
        :param amount:自增数(必须为整数)
        :return: 自增 key对应的值，当 key不存在时，则创建 key＝amount，否则，则自增。
        "decr":同理为自减
        """
        return self.redisclientpoolconn.incr(key, amount=amount)

    def incrbyfloat(self, key, amount):
        """
        :param amount:自增数(浮点型)
        :return: 自增 key对应的值，当 key不存在时，则创建 key＝amount，否则，则自增。
        "decr":同理为自减
        """
        return self.redisclientpoolconn.incrbyfloat(key, amount=amount)


if __name__ == '__main__':
    redisclientpoolstring = RedisClientPoolstring(host="121.40.18.239", password=123456, port=6379, db=1)
    """string操作"""
    """set"""
    # print(redisclientpoolstring.set("k3", "3", nx=True))
    # print(redisclientpoolstring.setnx("k4", 4))
    # print(redisclientpoolstring.setex("k5", 5, time=30))
    """mset"""
    # dict = {"k11": 11, "k22": 22}
    # print(redisclientpoolstring.mset(dict))
    """get"""
    # print(redisclientpoolstring.get("k1"))
    # mget_list = ["k11", "k22"]
    # print(redisclientpoolstring.mget(mget_list))
    """getrange"""
    # print(redisclientpoolstring.getrange("k6", 0, 1))
    """append"""
    # print(redisclientpoolstring.append("k6", "one"))
    """strlen"""
    # print(redisclientpoolstring.strlen("hanzi"))
    """incr"""
    # print(redisclientpoolstring.incr("k7", amount=2))
    # print(redisclientpoolstring.incrbyfloat("k7", amount=0.01))

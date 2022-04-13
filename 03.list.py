# -*- coding: utf-8 -*-
# @Time : 2022/4/11 10:31
# @Author : O·N·E
# @File : 03.list.py
from redisutils import RedisClientPool


class RedisClientPoollist(RedisClientPool):
    # list操作:redis中的List在在内存中按照一个name对应一个List来存储。
    def redis_lpush(self, name, *values):
        """
        :return: 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
        """
        return self.redisclientpoolconn.lpush(name, *values)

    def redis_rpush(self, name, *values):
        """
        :return: 在name对应的list中添加元素，每个新的元素都添加到列表的最右边
        """
        return self.redisclientpoolconn.rpush(name, *values)

    """
    往已经有的name的列表中添加元素，没有的话无法创建
        lpushx(name, value)：往name列表的左边添加元素
        rpushx(name, value)：往name列表的右边添加元素
    """

    def redis_linsert(self, name, where, refvalue, value):
        """
        :param name:redis的name
        :param where:BEFORE或AFTER
        :param refvalue:标杆值，即：在它前后插入数据
        :param value:要插入的数据
        :return:在name对应的列表的某一个值前或后插入一个新值
        """
        return self.redisclientpoolconn.linsert(name, where, refvalue, value)

    def redis_lset(self, name, index, value):
        """
        :param index: 索引号
        :param values: 修改的值
        :return:对应的list中的某一个索引位置重新赋值
        """
        return self.redisclientpoolconn.lset(name, index, value)

    def redis_lrem(self, name, value, num=1):
        """
        :num=1:从前到后，删除2个, num=1,从前到后，删除左边第1个
        :num=-1:从后向前，删除2个
        :return:在name对应的list中删除指定的值
        """
        return self.redisclientpoolconn.lrem(name, value, num)

    def redis_lindex(self, name, index):
        """
        :param index: 索引值
        :return: 取值
        """
        return self.redisclientpoolconn.lindex(name, index)

    def redis_ltrim(self, name, start, end):
        """
        :param start: 起始索引值
        :param end: 结束索引值
        :return:删除索引之外的值
        """
        return self.redisclientpoolconn.ltrim(name, start, end)

    def redis_rpoplpush(self, src, dst):
        """
        移动元素从一个列表移动到另外一个列表 可以设置超时brpoplpush(src, dst, timeout=0)
        :param src: 要取数据的列表的 name
        :param dst: 要添加数据的列表的 name
        :return:从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
        """
        return self.redisclientpoolconn.rpoplpush(src, dst)

    def redis_iter(self, name):
        """
        由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要增量迭代
        :return:
        """
        list_count = self.redisclientpoolconn.llen(name)
        for index in range(list_count):
            yield self.redisclientpoolconn.lindex(name, index)


if __name__ == '__main__':
    redisclientpoollist = RedisClientPoollist(host="121.40.18.239", password=123456, port=6379, db=1)
    """list操作"""
    """lpush"""
    # print(redisclientpoollist.redis_lpush("list_text", 1, 2, 3))
    """rpush"""
    # print(redisclientpoollist.redis_rpush("list_text1", 1, 2, 3))
    """linsert"""
    # print(redisclientpoollist.redis_linsert("list_text", "before", 1, 0))
    """lset"""
    # print(redisclientpoollist.redis_lset("list_text", 3, -1))
    """lrem"""
    # print(redisclientpoollist.redis_lrem("list_text", 1))
    """lindex"""
    # print(redisclientpoollist.redis_lindex("list_text", 3))
    """ltrim"""
    # print(redisclientpoollist.redis_ltrim("list_text", 0, 1))
    """rpoplpush"""
    # print(redisclientpoollist.redis_rpoplpush("list_text", "list_text1"))
    """list_iter"""
    for item in redisclientpoollist.redis_iter('list_text1'):  # 遍历这个列表
        print(item)

# -*- coding: utf-8 -*-
# @Time : 2022/4/1 16:37
# @Author : O·N·E
# @File : redis_python.py
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

    def set(self, key, values):
        print("ok")
        return self.redis_client.set(key, values)

    def get(self, key):
        return self.redis_client.get(key)


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

    # string操作
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
    redisclient = RedisClient(host="121.40.18.239", password=123456, port=6379, db=0)
    # print(redisclient.set("k1", "1"))
    # print(redisclient.get("k1"))
    """一般使用连接池，因为大部分时间都会浪费在redis连接"""
    redisclientpool = RedisClientPool(host="121.40.18.239", password=123456, port=6379, db=0)
    """string操作"""
    """set"""
    # print(redisclientpool.set("k3", "3", nx=True))
    # print(redisclientpool.setnx("k4", 4))
    # print(redisclientpool.setex("k5", 5, time=30))
    """mset"""
    # dict = {"k11": 11, "k22": 22}
    # print(redisclientpool.mset(dict))
    """get"""
    # print(redisclientpool.get("k1"))
    # mget_list = ["k11", "k22"]
    # print(redisclientpool.mget(mget_list))
    """getrange"""
    # print(redisclientpool.getrange("k6", 0, 1))
    """append"""
    # print(redisclientpool.append("k6", "one"))
    """incr"""
    # print(redisclientpool.incr("k7", amount=2))
    # print(redisclientpool.incrbyfloat("k7", amount=0.01))
    """hash操作"""
    """hset"""
    # print(redisclientpool.hset("one", "k8", 8))
    # hmset_mappings = {"k1": 1, "k2": 2}
    # print(redisclientpool.hmset("two", hmset_mappings))
    """hmget"""
    # key_list = ["k1", "k2"]
    # print(redisclientpool.hmget("two", key_list))
    """hgetall"""
    # print(redisclientpool.hgetall("two"))
    """hkeys"""
    # print(redisclientpool.hkeys("two"))
    """hvals"""
    # print(redisclientpool.hvals("two"))
    """hdel"""
    # print(redisclientpool.hdel("two", "k2"))
    """hincrbyfloat"""
    # print(redisclientpool.hincrbyfloat("two", "k1", amount=0.1))
    """scan"""
    # print(redisclientpool.redisscan(course=0,match="k1?", count=3))
    """hscan_iter"""
    # for i in redisclientpool.redishscan_iter("three", match="k1?", count=3):
    #     print(i)
    """list操作"""
    """lpush"""
    # print(redisclientpool.list_lpush("list_text", 1, 2, 3))
    """rpush"""
    # print(redisclientpool.redis_rpush("list_text1", 1, 2, 3))
    """linsert"""
    # print(redisclientpool.redis_linsert("list_text", "before", 1, 0))
    """lset"""
    # print(redisclientpool.redis_lset("list_text", 3, -1))
    """lindex"""
    # print(redisclientpool.redis_lindex("list_text", 3))
    """ltrim"""
    # print(redisclientpool.redis_ltrim("list_text", 0, 1))
    """rpoplpush"""
    # print(redisclientpool.redis_rpoplpush("list_text", "list_text1"))
    """list_iter"""
    # for item in redisclientpool.redis_iter('list_text1'):  # 遍历这个列表
    #     print(item)
    """set操作"""
    """sadd"""
    # print(redisclientpool.redis_sadd("set_text2", "a", "b", "c", "one","two"))
    """scard"""
    # print(redisclientpool.redis_scard("set_text"))
    """smembers"""
    # print(redisclientpool.redis_smembers("set_text"))
    """sdiff"""
    # print(redisclientpool.redis_sdiff("set_text", "set_text2"))
    """sinter"""
    # print(redisclientpool.redis_sinter("set_text", "set_text2"))
    """smove"""
    # print(redisclientpool.redis_smove("set_text", "set_text2", "one"))
    """sunion"""
    # print(redisclientpool.redis_sunion("set_text", "set_text2"))
    """srem"""
    # print(redisclientpool.redis_srem("set_text", "one"))
    """zset操作"""
    """zadd"""
    # print(redisclientpool.redis_zadd("zset_text", {"t1": 1, "t2": 100, "t3": 10}))
    """zcard"""
    # print(redisclientpool.redis_zcard("zset_text"))
    """zrange"""
    # print(redisclientpool.redis_zrange("zset_text",0,1,desc=True))
    """zrevrangebyscore"""
    # print(redisclientpool.redis_zrangebyscore("zset1", 10, 30))
    """zscan"""
    # print(redisclientpool.redis_zscan("zset1"))
    """zscan_iter"""
    # for i in redisclientpool.redis_zscan_iter("zset1"):
    #     print(i)
    """zrem"""
    # print(redisclientpool.redis_zrem("zset_text", "t1"))
    """zrevrangebyscore"""
    # print(redisclientpoolset.redis_zremrangebyscore("zset1", 50, 60))

# -*- coding: utf-8 -*-
# @Time : 2022/4/11 16:10
# @Author : O·N·E
# @File : 06.piplines.py
from redisutils import RedisClientPool


class RedisClientPoolpiplines(RedisClientPool):
    def redisclientpoolpiplines(self):
        """创建管道"""
        self.pipe = self.redisclientpoolconn.pipeline()
        self.pipe.mset({"k1": 1, "k2": 2})
        self.pipe.mget("k1", "k2")
        self.pipe.hmset("one", {"k1": 1, "k2": 2})
        return self.pipe.execute()


if __name__ == '__main__':
    redisclientpoolpiplines = RedisClientPoolpiplines(host="121.40.18.239", password=123456, port=6379, db=2)
    print(redisclientpoolpiplines.redisclientpoolpiplines())

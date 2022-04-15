# -*- coding: utf-8 -*-
# @Time : 2022/4/14 14:34
# @Author : O·N·E
# @File : 07 Bloom_Filter.py
import redis

client = redis.Redis(
    host="192.168.81.100",
    password=123456,
    port=6379,
    db=0,
    decode_responses=True
)

size = 1000000
count = 0
# client.execute_command("bf.reserve", "demo_1000000", 0.001, size)
for i in range(size):
    client.execute_command("bf.add", "demo_1000000", "xxx%d" % i)
    result = client.execute_command("bf.exists", "lqz", "xxx%d" % (i + 1))
    if result == 1:
        # print(i)
        count += 1
print("size: {} , error rate: {}%".format(size, round(count / size * 100, 5)))

# `Redis` python操作、主从复制、RDB、AOF、哨兵模式
****
## 1.数据库对比
Memcache
``````
很早出现的NoSql数据库
数据都在内存中，一般不持久化
支持简单的key-value模式，支持类型单一
一般是作为缓存数据库辅助持久化的数据库
``````
Redis
``````
几乎覆盖了Memcached的绝大部分功能
数据都在内存中，支持持久化，主要用作备份恢复
除了支持简单的key-value模式，还支持多种数据结构的存储，比如 list、set、hash、zset等。
一般是作为缓存数据库辅助持久化的数据库
``````
MongoDB
```
高性能、开源、模式自由(schema  free)的文档型数据库
数据都在内存中， 如果内存不足，把不常用的数据保存到硬盘
虽然是key-value模式，但是对value（尤其是json）提供了丰富的查询功能
支持二进制数据及大型对象
可以根据数据的特点替代RDBMS ，成为独立的数据库。或者配合RDBMS，存储特定的数据
```
****
## 2.`redis`五种数据类型
### `String`数据类型、`List`数据类型、`Hash`数据类型（散列类型）、`set`数据类型（无序集合）、`Sorted Set`数据类型 (zset、有序集合)。
### 详情信息见`01-07.py`文件
****
## 3.数据持久化
### 3.1 RDB机制
    RDB 是 Redis DataBase 的缩写，即内存块照。因为Redis的数据时存在内存中的，当**服务器宕机**时，Redis中存储的数据就会丢失。这个时候就需要内存快照来恢复Redis中的数据了。快照就是在某一时刻，将Redis中的所有数据，以文件的形式存储起来。
### 3.2 RDB配置
    1. SNAPSHOTTING
    2. 开启保存出错停止写入功能（默认开启）
    3. 数据压缩（默认开启）
    4. RDB文件校验（默认开启）
    5. 指定本地数据库文件名，一般采用默认的 dump.rdb
### 3.3 AOF机制
    AOF机制以日志的形式记录 Redis 的每一个写操作，将 Redis 执行过的所有写指令保存下来，以追加的形式保存到 AOF 文件 (默认为 appendonly.aof) 中当需要恢复数据时，Redis 会重新执行 AOF 文件中的写指令，来达到恢复数据的目的。
### 3.4AOF配置
    appendonly no # 是否开启aof
    appendfilename "appendonly.aof" # 文件名
    #磁盘同步策略 默认每秒一次  
    # appendfsync always  # 每次
    appendfsync everysec # 每秒一次
    # appendfsync no # 由操作系统执行，默认Linux配置最多丢失30秒
## no-appendfsync-on-rewrite

作用： 后台执行（RDB的save | aof重写）时appendfsync设为no

```
no-appendfsync-on-rewrite no
```


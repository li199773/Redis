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
## 3.数据持久化
### 3.1 RDB机制
RDB 是 Redis DataBase 的缩写，即内存块照。因为Redis的数据时存在内存中的，当**服务器宕机**时，Redis中存储的数据就会丢失。这个时候就需要内存快照来恢复Redis中的数据了。快照就是在某一时刻，将Redis中的所有数据，以文件的形式存储起来。
### 3.2 RDB配置
1. SNAPSHOTTING
   ```
   save 3600 1
   save 300 100
   save 60 10000
   save 30 2
   服务器在900秒之内，对数据库进行了至少1次修改
   服务器在300秒之内，对数据库进行了至少10次修改　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
   服务器在60秒之内，对数据库进行了至少10000次修改。
   这里配置了30秒之内，对数据库进行了至少2次修改就触发RDB。
   ```
2. 开启保存出错停止写入功能（默认开启）
   ```
   如果RDB快照持久化操作被激活（至少一个条件被激活）并且持久化操作失败，Redis则会停止接受更新操作。
   stop-writes-on-bgsave-error yes
   ```
3. 数据压缩（默认开启）
   ```
   rdbcompression yes
   ```
4. RDB文件校验（默认开启）
   ```
   会让格式更加耐攻击，但是当存储或者加载rbd文件的时候会有一个10%左右的性能下降
   rdbchecksum yes
   ```
5. 指定本地数据库文件名，一般采用默认的 dump.rdb

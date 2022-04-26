# `Redis python操作、主从复制、RDB、AOF、哨兵模式`
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
### RDB 是 Redis DataBase 的缩写，即内存块照。因为Redis的数据时存在内存中的，当**服务器宕机**时，Redis中存储的数据就会丢失。这个时候就需要内存快照来恢复Redis中的数据了。快照就是在某一时刻，将Redis中的所有数据，以文件的形式存储起来。
### 3.2 RDB配置
    1. SNAPSHOTTING
    2. 开启保存出错停止写入功能（默认开启）
    3. 数据压缩（默认开启）
    4. RDB文件校验（默认开启）
    5. 指定本地数据库文件名，一般采用默认的 dump.rdb
### 3.3 AOF机制
### AOF机制以日志的形式记录 Redis 的每一个写操作，将 Redis 执行过的所有写指令保存下来，以追加的形式保存到 AOF 文件 (默认为 appendonly.aof) 中当需要恢复数据时，Redis 会重新执行 AOF 文件中的写指令，来达到恢复数据的目的。
### 3.4 AOF配置
    appendonly no # 是否开启aof
    appendfilename "appendonly.aof" # 文件名
    #磁盘同步策略 默认每秒一次  
    # appendfsync always  # 每次
    appendfsync everysec # 每秒一次
    appendfsync no # 由操作系统执行，默认Linux配置最多丢失30秒
    no-appendfsync-on-rewrite # 作用： 后台执行（RDB的save | aof重写）时appendfsync设为no
    auto-aof-rewrite-percentage # 作用： 自动触发AOF重写no-appendfsync-on-rewrite no
    aof-load-truncated # 作用：指定当发生AOF文件末尾截断时，加载文件还是报错退出
    aof-use-rdb-preamble # 作用： 开启混合持久化，更快的AOF重写和启动时数据恢复
### 详细总结配置查看`3.RDB.md`、`4.AOF.md`、`5.RDB和AOF总结.md`文件
****
## 4.发布 (pub) /订阅 (sub) 模式
### 发布/订阅模式模式包含两种角色：发布者和订阅者。订阅者可以订阅一个或多个通道(channel)，而发布者可以向指定的通道(channel)中发送消息，所有此通道的订阅者都会收到消息。拿一个现实生活中的例子来比喻的话，发布者就像一个电台广播员，订阅者就像听众，广播员将消息通过将消息发送到一个频道中，而这个频道的听众就会听到播音员的声音。
### 详情见`6.发布订阅模式.md`
****
## 5.布隆过滤器
### 相比于 Set 集合的去重功能而言，布隆过滤器在空间上能节省 90% 以上，但是它的不足之处是去重率大约在 99% 左右，也就是说有 1% 左右的误判率，这种误差是由布隆过滤器的自身结构决定的。俗话说“鱼与熊掌不可兼得”，如果想要节省空间，就需要牺牲 1% 的误判率，而且这种误判率，在处理海量数据时，几乎可以忽略。
### 1.下载
    编译安装，需要从 github 下载，下载地址：https://github.com/RedisBloom/RedisBloom
    编译插件
    cd RedisBloom-2.2.14
    make
    编译成功，生成 redisbloom.so 文件。
### 2.缓存穿透
    意味着有特殊请求在查询一个不存在的数据，即数据不存在 Redis 也不存在于数据库。
    1. 创建布隆过滤器：
    BF.RESERVE {key} {error_rate} {capacity} [EXPANSION {expansion}] [NONSCALING]
### 详情见`7.布隆过滤器.md`
## 6.主从复制
### Slave 启动成功连接到 master 后会发送一个 sync 同步命令，Master 接到命令后，会启动后台的存盘进程，同时收集所有接收到的用于修改数据集命令，在后台进程执行完毕后，master 将传送整个数据文件到 salve，并完成一次完整的同步。
### 主机数据更新后根据配置和策略， 自动同步到备机的master/slaver机制，**Master**以写为主，**Slave**以读为主
|     IP地址     |     角色     |
| :------------: | :----------: |
| 192.168.81.100 | redis-master |
| 192.168.81.101 | redis-slave1 |
| 192.168.81.102 | redis-slave2 |
### 1.配从不配主
### 192.168.81.101/192.168.81.102
    bind 0.0.0.0            #表示redis允许所有地址连接。默认127.0.0.1，仅允许本地连接。
    daemonize yes             #允许redis后台运行
    logfile "/usr/local/bin/redis/redis.log"    #设置redis日志存放路径
    requirepass "123456"        #设置redis密码
    protected-mode no      #设置为no，允许外部网络访问
    port 6379             #修改redis监听端口(可以自定义)
    pidfile "/usr/local/bin/redis/redis.pid"  #pid存放目录
    requirepass 123456     #设置redis密码
    masterauth 123456    #主从同步master的密码
    replicaof 192.168.81.100 6379
### 2.主机
    bind 0.0.0.0            #表示redis允许所有地址连接。默认127.0.0.1，仅允许本地连接。
    daemonize yes             #允许redis后台运行
    logfile "/usr/local/bin/redis/redis.log"    #设置redis日志存放路径
    requirepass "123456"        #设置redis密码
    protected-mode no      #设置为no，允许外部网络访问
    port 6379             #修改redis监听端口(可以自定义)
    pidfile "/usr/local/bin/redis/redis.pid"  #pid存放目录
    requirepass 123456     #设置redis密码
    masterauth 123456    #主从同步master的密码
### 3.启动查看状态
    # 显示有两个从机
    # Replication
    role:master
    connected_slaves:2
    slave0:ip=192.168.81.101,port=6379,state=online,offset=1470,lag=1
    slave1:ip=192.168.81.102,port=6379,state=online,offset=1470,lag=1
    master_failover_state:no-failover
    master_replid:e423bf4da80cd655727c45f1c06d099910228e04
    master_replid2:0000000000000000000000000000000000000000
    master_repl_offset:1470
    second_repl_offset:-1
    repl_backlog_active:1
    repl_backlog_size:1048576
    repl_backlog_first_byte_offset:1
    repl_backlog_histlen:1470
### 4.主机插入数据之后从机同样可以查看
    set k1 1 k2 2 k3 3 k4 4 
### 5.从节点默认是只读的，如果支持写 需要设置如下值 no,然后重启redis服务 才能有效。
    replica-read-only no
## 7.哨兵模式
### 哨兵模式概述
### （自动选主机的方式）
### 主从切换技术：当主机宕机后，需要手动把一台从（slave）服务器切换为主服务器，这就需要人工干预，费时费力，还回造成一段时间内服务不可用，所以推荐哨兵架构（Sentinel）来解决这个问题。
### 哨兵模式是一种特殊的模式，首先Redis提供了哨兵的命令，哨兵是一个独立的进程，作为进程，它独立运行。其原理是哨兵通过发送命令，等待Redis服务器响应，从而监控运行的多个Redis实例。

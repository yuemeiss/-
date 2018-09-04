redis集群
为什么搭建集群？
１．为了突破内存存储限制
２．可以实现实时备份（同步各节点的数据）
３．当有高并发操作的时候，我们可以让多个主节点执行，减轻服务器压力
４．可以提升存储、查询、修改等操作的效率
５．可以实现读写分离
６．当一个主节点宕机后，从节点可以变为主节点，但是如果多数节点发生宕机现象，集群就不可用了
７．数据透明
缺点：
不能够保证强一致性

如何搭建集群？
１．首先修改个服务器的redis的conf文件

下面是一个最少选项的集群的配置文件:

port 7000
bind 端口号
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
daemonize yes 进程守护，默认是NO

文件中的 cluster-enabled 
选项用于开实例的集群模式， 
而 cluster-conf-file 选项则设定了保存节点配置文件的路径，
默认值为 nodes.conf.节点配置文件无须人为修改， 
它由 Redis 集群在启动时创建， 并在有需要时自动进行更新。

２．修改完毕，启动各节点的redis服务

３．可以在任意服务端创建集群(redis-tirb.rb)
  3.1安装依赖：sudo apt-get install ruby
  查看ruby版本，显示说明安装成功：ruby -v

  3.2sudo gem install redis
  3.3创建集群：
  ./redis-trib.rb create --replicas 1 ip:端口　ip:端口　ip:端口
  ip:端口　....
  3.4会打印出节点的分配信息（哪些为主节点，哪些为从节点）

４．开启客户端验证：
可以连接任意主节点的redis的客户端：
redis-cli -c -h 主节点ip -p 主节点端口

补充：
zset 

zinterstore newkey num key1 key2 













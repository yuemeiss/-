关系型数据库：mysql
非关系型数据库：mongodb、redis
mongodb:（nosql:not only sql）
它是一个非关系型数据库(文档性(mongodb)、图像存储型、键值存储(redis)...)

{'name':'lisi'}
{'name':'xinc','age':20}
{'name':'xinc','age':20,'bhsc':'bckssc'}

数据库的配置文件
/etc/mongod.conf

#
service mongod start
地板本
service mongodb start

service mongod stop

service mongodb restart

# 查看当前数据库
db 

#查看所有数据库据
show dbs

#切换数据库（创建数据库）
use dbname

#查看数据库的状态信息
db.stats()

#查看数据库下面的所有集合
show collections

#删除数据库(你当前在那个数据库下，删除的就是那个数据库)
db.dropDatabase()

#创建结合
db.createCollection('dbname')

db.createCollection('dbname',{'capped':true,'size':1000,'max':10})

#插入数据
db.collectionname.insert({document})

#查找数据
db.collectionname.find({})
db.collectionname.find()


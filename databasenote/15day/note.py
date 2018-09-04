1.复习：
索引：
１．单键索引
db.colname.createIndex({key:排序})
２．复合索引
db.colname.createIndex({key:排序,key:排序,key:排序})
３．_id索引
４．唯一索引
db.colname.createIndex({key:排序,key:排序,key:排序},{unique:true})
５．稀疏索引
db.colname.createIndex({key:排序,key:排序,key:排序},{sparse:true})
５．子文档索引
db.colname.createIndex({'父key.子key':排序,'父key.子key':排序,'父key.子key':排序},{属性})
６．数组索引
db.colname.createIndex({tags:1})
７．全文索引
1.目的根据索引，进行全文查找（模糊匹配）
2.怎么创建的？
{title:'p abcd 1234 李，我是。sncdscn'}
{title:'p 1234 李，我是。sncdscn'}
{title:'abc'}
#创建一个全文索引
db.colname.createIndex({title:'text'})
#使用
db.colname.find({$text:{$search:'abc'}})
#搜索ｔｉｔｌｅ包含（abcd 或1234）的文档
db.colname.find({$text:{$search:'abcd 1234'}})
#搜索ｔｉｔｌｅ包含abcd不包含1234的文档
db.colname.find({$text:{$search:'abcd --1234'}})



属性：
background：当数据量太大，我们想要给某一个key添加索引，
这个时候会非常耗时，出现阻塞，我们可以设置background,在后台创建索引
name ：我们可以为索引起一个名称
unique ：　设置唯一索引
sparse ：稀疏索引，如果文档存在索引键就创建，不存在，不创建
expireAfterSeconds 设置过期时间，超时后，自动删除

#查看
db.colname.getIndexes()
#删除
db.colname.dropIndex('indexname')
#　创建
db.colname.createIndex({key:排序},{属性})

#强制索引(不支持全文索引)
db.colname.find({条件}).hint('indexname')

#全文索引（可以是）多个键共同组成一个全文索引，但是只能有一个全文索引
db.colname.createIndex({key:'text'})

#使用：
db.colname.find({$text:{$search:'关键字'}})

#查看集合下的索引大小
db.colname.totalIndexSize()

#重键索引
db.colname.reIndex()

#删除所有索引：(除了_id以外)
db.colname.dropIndexes()

#查看当前使用索引的信息
db.colname.find({条件}).explain()


#创建索引的注意事项和规则

#创建用户

#read
#readWrite
#root

创建一个超级管理员
use admin
db.createUser(
    {
        user:'username',
        pwd:'mima',
        roles:[{role:'root',db:'admin'}]
    }
)

１．修改/etc/mongod.conf 文件
２．打开其中的安全配置
#security:
#  authorization: enabled
３．退出保存，并重置

mongo -u 'ljh' -p '123' --authenticationDatabase 'admin'

#查看所有用户
use admin
db.system.users.find()

创建一个普通用户（必须是超级管理才能够创建）
> use class1804
switched to db class1804
> db.createUser(
... {user:'zhangsan',pwd:'12345',roles:[{role:'readWrite',db:'class1804'}]}
... )

mongo -u 'zhangsan' -p '12345' --authenticationDatabase 'class1804'

修改密码：
> use class1804
switched to db class1804
> db.updateUser('zhangsan',{pwd:'123456'})

删除用户权限
use class1804
db.revokeRolesFromUser('username',[{role:'',db:''}])

添加权限
> use class1804
switched to db class1804
> db.grantRolesToUser('zhangsan',[{role:'readWrite',db:'class1804'}])

删除用户（在当前用户所有权限的数据库下删除）：
> use class1804
switched to db class1804
> db.dropUser('zhangsan')

删除用户（在admin数据库下删除）：
use admin
db.system.users.remove({user:'username'})

#数据库的备份
mongodump -h 127.0.0.1:27017 -d class1804 -o ~/桌面/dump/

#有认证权限的时候
mongodump -u 'username' -p 'mima' --authenticationDatabase 'admin'' -d class1804 -o ~/桌面/dump/

#恢复：
mongorestore -h 127.0.0.1:27017 -d class1804 --dir ~/桌面/dump/class1804

#备份所有数据库：
mongodump -h ip:port -o 备份文件路径

#恢复（还原）所有数据库
mongorestore -h ip:port --dir 已经备份的文件路径

#mongodb 导出json文件
mongoexport -d dbname -c colname -o path(路径)/文件名.json --type json

#mongodb 导入json文件
mongoimport -d dbname -c colname --file path(路径)/文件名.json --type json

#mongodb 导出csv文件
mongoexport -d dbname -c colname -o path(路径)/文件名.csv --type csv -f '键的名称，键的名称，键的名称' 

#mongodb 导入csv文件
mongoimport -d dbname -c colname --file path(路径)/文件名.csv --headerline --type csv


#主从副本集
（实时备份、防止数据灾难、读写分离、无宕机行为）
#怎么实现主从？
必须要保证一注一从
开启服务。服务处于等待状态
mongod --bind_ip (ip) --port (port) --dbpath (数据备份的路径) --replSet (标示)rs0

连接服务？
mongo --host (ip) --port (port)

确定主节点（主窗口）
rs.initiate() (初始化主节点)

添加从节点
rs.add('ip:port')

查看节点信息
rs.status()

激活从节点
rs.slaveOk()













1.安装
2.mongodb服务：
sudo service mongod/mongodb start
sudo service mongod/mongodb stop
sudo service mongod/mongodb restart

配置文件路径 /etc/mongod.conf|mongodb.conf

３．连接：
mongo
mongo -h ip:prot
mongo --host ip --port port

4.mongodb的操作：
数据库：
　　 show dbs
    db
    use dbaname
    db.dropDatabase()
    db.stats()

集合：
　　db.createCollection('colname',属性)
   db.createCollection('colname')
   db.createCollection('colname',{capped:true,size:字节大小,max:最大文档数量})
   db.colname.drop()

文档的操作：
docment = {
    name:'xxx',
    age:20,
}
增：
db.colname.insert(docment)
db.colname.insert([docment,docment1,....])
db.colname.insertOne(docment)
db.colname.insertMany([docment,docment1,....])

删除：
db.colname.remove({})
db.colname.remove({条件})
db.colname.remove({条件},1) ->　db.colname.remove({条件},{justOne:true})

修改：
#更新文档中的某些键
db.colname.update({条件},{$set:{键:值}})
#全文档更新
db.colname.update({条件},{键:值})
#全文档更新(如果没找到，则作为一条新的数据插入)
db.colname.update({条件},{键:值},{upsert:true})
#save
# case1:假如我们要跟新的文档_id存在，则进行全文档跟新
# case2:假如我们要跟新的文档_id不存在，则作为新的文档插入
db.colname.save({_id:'',键:值,键:值,键:值,...})

查：
db.colname.find() -> db.colname.find({})
db.colname.find({条件}})　-> db.colname.find({age:20,name:'xxx'}})

限制查询：
db.colname.find({条件}).limit(num) - > db.colname.find({age:20,name:'xxx'}}).limit(3)

跳过：skip
db.colname.find({条件}).skip(num) 

结合使用：(返回符合条件的结果，从num1开始，返回num2条数据)
db.colname.find({条件}).skip(num１).limit(num2)

排序：sort　（１：升序，-1：降序）
db.colname.find({条件}).sort({键:方向})

投影：project (0:不显示，１：显示)
docment = {
    _id:'xklsancniwknc'
    name:'xxx',
    age:20,
    gender:'男',
    class:'1804'
}
db.colname.find({},{name:1,age:1,_id:0})
db.colname.find({},{name:0})

#distinct 去重
db.colname.distinct('键',{条件})　->　db.colname.distinct('age',{name:'lisi'})

#count() 计算总数
db.colname.find().count() 
db.colname.count({条件})　-> db.colname.find({条件}).count()

# $type:返回所有键为字符串类型的文档
db.colname.find({键:{$type:'string'}})

#比较运算符
=  -> db.colname.find({name:'xxx'}).count()
$lt 小于　-> db.colname.find({salary:{$lt:10000}}).count()
$lte 小于等于　-> db.colname.find({salary:{$lte:10000}}).count()
$gt 大于
$gte 大于等于
$ne 不等于
#逻辑运算符
$or -> db.colname.find({$or:[{salary:{$gt:10000}},{name:'liming'}]})
#范围运算符
$in -> db.colname.find({age:{$in:[19,23,30]}})
$nin -> db.colname.find({age:{$nin:[19,23,30]}})

#正则查询：(一定是字符窜)
db.colname.find({name:/^李.*?/})
db.colname.find({name:{$regex:'^李.*?'}})

#自定义查询：
db.colname.find({$where:function(){ reture this.name == '李磊' }})
db.colname.find({$where:function(){ reture this.age > 20 }})

#聚合操作：
#管道
$group $project　$match　$skip　$limit　$unwind　$sort

#函数
$sum $avg $max $min $push $last $first

docment = {
    _id:'xklsancniwknc'
    name:'xxx',
    age:20,
    gender:'男',
    class_:'1804'
}

$group:分组
#统计班级人数
db.colname.aggregate([{$group:{_id:'$class_',count:{$sum:1}}}])
#班级的平均年龄
db.colname.aggregate([{$group:{_id:'$class_',avgage:{$avg:'$age'}}}])
#返回班级的最大年龄，最小年龄
db.colname.aggregate([{$group:{_id:'$class_',maxage:{$max:'$age'}}}])
db.colname.aggregate([{$group:{_id:'$class_',minage:{$min:'$age'}}}])

#$push: 根据班级进行分组，返回班级下所有同学的姓名,返回的是一个数组
db.colname.aggregate([{$group:{_id:'$class_',names:{$push:'$name'},ages:{$push:'$age'}])

#last:返回集合总的最后一个name
db.colname.aggregate([{$group:{_id:'null',last:{$last:'$name'}}}])

#first:返回集合总的第一个name
db.colname.aggregate([{$group:{_id:'null',first:{$first:'$name'}}}])

$project (只返回年龄和性别)
db.colname.aggregate([{$project:{age:1,gender:1,_id:0}}])

$match:过滤 (返回年龄在大于５０，小于１００)
db.colname.aggregate([{$match:{age:{$gt:50,$lt:100}}}])

$sort 排序 (返回年龄在大于５０，小于１００,)
降序排列
db.colname.aggregate([{$match:{age:{$gt:50,$lt:100}}},{$sort:{age:-1,..}}])
升序排列
db.colname.aggregate([{$match:{age:{$gt:50,$lt:100}}},{$sort:{age:1,..}}])

$unwind:将文档中的键对应的数组，拆分成单条独立数据
docment = {
    _id:'xklsancniwknc'
    name:'xxx',
    age:20,
    gender:'男',
    class_:'1804',
    tags:['python','人工智能','mongodb']
}

db.colname.aggregate([{$unwind:'$tags'}]) 结果如下：

docment = {
    _id:'xklsancniwknc'
    name:'xxx',
    age:20,
    gender:'男',
    class_:'1804',
    tags:'python',
}

docment = {
    _id:'xklsancniwknc'
    name:'xxx',
    age:20,
    gender:'男',
    class_:'1804',
    tags:'人工智能',
}
.....

#skip与限制查询
db.colname.aggregate([{$match:{age:{$gt:30}}},{$limit:3}])
db.colname.aggregate([{$match:{age:{$gt:30}}},{$skip:2}])
db.colname.aggregate([{$match:{age:{$gt:30}}},{$skip:2},{$limit:3}])
#注意：skip与limit有先后顺序（顺序不同，会影响结果）

#索引：（ｍｏｎｇｏｄｂ的索引存放在内存中）
_id索引：这个在插入文档的会自动创建
普通索引：

　　单键索引：
　　　db.colname.createIndex({'索引键':方向})
　　复合索引：
　　　db.colname.createIndex({'索引键':方向,'索引键':'方向',..})

子文档索引：
{
    class_:'1804',
    students:{
        name:'liming',
        age:20,
        email:'nxkj@qq.com'
        adress:'北京'
    }
}
db.colname.createIndex({'students.name':1,'students.email':-1})
db.colname.find({'students.name':'liming','students.email':'nxkj@qq.com'})

数组索引：
db.colname.createIndex({tags:1})

全文索引：(在一个集合中只能创建一个)
{
    'content':'abc 123 李某某　1804 班'
}
db.colname.createIndex({content:'text',...})
使用
db.colname.find({$text:{$search:'关键词'}})

属性：
background 在后台创建索引
unique 唯一索引
name 给索引起一个名称
sparse 稀疏索引(if 设置了这个属性，文档中如果含有这个索引键，那么创建索引，else 不创建)
TTL expireAfterSeconds 秒　：改属性设置文档在集合中存活的时间，超时，则删除
注意：（我们直接插入一个时间，会跟文档中正真插入的时间，相差８小时。）

TTL补充：
   _id 不能设置为日期索引
   不能将已创建的索引直接修改为时间索引。只能删除，重新创建
   TTL不能是复合索引，只能是单键索引
   在固定的集合中，不能创建TTL索引

#删除索引
db.colname.dropIndex('索引名')
db.colname.dropIndexes()

#查看集合中的所有索引
db.colname.getIndexes()

#查看集合中的索引的总大小
db.colname.totalIndexSize()

#强制索引
db.colname.find({条件}).hint('索引名')

#重建索引
db.colname.reIndex()

#建立索引的注意事项、有点，缺点：
优点：相当于创建了一个目录，能够提高查找的效率
缺点：１．对于插入、删除、修改数据会变慢，因为在做插入、删除、修改数据的时候，索引也会随之变化，
这样会降低效率 ２.创建索引会产生额外的数据，增加我们对硬件的要求，会额外占用内存。

注意事项：
１．尽量减少创建不必要的索引
２．经常变动的键不必要创建索引
３．不会成为查询条件的值不需要创建索引
４．mongodb集合中最大的索引个数不能超过６４个，
索引的名称不能超过１２８个字符，符合索引最大只能有３１个字段
5.　不能命中索引的情况：$in $nin 范围运算符，以及比较运算符。。。。。
6.　mongodb中索引存放在内存中，必须确保索引的大小不会超过内存，
如果超过内存最大限制，mongodb会自动删除一些索引


创建用户：
#普通用户、超级管理员
1.#创建超级管理员：
root:
read:
readWrite
use admin
db.createUser({
    'user':'username',
    'pwd':'password',
    'roles':[{'role':'root',db:'admin'}]
})

2.#打开mongodb的安全设置
sudo vim /etc/mongod.conf
#高版本
#security:
#  authorization: enabled

2.1sudo vim /etc/mongodb.conf
#低版本
#auth=True

3.修改完毕之后重置:sudo service mongod|mongodb restart

4.使用超管登录
mongo -u 用户名 -p 密码 --authenticationDatabase 'admin'

创建一个普通用户
use dbname
db.createUser({
    'user':'username',
    'pwd':'password',
    'roles':[{'role':'readWrite',db:'dbname'}]
})

mongo -u 用户名 -p 密码 --authenticationDatabase 'dbname'

#修改用户信息
# 修改密码
db.updateUser('username',{pwd:'newpassword'})
# 修改用户名
db.updateUser('username',{user:'newusername'})

#删除权限
db.revokeRolesFromUser('username',[{role:'权限',db:'dbname'}])
#添加权限
db.grantRolesToUser('username',[{role:'权限',db:'dbname'}])

#删除用户
db.dropUser('username')
方式二
use admin
db.system.users.remove({user:'username'})

#查看所有的用户
use admin
db.system.users.find()

#mongodb数据备份
mongodump -h 127.0.0.1:27017(本地可以省略) -d dbname -o 备份文件的路径

#mongodb备份数据库下的集合
mongodump -h 127.0.0.1:27017(本地可以省略) -d dbname　colname -o 备份文件的路径

#备份所有数据库
mongodump -h 127.0.0.1:27017(本地可以省略) -o 备份文件的路径

#恢复数据库：
mongorestore -h 127.0.0.1:27017(本地可以省略) -d dbname --dir 备份文件的路径

#恢复数据库下的集合：
mongorestore -h 127.0.0.1:27017(本地可以省略) -d dbname　colname --dir 备份文件的路径

#回复所有数据库
mongorestore -h 127.0.0.1:27017(本地可以省略) --dir 备份文件的路径

#数据的导出（json、csv）
导出ｊson数据
mongoexport -d dbname -c colname -o ~/桌面/dump/名称.json --type json 
导出csv数据
mongoexport -d dbname -c colname -o ~/桌面/dump/名称.csv --type csv -f '键名,键名...'

#导入数据
导入ｊson数据
mongoimport -d dbname -c colname --file ~/桌面/dump/名称.json --type json

导入csv数据
mongoimport -d dbname -c colname --file ~/桌面/dump/名称.csv --type csv -filed '键名,..' ????
mongoimport -d dbname -c colname --file ~/桌面/dump/名称.csv --headerline --type csv

#mongodb状态检测
mongostat

mongotop

#副本集

#目的：
１．防止数据灾难
２．实时备份，实现主从节点数据一致性
３．读写分离
４．无宕机行为
５．分担主节点的压力

缺点：具有中心化，所有的增删改操作都需要在主节点完成，
对主节点的压力较大，对主机的性能要求较高。

#如何实现副本集？
#开启mongod服务（至少两个）
mongod --bind_ip ip --port port --dbpath 数据存放的路径　--replSet rs0
....

#连接ｍｏｎｇｏ服务
mongo --host ip --port port

#确定主节点
rs.initiate()

#添加从节点
rs.add('ip:port')

#激活从节点
rs.slaveOk()

#mongodb 与python的交互
...
#　mongodb与python的交互
# 　pip3 intsall pymongo
import pymongo
from bson.objectid import ObjectId

#创建mongo客户端链接
mongoConn = pymongo.MongoClient('localhost',27017)
# 第二种
# mongoConn = pymongo.MongoClient('mongodb://localhost:27017/')

#有账号和密码的连接
#mongoConn = pymongo.MongoClient('mongodb://user:paw@localhost:27017/')


#操作数据库下的集合
#获取要操作的数据库
# use_db = mongoConn.数据库名称
use_db = mongoConn.mongotest
# use_db = mongoConn['mongotest']

#获取数据库下要操作的集合
use_col = use_db.class1804
# use_col = use_db['class1804']

#文档操作
# 增
def add_data():
    document = {
        # '_id':'2e761r27e1' 指定id
        'name':'liyong',
        'age':20,
        'gender':'男',
        'class':'1804',
    }

    document1 = {
        'name':'lihua',
        'age':22,
        'gender':'男',
        'class':'1804',
    }
    #插入单条(result直接返回一个ｉｄ串)
    # result = use_col.insert(document)
    # use_col.insert_one(document)
    #插入多条(result直接返回list(Object(...),Object(...))
    result = use_col.insert([document,document1])
    # use_col.insert_many([document,document1])
    #也可以使用save
    # use_col.save(document)
    print(result)
# 删

def delete_data():
    #删除一条
    #result = use_col.delete_one({})
    # result = use_col.remove({'name':'liyong'},multi=False)
    # print(result)
    #删除多条
    # result = use_col.delete_many({})
    #　multi=False删除一条，multi=True删除多条，
    result = use_col.remove({'name':'liyong'})
    print(result)

# 改
def update_data():
    #默认情况下只修改一条
    # result = use_col.update({'name':'liyong'},{'$set':{'age':23}})
    # print(result)
    #全文档更新只修改一条
    # result = use_col.update({'name':'liyong'},{'name':'lisi','age':23})
    # print(result)
    #更新超照到的全部结果修改多条
    # result = use_col.update_many({'name':'liyong'},{'$set':{'age':23}})
    # print(result)
    #　使用save做更新操作,全文档更新
    #注意：name 'ObjectId' is not defined,导入Bson模块下的objectid
    result = use_col.save({'_id':ObjectId("5b836b9711575e79be9af0c7"),'name':'wangwu'})
# 查

def find_data():
    #　使用find查询，会返回一个ｃｕｒｓｏｒ对象，
    #<pymongo.cursor.Cursor object at 0x7fa13d988e10>
    # 我们要拿到数据，需要遍历
    # result = use_col.find({'name':'liyong'})
    # print(result)
    # print([i for i in result])

    # result = use_col.find_one_and_delete()
    # result = use_col.find_one_and_replace()
    # result = use_col.find_one_and_update()

    #find_one查询时，直接返回一个字典
    # result = use_col.find_one({'name':'liyong'}) 
    # print(result)
    # print(type(result))

    #跳过和限制查询s
    # result = use_col.find({}).limit(4).skip(2).sort([("age",1),("name",1)])
    result = use_col.find({}).limit(4).skip(2).sort("age",1).sort("name",1)
    print([i for i in result])

    # for dict in result:
    # print(dict)

    
if __name__ == '__main__':
    # add_data()
    #update_data()
    # find_data()
    #delete_data()
   
























































#复习
sudo service mongod/mongodb strat/stop/restart

mongod.conf -> /etc/mongod.conf (数据库的数据路径、ｌｏｇ日志路径、ｉｐ、ｐｏｒｔ等)

db

show dbs

use dbname 

db.stats()

db.dropDatabase()

db.createCollection(colname,{参数})
# 不固定大小的集合
db.createCollection(colname)
# 固定大小的集合（超出会覆盖）
db.createCollection(cloname,{capped:true,size:1000,max:100})

#
db.colname.insert({key:'value',....})
db.colname.insert([{key:'values'},{key:'values',....}])

db.colname.insertOne({key:'values'})
db.colname.insertMany([{key:'values'}....])

#
db.colname.find()
db.colname.find({})

#自己设置_id,但是必须要保证唯一，如果不唯一，插入数据会报错。
db.colname.insert({_id:'values'})

#
db.colname.drop()


{key:[1,2,3,4,5],key:NULL}

#update

db.colname.update({条件},{$set:{age:20}})

db.colname.update({条件},{age:20})

#multi:true表是更改所有查到（满足条件）的数据（multi默认是ｆａｌｓｅ，只跟新一条）
db.colname.update({条件},{$set:{age:20}},{multi:true})

#upsert:true表示找不到数据，插入一条数据，upsert:默认是ｆａｌｓｅ
db.students.update({name:'李三'},{name:'李四'},{upsert:true})

#假如_id这个文档已经存在，那么全文档覆盖，反之，新插入一条数据
db.colname.save({_id:'value',name:'',age:''})

#不跟ｉｄ，相当于ｉｎｓｅｒｔ插入数据，效率低
db.colname.save({name:'',age:''})

#　remove,删除所有
db.colname.remove({条件})

# 删除一条
db.colname.remove({条件},{justOne:true})
db.colname.remove({条件},1)

查：
db.colname.find()
db.colname.find({条件})
比较运算符
等于
db.colname.find({name:'',age:''})
$lt 小于
db.colname.find({age:{$lt:20}})
$lte 小于等于
db.colname.find({age:{$lte:20}})
$gt 大于
db.colname.find({age:{$gt:20}})
$gte 大于等于
db.colname.find({age:{$gte:20}})
$ne 不等于
db.colname.find({age:{$ne:20}})
$or 或者
db.colname.find({$or:[name='张三',{age:{$gt:23}}]})
$in (范围查询)相当于或者的意思
db.colname.find({age:{$in:[25,28,30]}})
$nin (不在某个范围)
db.colname.find({age:{$nin:[25,28,30]}})

#正则的使用
#/正则表达式/
#{key:{$regex:'正则表达式'}}
db.colname.find({key:/正.../})
db.colname.find({key:{$regex:'正则表达式'}})

#可以自定义函数查询
db.students.find({$where:function(){return this.gender=='女'}})

# 可以根据$ｔｙｐｅ 查找指定类型的文档
db.students.find({age:{$type:'string'}})

# limit:返回限定的条数
db.students.find().limit(2)

#skip  跳过指定条数，返回其他所有
db.students.find().skip(2)

#skip  跳过指定条数，返回限定的条数（skip与limit的先后顺序无所谓）
db.students.find().skip(2).limit(2)
db.students.find().limit(2).skip(2)

# pretty()　按照ｊｓｏｎ的格式化结构输出结果
db.colname.find().pretty()

#sort 排序(1:表示升序，-1:表示降序)
db.colname.find({条件}).sort({age:1})

db.colname.find({条件}).sort({age:1,salary:-1})

#distinct 去重
db.colname.distinct('字段名',{条件})

#投影（相当于ｍｙｓｑｌ中的检索列的功能）
#除了年龄这个字段不返回外，其他都给返
db.colname.find({},{age:0,name:0})(name、ｓａｌａｒｙ)

#除了年龄之外其他的文档字段都不给返回（_id必反）
db.colname.find({},{age:1})

#count 统计数量
db.colname.find({条件}).count()

db.colname.count({条件})

#聚合
{ "_id" : ObjectId("5b7d0c370ab2ba397a8d712d"), "title" : "MongoDB Overview", "description" : "MongoDB is no sql database", "by_user" : "w3cschool.cc", "url" : "http://www.w3cschool.cc", "tags" : [ "mongodb", "database", "NoSQL" ], "likes" : 100 }
{ "_id" : ObjectId("5b7d0c370ab2ba397a8d712e"), "title" : "NoSQL Overview", "description" : "No sql database is very fast", "by_user" : "w3cschool.cc", "url" : "http://www.w3cschool.cc", "tags" : [ "mongodb", "database", "NoSQL" ], "likes" : 10 }
{ "_id" : ObjectId("5b7d0c370ab2ba397a8d712f"), "title" : "Neo4j Overview", "description" : "Neo4j is no sql database", "by_user" : "Neo4j", "url" : "http://www.neo4j.com", "tags" : [ "neo4j", "database", "NoSQL" ], "likes" : 750 }
{ "_id" : ObjectId("5b7d0ce60ab2ba397a8d7130"), "title" : "python", "description" : "this is a python book", "by_user" : "1234_abcd", "url" : "https://www.baidu.com/", "tags" : [ "mongodb", "mysql", "redis" ], "likes" : 800 }

#根据作者分作，统计每个分组的下文档数量
db.books.aggregate([{$group:{_id:'$by_user',count:{$sum:1}}}])

#_id为空的时候，将所有的文档分为一组
db.books.aggregate([{$group:{_id:'null',count:{$sum:1}}}])

#统计每个分组下的，文档的ｌｉｋｅｓ字段的总和
db.books.aggregate([{$group:{_id:'$by_user',likes:{$sum/max/min/avg:'$likes'}}}])

#first 返回分组文档里面的第一个文档中的某个字段
db.books.aggregate([{$group:{_id:'$by_user',url:{$first:'$url'}}}])

#last 返回分组文档里面的最后一个文档中的某个字段
db.books.aggregate([{$group:{_id:'$by_user',url:{$last:'$url'}}}])

#push 可以将分组文档中的某个字段，以数组的形式返回
db.books.aggregate([{$group:{_id:'$by_user',push:{$push:'$url'},...}}])
db.books.aggregate([{$group:{_id:'$by_user',push:{$push:'$$ROOT'}}}])

#project:
db.colname.aggregate([{$project:{'字段':1}}])
db.colname.aggregate([{$project:{'字段':0}}])

#分组和投影共同使用
db.books.aggregate([{$group:{_id:'$by_user',count:{$sum:1}}},{$project:{count:0,_id:0}}])

#limit 限定返回
db.books.aggregate([{$limit:2}])

#skip　跳过
db.books.aggregate([{$skip:2}])

#组合使用（有先后顺序会印象结果）
db.books.aggregate([{$skip:2},{$limit:2}])

#match 过滤
db.books.aggregate([{$match:{likes:{$gt:20,$lt:50}}}])
db.books.aggregate([{$match:{likes:{$gt:20,$lt:50}}},{$skip:2},{$limit:2}])

#unwind 将文档中的数组拆分成单条数据
db.books.aggregate([{$unwind:'$tags'}])



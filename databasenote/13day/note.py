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







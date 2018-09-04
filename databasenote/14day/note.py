索引：
_id :是一个索引

查看所有索引：
db.colname.getIndexes()

#创建单列索引：
db.colname.createIndex({'key':1|-1)

#可以查看当前使用的索引的信息
db.jobdesc1.find({jobname:'python'}).explain()

#复合索引
db.colname.createIndex({key1:1,key2:-1,})

#给数组添加索引：
db.colname.createIndex({数对应的键:1})
注意：查找的时候数组中的值的顺序必须一致


你好我不好你好吗

好吗

#删除索引
db.colname.dropIndex('indexname)

## 索引的属性
##后台创建索引：
db.jobdesc1.createIndex({jobname:1},{background:true})

{name:'',desc:'',age:'',gender:}
{name:'',desc:'',gender:}
{name:'',desc:'',age:''}
{name:'',desc:'',age:'',gender:}
{name:'',desc:'',age:'',gender:}

# 唯一索引
１．假如集合中已经存在多个相同的值，不能创建成功
２．假如成功创建唯一索引，不能重复插入
db.colname.createIndex({field:1,field:1,field:-1},{unique:true})

#name :给我们创建的索引起个名
db.colname.createIndex({field:1,field:1,field:-1},{unique:true,name:'indexname'})

#sparse 稀疏索引
因为mongodb中集合里面可以存在不同的文档数据，那么我们在创建索引的时候，就会出现，有些文档含有
索引键，有些文档没有索引键，我们可以使用sparse 稀疏索引这个属性，如果存在索引键的文档就会创建索引
，不在在索引键的文档就不会创建（索引键）对应的索引。

#expireAfterSeconds :给文档设置一个过期时间，文档从插入时开始，能存活的时间，到达时间自动删除（延迟１）分钟
#插入的时间会跟本地时间(北京时间)有８小时的时差
db.colname.createIndex({field:1,field:1,field:-1},{expireAfterSeconds:60})

#删除所有索引（除了_id索引以外）
db.colname.dropIndexes()

# 重建索引
db.colname.reIndex()

# {name   desc  age}
# {name   desc  age}
# {name   desc  age}
# {name   desc  age}
# {name   desc  age}
# {name   desc  age}

#强制索引hint：
db.colname.find({'索引'：'值'}).hint('索引名称')

##查看索引总大小
db.jobdesc1.totalIndexSize()

## 创建超级管理员


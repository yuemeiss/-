import pymongo

#导入ｂｓｏｎ模块
from bson.objectid import ObjectId

mongoConn = pymongo.MongoClient('localhost',27017)

#密码链接

#mongoConn = pymongo.MongoClient('mongodb://user:dzb)


user_db = mongoConn.p1804

user_col = user_db.global_suoyin

def add():
    document = {
        'name':'dad',
        'age':20,
        'gender':'男',
        'class':'1804',

    }
    #result 返回一个ｉｄ字符串
    result = user_col.insert(document)
    

def alter():
    #修改
    #全文档只修改一条
    result = user_col.update({'name':'dad'},{'$set':{'name':'xxx'}})

    #修改多条
    
    print(result)
def find():
    #查找
    result = user_col.find({})
    #跳过

def delete():
    #删除
    pass



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
    pass
   



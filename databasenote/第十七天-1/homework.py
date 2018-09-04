import pymongo
from bson.objectid import ObjectId

mongoConn = pymongo.MongoClient('localhost',27017)

# mongoConn = pymongo.MongoClient('mongodb://user:pwd@ip:port/')
db = mongoConn.mgj

def get_product_data():
    #１． 获取商品的列表信息
    result = db.productsinfo.find()
    print([product for product in result])

def get_product_data_sort():
    #２． 获取商品的列表，并根据商品的价格按照降序排列
    result = db.productsinfo.find().sort('price',-1)
    # result = db.productsinfo.find().sort([('price',-1),...])
    print([product for product in result])
    # print([type(i['price']) for i in [product for product in result]])
    

def get_user_info():
    #３． 查询出用户表中的年龄大于２０岁的用户的信息
    result = db.usersinfo.find({'age':{'$gt':20}})
    print([info for info in result])

def sum_order_price():
    result = db.orderinfo.find()
    #查询订单列表
    order_list = [order for order in result]
    for order in order_list:
        #获取每个订单的详情
        print(order)
        sum = 0
        for productid in order['products']:
            #获取每个商品的id
            # print(productid)
            productinfo = get_product_info(productid)
            price = productinfo['price']
            sum += price

        print(sum)

def get_product_info(productid):
    # 根据商品id,查找商品信息
    result = db.productsinfo.find_one({'_id':ObjectId(productid)})
    # 返回商品信息,是一个字典
    return result

def create_user_index():
    #添加索引
    reslut = db.usersinfo.create_index([('address','text')])
    #返回索引名称
    print(reslut)

def find_user_info():
    #５． 在用户列表中创建adress为全文索引，查询出所有地址中包含北京市的用户的用户信息
    result = db.usersinfo.find({'$text':{'$search':'北京市'}}) 
    print(result)
    print([user for user in result])

def get_userinfo_by_order():
    result = db.orderinfo.find()
    #查询订单列表
    order_list = [order for order in result]
    for order in order_list:
        #获取每个订单的详情
        print(order['userid'])
        userinfo = get_userinfo_by_userid(order['userid'])
        print(userinfo)

def get_userinfo_by_userid(userid):
    result = db.usersinfo.find_one({'_id':ObjectId(userid)})
    return result



if __name__ == '__main__':
    #get_product_data()
    #get_product_data_sort()
    #get_user_info()
    #sum_order_price()
    #create_user_index()
    #find_user_info()
    #get_userinfo_by_order()
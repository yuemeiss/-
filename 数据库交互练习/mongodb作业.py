import pymongo
import time

#创建连接
mongoConn = pymongo.MongoClient('localhost',27017)

#获得数据库
mydb = mongoConn.mogujie

#获得数据库下的集合
user_col = mydb.m_user
product = mydb.m_product
order_1 = mydb.m_order


#文档操作
def add_msg():
    name = input('用户名:')
    age = int(input("年龄:"))
    address = input('地址:')
    phonenum = input('手机号:')
    document = {
        'name':name,
        'age':age,
        'address':address,
        'phonenum':phonenum,
    }
    #插入数据 result　返回的结果是文档的ｉｄ　字符串类型
    result = user_col.insert(document)
    return result
def add_product():
    name = input("商品名:")
    price = float(input('价格'))
    product_info = input('商品描述:')
    document = {
        'productname':name,
        'productprice':price,
        'productinfo':product_info,
    }
    #插入数据 result　返回的结果是文档的ｉｄ　字符串类型
    result = product.insert(document)
    return result
def add_order(user_id,pro_id):
    orderinfo = time.asctime()
    document = {
       'orederinfo':orderinfo,
       'products':pro_id,
       'username':user_id['name'],
       'userid':user_id['_id'],
    }
    #插入数据 result　返回的结果是文档的ｉｄ　字符串类型
    result = order_1.insert(document)
    return result
def main():    
    while True:
        user = input('1.添加用户 2.商品 3.添加订单　q.退出')
        if user == '1':
            add_msg()
        if user == '2':
            add_product()
        if user == '3':
            user_name = input('用户名:')
            userId = user_col.find_one({'name':user_name})
            pro_id = []
            while True:
                user_pro = input('输入要购买的商品名:')
                if user_pro == 'q':
                    break
                productid = product.find_one({'productname':user_pro})
                pro_id.append(productid['_id'])
            add_order(userId,pro_id)
        else:
            break

#第一题
def aa():
    result = product.find()
    pro_list = [i for i in result]
    print(pro_list)
#2
def bb():
    result = product.find().sort([('productprice',-1)])
    print([i for i in result])
#3
def cc():
    result = user_col.find({'age':{'$gt':20}})
    print([i for i in result])
#4
def dd(userName):
    #userName = input('用户名:')
    ss = order_1.find_one({'username':userName})
    money = 0
    for i in ss['products']:
        price = product.find_one({'_id':i})['productprice']
        money = money + price
    # print(money)
    return money
def dd_one():
    result = order_1.aggregate([{'$group':{'_id':'$username'}}])
    for i in result:
        # print(i)
        print('用户:%s 消费金额:%.2f'% (i['_id'],dd(i['_id'])))
#5
def ee():
    user_col.create_index([('address','text')])
    jieguo = user_col.find({'$text':{'$search':'北京市'}})
    print([i for i in jieguo])

#6
def ff():
    # userName = input('用户名:')
    # ss = order_1.find_one({'username':userName})
    result = order_1.find({})
    for ss in result:
        print(ss['username'])
        for i in ss['products']:
            price = product.find_one({'_id':i})
            print(price)
#7
def gg():
    result = order_1.find({})
    for i in result:
        userinfo = user_col.find_one({'_id':i['userid']})
        print(userinfo)


aa()
print('*'*50)
bb()
print('*'*50)
cc()
print('*'*50)
dd_one()
print('*'*50)
ee()
print('*'*50)
ff()
print('*'*50)
gg()
 

    

import pymysql

#链接mysql
mysqlconn = pymysql.connect(host='localhost',user='root',password='123456',database='user_register',charset='utf8')
#创建游标
cursor_handler = mysqlconn.cursor(cursor=pymysql.cursors.DictCursor)


#验证用户名
def yz_name(userName):
    #获得数据库 信息
    massgin = '''
        select user_name,user_passwd,user_state from register where user_name = %s ;
    '''      #是否命中索引  ?????
    #执行sl语句
    cursor_handler.execute(massgin,[userName])

    #获得 用户信息列表
    data_mas = cursor_handler.fetchone()
    return data_mas


#验证用户名（没用索引）
# def yz_name(userName):
#     for i in data_mas:
#         if userName == i['user_name']:
#             return i
#     return False


#密码错误三次，冻结账号；
def account_state(userName):
    sql = '''
        update register set user_state = 1 where user_name = %s
    '''
    #执行sql语句
    cursor_handler.execute(sql,[userName])
    #提交数据
    mysqlconn.commit()
def data_close():
    #关闭
    cursor_handler.close()
    mysqlconn.close()
def main(user_name):        
    #验证密码的次数
    passwd_flag = 5
    flag = True
    while flag:
        # user_name = input('用户名:')
        if user_name == 'q':
            print('退出登录')
            break
        userMas = yz_name(user_name)
        if userMas:
            print('用户名验证成功')
            if userMas['user_state'] == 0:
                while passwd_flag > 0:
                    user_passwd = input('密码:')
                    if user_passwd == 'q':
                        flag = False
                        break
                    if user_passwd == userMas['user_passwd']:
                        print('登录成功')
                        flag = False
                        data_close()
                        return {'mima':user_passwd,'status':0}
                    else:
                        print('密码错误,您还有%d次机会'% (passwd_flag - 1))
                        passwd_flag -= 1
                if passwd_flag == 0:
                    account_state(user_name)
                    print('已将该账号冻结')
                    flag = False
                    return False
            else:
                print('该账户已冻结')
                # data_close()
        else:
            print('用户不存在')
            # user_name = input('用户名:')
            break
    return False
    
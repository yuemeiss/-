import pymysql
import random,re

#建立链接
mysqlconn = pymysql.connect(host='localhost',user='root',password='123456',database='user_register',charset='utf8')

#创建游标 用于执行sql语句 使用返回字典的方式
cursor_handler = mysqlconn.cursor(cursor=pymysql.cursors.DictCursor) 
#获得数据库  用户名 信息
def yz_userName(name):
    name_sql = '''
        select user_name from register where user_name = %s;
    '''
    #执行sql语句
    cursor_handler.execute(name_sql,[name])
    #获得 字典类型的信息
    data_user_name = cursor_handler.fetchone()
    return data_user_name

#获得所有 用户名 并验证是否存在
# def yanzheng(data_base,name):
#     userName = []
#     for d in data_base:
#         userName.extend(d.values())
#     if name in userName:
#         return True
#     else:
#         print('用户名可用')
#         return False



#验证密码格式
def yz_passwd(passwd):
    while True:
        aa = re.match('^[A-Za-z].*',passwd)
        if aa and len(passwd) >= 8:
            return True
        else:
            print('密码格式不正确\n(开头必须是字母,并且不能少于8位)')
            passwd = input('密码:')
    return False
def zhuce():
    #填写注册信息
    print('用户注册（退出输q）'.center(50,'*'))
    name = input('用户名:')
    
    while True:
        if yz_userName(name):
            print('用户名已存在,请重新输入')
            print(len(name))
            name = input('用户名:')
        elif name == 'q':
            print('退出注册')
            break
            # exit()
        else:
            #输入用户名需大与 两个字
            if len(name) > 2:
                passwd = input('密码:')
                if yz_passwd(passwd):
                    print('密码格式正确')
                    while True:
                        confirm_password = input('确认密码')
                        if passwd == confirm_password:
                            print('密码确认成功')
                            break
                        else:
                            print('两次密码不一致')
                    email = input('邮箱地址:')
                    sex = int(input('性别'))
                    while sex != 1 and sex != 0:
                        print('重新输入')
                        sex = int(input('性别'))
                    age = int(input('年龄'))
                    #用户指纹
                    token = name + '-' + str(random.randint(000,999))  
                    sql = '''
                        insert into register(user_token,user_name,user_passwd,user_email,user_gender,user_age)
                        values(
                        %s,%s,%s,%s,%s,%s
                        );  
                    '''
                    #执行sql语句
                    cursor_handler.execute(sql,[token,name,passwd,email,sex,age])

                    #提交数据
                    mysqlconn.commit()

                    # #关闭
                    # cursor_handler.close()
                    # mysqlconn.close()

                    print('注册成功'.center(50,'='))
                    break
            else:
                print('用户名输入有误')
                print('用户名至少3个字')
                name = input('用户名:')
                # break

           
        


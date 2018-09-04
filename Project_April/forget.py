import pymysql,random,re
import redis
#连接redis数据库
redisConn = redis.StrictRedis('localhost',6379,0)

#MySQL数据库
mysqlconn = pymysql.connect(host='localhost',user='root',password='123456',database='user_register',charset='utf8')

cursor_handler = mysqlconn.cursor(cursor=pymysql.cursors.DictCursor)
#验证用户名
def yz_userName(name):
    name_sql = '''
        select user_email from register where user_name = %s;
    '''
    #执行sql语句
    cursor_handler.execute(name_sql,[name])
    #获得
    data_user_name = cursor_handler.fetchone()
    return data_user_name
#验证密码格式
def yz_passwd(passwd):
        while True:
            aa = re.match('^[A-Za-z].*',passwd)
            if aa and len(passwd) >= 8:
                return passwd
            else:
                print('密码格式不正确\n(开头必须是字母,并且不能少于8位)')
                passwd = input('密码:')
        return False
#修改密码
def account_passwd(userPasswd,userName):
    sql = '''
        update register set user_passwd = %s,user_state = 0 where user_name = %s
    '''
    #执行sql语句
    cursor_handler.execute(sql,[userPasswd,userName])
    #提交数据
    mysqlconn.commit()


# #发布验证码
# def auth_code(channel):
#     # channel = input("发布频道:")
#     msg = random.randint(0000,9999)
#     redisConn.publish(channel,msg)
#     return msg


#接收验证码
def accept_code(channel):
    Flag=True
    #创建订阅对象
    chan=redisConn.pubsub()
    #订阅
    chan.subscribe(channel)
    msg=chan.parse_response()#第一次会返回订阅确认信息
    print(msg)
    print("订阅成功，开始接收验证码")
    while Flag:
        msg=chan.parse_response()#接收消息
        if msg:
            print(msg)
            break
    return msg[2].decode()  

#redis用户密码和状态的修改
def r_status(name,passwd):
    result = redisConn.hmset(name,{'mima':passwd,'status':0})
    return result



#主程序
def alter_passwd():
    print('忘记密码（退出输q）'.center(50,'*'))
    while True:
        name = input('用户名:')
        email = yz_userName(name)
        if name != 'q':
            if email:
                print('用户名正确')
                # #选择频道 发布验证码
                # aa = auth_code(email['user_email'])
                # print('已经向 %s 发送验证马: %d'% (email['user_email'],aa))
                while True:
                    #接收验证码
                    code1 = accept_code(email['user_email'])
                    yanzhengma = input('输入验证马:')
                    if yanzhengma == str(code1):
                        print('验证码正确')
                        break
                    else:
                        print('验证吗错误')
            mima = input('新密码:')
            password = yz_passwd(mima)
            if password:
                print('密码格式正确')
                while True:
                    confirm_password = input('确认密码:')
                    if password == confirm_password:
                        print('密码确认成功')
                        #修改密码
                        account_passwd(confirm_password,name)
                        r_status(name,confirm_password)
                        print('密码修改成功')
                        break
                    else:
                        print('两次密码不一致')
                    
        else:
            print('退出更改')
            break
    
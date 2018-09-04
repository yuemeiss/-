import pymysql,random,re

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
    data_user_name = cursor_handler.fetchall()
    return data_user_name
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
#修改密码
def account_passwd(userPasswd,userName):
    sql = '''
        update register set user_passwd = %s,user_state = 1 where user_name = %s
    '''
    #执行sql语句
    cursor_handler.execute(sql,[userPasswd,userName])
    #提交数据
    mysqlconn.commit()
print('忘记密码（退出输q）'.center(50,'*'))
while True:
    name = input('用户名:')
    email = yz_userName(name)
    if name != 'q':
        if yz_userName(name):
            print('用户名正确')
            aa = random.randint(0000,9999)
            print('已经向 %s 发送验证马: %d'% (email[0]['user_email'],aa))
            while True:
                    yanzhengma = input('输入验证马:')
                    if yanzhengma == str(aa):
                        break
                    else:
                        print('验证吗错误')
            passwd = input('新密码:')
            if yz_passwd(passwd):
                print('密码格式正确')
                while True:
                    confirm_password = input('确认密码:')
                    if passwd == confirm_password:
                        print('密码确认成功')
                        #修改密码
                        account_passwd(confirm_password,name)
                        print('密码修改成功')
                        break
                    else:
                        print('两次密码不一致')
                
    else:
        print('退出更改')
        break
    
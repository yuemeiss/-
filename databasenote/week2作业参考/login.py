# -*- 
"""
     aim: 基于文件存储的用户登录程序（3次登录失败，锁定用户）
     
     need: 
         a. 用户信息文件
         b. 用户输入
     
     logical:
         a. 校验用户名合法情况
         b. 校验用户锁定情况
         c. 校验密码
         d. 更新登录失败次数
         
     sum:
         b. 逻辑判断情况
"""


import pymysql,hashlib

conn = pymysql.connect('localhost','root','ljh1314','week2homework',charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 1、MD5加密
# 不能直接对字符串加密，要先把字符串转换为bytes类型
def my_md5(str):
    new_str=str.encode()#把字符串转换成bytes类型
    #new_str=b'%s'%str #把字符串转换成bytes类型
    m=hashlib.md5()  #实例化MD5对象
    m.update(new_str)  #加密
    return m.hexdigest()  #获取结果返回

# 主程序退出标志位
flag = True
# 密码错误次数(登录失败次数)
exit_flag = 0
#上一次登录的用户名
last_user_name = ''


def find_user_from_db(name):
    sql = """
    SELECT * FROM register WHERE name=%s
    """
    res = cursor.execute(sql,[name])
    conn.commit()
    if res == 0:
        return 0
    else:
        return cursor.fetchone()

def update_data_to_db(data):
    sql = """
    UPDATE register SET isfreeze=%s WHERE name=%s
    """
    try:
        cursor.execute(sql,['1',data['name']])
        conn.commit()
    except:
        print('数据更新失败')
        conn.rollback()

def close():
    cursor.close()
    conn.close()

def checkpwd(data):
    global exit_flag
    user_pwd = input("密码: ")
    # 校验密码
    if my_md5(user_pwd) == data['password']:
        print('登录成功') 
        return True
    else:
        print('密码错误') 
        if exit_flag < 3:
            exit_flag += 1
            print(exit_flag)
            checkpwd(data)
        else:
            print("用户已经锁定,24小时后将解锁")
            data['isfreeze'] = '1'
            #更新数据到文件中
            update_data_to_db(data)
            return False 

def main():

    print("""欢迎来到数据库学习月度！体验登录功能""")
    
    global flag,exit_flag,last_user_name
    while flag:
        user_name = input("用户名(退出[Q]): ")
        # 退出判断
        if user_name != 'Q':
            data = find_user_from_db(user_name)
            print(data)
            if data == 0:
                print('用户名不存在')
            else:
                if last_user_name != user_name:
                    exit_flag = 0
                    last_user_name = user_name

                if int(data['isfreeze']) == 1:
                    close()
                    flag = False
                    print("用户已经锁定,24小时后将解锁")
                else:
                    checkpwd(data)
                    close()
                    flag = False
        else:
            close()
            flag = False
            
       

if __name__ == '__main__':
    main()
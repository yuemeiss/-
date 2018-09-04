#注册
#如何完善注册代码？可以判断用户是否已经注册？可否添加修改密码的逻辑？
# mysql> create table register(
#     -> num int auto_increment,
#     -> token char(255),
#     -> name varchar(15),
#     -> password varchar(255),
#     -> email varchar(50),
#     -> gender int default 0,
#     -> age int,
#     -> isfreeze int default 0,
#     -> primary key(num),
#     -> index name_index (name)
#     -> );
# Query OK, 0 rows affected (0.03 sec)

import pymysql,re,hashlib

conn = pymysql.connect('localhost','root','ljh1314','week2homework',charset='utf8')
cursor = conn.cursor()

# 主程序退出标志位
flag = True

def checkpwd(pwd):
    check_pwd = input('请再次输入密码(退出[Q]):')
    if check_pwd != 'Q':
        if check_pwd == pwd:
            return True
        else:
            print('请核实后再次输入密码')
            checkpwd(pwd)
    else:
        return False

# 1、MD5加密
# 不能直接对字符串加密，要先把字符串转换为bytes类型
def my_md5(str):
    new_str=str.encode()#把字符串转换成bytes类型
    #new_str=b'%s'%str #把字符串转换成bytes类型
    m=hashlib.md5()  #实例化MD5对象
    m.update(new_str)  #加密
    return m.hexdigest()  #获取结果返回

def writedata_to_data(name,email,gender,age,user_pwd):
    sql = """
    INSERT INTO register(token,name,password,email,gender,age) 
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    print(my_md5(name),my_md5(user_pwd))
    try:
        cursor.execute(sql,[my_md5(name),name,my_md5(user_pwd),email,int(gender),int(age)])
        conn.commit()
    except:
        print('插入失败')
        conn.rollback()
    
    cursor.close()
    conn.close()    

def check_user_form_name(name):
    sql = """
    SELECT * FROM register WHERE name=%s
    """
    res = cursor.execute(sql,[name])
    conn.commit()
    return res != 0


def main():

    print("""欢迎来到数据库学习月度！体验注册功能""")

    global flag
    while flag:
        user_name = input("输设置用户名(退出[Q]): ")
        # 退出判断
        if user_name != 'Q':
            if check_user_form_name(user_name) is not True:
                email = input("输设置用户邮箱: ")
                gender = input('输入用户性别(1:男,0:女):')
                age = input('输入年龄：')
                user_pwd = input("请设置密码8位，包含大小写数字(退出[Q]): ")
                if user_pwd != 'Q':
                    #检查密码是否符合规则
                    result１ = re.search('[0-9]',user_pwd)
                    result2 = re.search('[A-Z]',user_pwd)
                    result3 = re.search('[a-b]',user_pwd)
                    if result１ and result2 and result3:
                        if checkpwd(user_pwd):
                            writedata_to_data(user_name,email,gender,age,user_pwd)
                            print('用户注册成功')
                        else:
                            print('用户取消注册')
                        flag = False
                    else:
                        print('密码不符合规则',flag)
                else:
                    flag = False
            else:
                print('该用户已存在',flag)
        else:
            flag = False

if __name__ == '__main__':
    main()
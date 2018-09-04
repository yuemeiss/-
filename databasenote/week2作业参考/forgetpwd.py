import pymysql,re,hashlib

conn = pymysql.connect('localhost','root','ljh1314','week2homework',charset='utf8')
cursor = conn.cursor()

# 主程序退出标志位
flag = True

# 1、MD5加密
# 不能直接对字符串加密，要先把字符串转换为bytes类型
def my_md5(str):
    new_str=str.encode()#把字符串转换成bytes类型
    #new_str=b'%s'%str #把字符串转换成bytes类型
    m=hashlib.md5()  #实例化MD5对象
    m.update(new_str)  #加密
    return m.hexdigest()  #获取结果返回

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

def update_data_to_db(name,pwd):
    sql = """
    UPDATE register SET password=%s,isfreeze=%s WHERE name=%s
    """
    try:
        cursor.execute(sql,[my_md5(pwd),0,name])
        conn.commit()
    except:
        print('数据更新失败')
        conn.rollback()  


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
        user_name = input("输用户名(退出[Q]): ")
        # 退出判断
        if user_name != 'Q':
            if check_user_form_name(user_name):
                check_num = input('请输入邮箱验证码：')
                user_pwd = input("请输入重置密码(8位，包含大小写数字退出[Q]): ")
                if user_pwd != 'Q' and check_num == '0609':
                    #检查密码是否符合规则
                    result１ = re.search('[0-9]',user_pwd)
                    result2 = re.search('[A-Z]',user_pwd)
                    result3 = re.search('[a-b]',user_pwd)
                    if result１ and result2 and result3 and len(user_pwd)!=8:
                        if checkpwd(user_pwd):
                            update_data_to_db(user_name,user_pwd)
                            print('用户重置密码成功')
                        else:
                            print('用户取消重置')
                        flag = False
                    else:
                        print('密码不符合规则',flag)
                else:
                    print('您已取消重置密码或验证码不正确')
                    flag = False
            else:
                print('该用户不存在',flag)
        else:
            flag = False

if __name__ == '__main__':
    main()
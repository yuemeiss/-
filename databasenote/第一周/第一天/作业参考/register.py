#注册
#如何完善注册代码？可以判断用户是否已经注册？可否添加修改密码的逻辑？


# 主程序退出标志位
flag = True

def checkpwd(pwd,user_name):
    check_pwd = input('请再次输入密码(退出[Q]):')
    if check_pwd != 'Q':
        if check_pwd == pwd:
            writeInfoToFile(user_name+','+pwd+','+'0')
            return True
        else:
            print('请核实后再次输入密码')
            checkpwd(pwd,user_name)
    else:
        return False

def writeInfoToFile(data):
    f1 = open('db', 'a+')
    content = data+'\n'
    f1.write(content)
    f1.close()


def main():
    # 读文件，获取用户信息  str
    f1 = open('db', 'r')
    content = f1.read()
    f1.close()
    # 转换用户信息从str到list
    user_data_list = content.split('\n')
    user_deta_dict = {}

    # 将用户信息以字典的形式保存到列表,易空格分割后，列表最后一个元素为''
    if len(user_data_list) > 0 and user_data_list[len(user_data_list)-1]=='':
        user_data_list.pop()
    print(user_data_list)
    for user_info in user_data_list:
        user_detail = user_info.split(',')
        user_deta_dict[user_detail[0]] = {
            'name': user_detail[0],
            'pwd': user_detail[1],
            'times': user_detail[2]
        }
        # user_detail_list.append({
        #     'name': user_detail[0],
        #     'pwd': user_detail[1],
        #     'times': user_detail[2]
        # })
    print(user_deta_dict)
    
    print("""欢迎来到数据库学习月度！体验注册功能""")

    global flag
    while flag:
        user_name = input("输设置用户名(退出[Q]): ")
        # 退出判断
        if user_name != 'Q':
            if user_name not in user_deta_dict.keys():
                user_pwd = input("请设置密码(退出[Q]): ")
                if user_pwd != 'Q':
                    if checkpwd(user_pwd,user_name): 
                        print('用户注册成功')
                    else:
                        print('用户取消注册')
                    flag = False
                else:
                    flag = False
            else:
                print('该用户已存在',flag)
        else:
            flag = False

if __name__ == '__main__':
    main()
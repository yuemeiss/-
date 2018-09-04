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

# 主程序退出标志位
flag = True
# 密码错误次数(登录失败次数)
exit_flag = 0
#上一次登录的用户名
last_user_name = ''

def main():
    # 读文件，获取用户信息  str
    f1 = open('db', 'r')
    content = f1.read()
    f1.close()
    # 转换用户信息从str到list
    user_data_list = content.split('\n')
    user_detail_dict = {}

    # 将用户信息以字典的形式保存到列表,易空格分割后，列表最后一个元素为''
    if len(user_data_list) > 0 and user_data_list[len(user_data_list)-1]=='':
        user_data_list.pop()
    print(user_data_list)
    for user_info in user_data_list:
        user_detail = user_info.split(',')
        user_detail_dict[user_detail[0]] = {
            'name': user_detail[0],
            'pwd': user_detail[1],
            'lock': user_detail[2]
        }

    print(user_detail_dict)

    print("""欢迎来到数据库学习月度！体验登录功能""")
    
    global flag,exit_flag,last_user_name
    # main process
    while flag:
        user_name = input("用户名(退出[Q]): ")
        # 退出判断
        if user_name != 'Q':
            if user_name not in user_detail_dict.keys():
                print('用户名不存在')
            else:
                
                if last_user_name != user_name:
                    exit_flag = 0
                    last_user_name = user_name

                infoData = user_detail_dict[user_name]
                if int(infoData['lock']) == 1:
                    flag = False
                    print("用户已经锁定,24小时后将解锁")
                else:
                    user_pwd = input("密码: ")
                    # 校验密码
                    if user_pwd == infoData['pwd']:
                        print('登录成功') 
                        flag = False 
                    else:
                        print('密码错误') 
                        if exit_flag < 3:
                            exit_flag += 1
                            print(exit_flag)
                        else:
                            print("用户已经锁定,24小时后将解锁")
                            infoData['lock'] = '1'
                            user_detail_dict[user_name] = infoData
                            #更新数据到文件中
                            writeDataToFile(user_detail_dict)
                            flag = False  
        else:
            flag = False
 
def writeDataToFile(data):
    f = open('db','w')
    all_user_info = ''
    for key,value in data.items():
        userInfo = value['name']+','+value['pwd']+','+value['lock']+'\n'
        all_user_info += userInfo
        print(userInfo)
    
    f.write(all_user_info)
    f.close()

if __name__ == '__main__':
    main()
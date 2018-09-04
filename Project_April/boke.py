import pymysql
import redis_login,time
import forget,register

#链接mysql
mysqlconn = pymysql.connect(host='localhost',user='root',password='123456',database='user_register',charset='utf8')
#创建游标
cursor_handler = mysqlconn.cursor(cursor=pymysql.cursors.DictCursor)
#时间
fabu_time = time.gmtime()


#查看用户详细信息
def user_details(name):
    sql = '''
        select * from register where user_name = %s;
    '''

    #执行语句
    cursor_handler.execute(sql,[name])
    #获取用户信息列表
    data_mas = cursor_handler.fetchone()

    return data_mas
#发表博客
def add_boke(userName):
    print('分享生活,留住感动'.center(50,'*'))
    print('\t\t\t\t欢迎发表博客(q:退出发表):')
    boke_title = input('博客标题:')
    if boke_title == 'q':
        print('退出发表')
        return False
    boke_content = input('博客内容:\n')
    if boke_content == 'q':
        print('退出发表')
        return False
    sql = '''
        insert into boke(title,conntent,faburen,time1,userId) values(
            %s,%s,%s,%s,%s
        );
    '''
    cursor_handler.execute(sql,[boke_title,boke_content,userName['user_name'],fabu_time,userName['user_id']])

    #提交数据
    mysqlconn.commit()
#博客主页
def boke_main(page = 1):
    aa = (page - 1)*5
    if aa < 0:
        aa = 1
    sql = '''
        select * from boke order by time1 DESC limit %s,5;
    '''
    cursor_handler.execute(sql,[aa])
    #获取用户信息列表
    data_mas = cursor_handler.fetchall()

    return data_mas
def ziji(cc):
    sql = '''
        select * from boke where faburen = %s;
    '''
    cursor_handler.execute(sql,cc)
    #获取用户信息列表
    data_mas = cursor_handler.fetchall()

    return data_mas
#浏览博客评论
def boke_details(boke_id):
    # sql = '''
    #     select userName,time2,comment from boke left join commint on boke.id = commint.bokeID where boke.faburen = %s;
    # '''
    sql = '''
        select userName,time2,comment from commint where bokeID = %s;
    '''
    #根据博客Id显示博客和评论
    cursor_handler.execute(sql,[boke_id])
    #获取博客评论
    data_mas = cursor_handler.fetchall()
    return data_mas
# 评论博客
def comment(userName,bk_id):
    com_content = input('评论内容:')
    sql = '''
        insert into commint(userName,time2,comment,userSex,userID,bokeID) values(
            %s,%s,%s,%s,%s,%s
        );
    '''
    cursor_handler.execute(sql,[userName['user_name'],fabu_time,com_content,userName['user_gender'],userName['user_id'],int(bk_id)])

    #提交
    mysqlconn.commit()

    print('成功')
    ss=input('输入任何键继续')
#刷博客
def look_boke(info):
    print('博客详情'.center(50,'*'))
    user = input('博客编号:')
    # info = boke_main()
    for v,i in enumerate(info,1):
        if user == str(v):
            print('用户:%s\t\t\t编号:%s\n标题:%s\n发布时间:%s\n内容:\t%s\n'%(i['faburen'],v,i['title'],i['time1'],i['conntent']))
            #显示评论
            # print(i['faburen'])
            bk_comment = boke_details(i['id'])
            print('评论区'.center(50,'*'))
            bb = 0
            if bk_comment[0]['userName'] != None:
                for s in bk_comment:
                    bb += 1
                    print('用户名:%s\n时间:%s\n评论内容:\n\t%s'%(s['userName'],s['time2'],s['comment']))
            else:
                print('该博客没有评论')
            if u_name != i['faburen']:
                #写评论 使用全局变量 name,u_name ???
                com_user = input('是否评论此博客:1.评论 2.不评论 ')
                if com_user == '1':
                    comment(name,i['id'])
                else:
                    print('你不想发表评论')
                #如过不是用户自己增加浏览量
                add_num(bb,i['page_view'] + 1,i['id'])
    
#增加浏览量
def add_num(comment,view,bk_id):
    sql = '''
        update boke set com_num = %s,page_view = %s where id = %s
    '''
    cursor_handler.execute(sql,[comment,view,bk_id])
    
    mysqlconn.commit()
#浏览排行榜
def view_rank():
    print('最牛B排行没有之一'.center(50,"*"))
    sql = '''
        select * from boke order by com_num DESC limit 10;
    '''
    cursor_handler.execute(sql)
    #获取用户信息列表
    data_mas = cursor_handler.fetchall()
    for v,i in enumerate(data_mas,1):
        #隐藏博客内容
        content = i['conntent'][0:5:1] + '\n\t\t\t.....(选择博客(编号)查看详细信息)'
        print('用户:%s\t\t\t编号:%d\n标题:%s\n发布时间:%s\n内容:\t%s\n评论:%d 浏览:%d '%(i['faburen'],v,i['title'],i['time1'],content,i['com_num'],i['page_view']))
        print('*' * 50)
    print('='*50)
    return data_mas
#物理删除博客
def delete(boke_id):
    sql = '''
        update boke set isdelete = 1 where id = %s;
    '''
    cursor_handler.execute(sql,[boke_id])
    
    mysqlconn.commit()


def main(mm):
    print('博客主页'.center(50,'*'))
    info = boke_main(mm)
    if len(info) > 0:
        for v,i in enumerate(info,1):
            #非物理删除
            if i['isdelete'] == 0:
                #隐藏博客内容
                content = i['conntent'][0:5:1] + '\n\t\t\t.....(选择博客(编号)查看详细信息）'
                print('用户:%s\t\t\t编号:%d\n标题:%s\n发布时间:%s\n内容:\t%s\n评论:%d 浏览:%d '%(i['faburen'],v,i['title'],i['time1'],content,i['com_num'],i['page_view']))
                print('*' * 50)
    else:
        print('已经没有了....')
    print('='*50)
    return info

def menu():
    print('欢迎来到这是一个博客网'.center(50,'*'))
    print('本网站功能如下:')
    print('\t\t1.用户注册')
    print('\t\t2.用户登录')
    print('\t\t3.忘记密码')
    print('\t\t4.进入博客主页')
    print('\t\t0.退出网站')
    print('=' * 50)

def login_meun():
    print('欢迎进入这是一个博客网'.center(50,'*'))
    print('您可选择如下功能:')
    print('\t\t 1.查看博客详细信息')
    print('\t\t 2.发布博客')
    print('\t\t 3.博客排行榜')
    print('\t\t 4.查看用户信息')
    print('\t\t 5.查看自己的博客和删除')
    print('\t\t 0.退出登录')
    print('=' * 50)

# print(comment('qq123'))
# print(boke_details('qq123'))

if __name__ == '__main__':
    while True:
        menu()
        user = input('输入对应的数字进入功能')
        if user == '1':
            register.zhuce()
        elif user == '2':
            #登录验证
            u_name = redis_login.login()
            name = user_details(u_name)
            if u_name != 'q':
                flag = True
                while flag:
                    login_meun()
                    login_user = input('输入对应的数字进入功能')
                    if login_user == '1':
                        mm = 1
                        while flag:
                            info1 = main(mm)
                            page1 = input('1.下一页: 2.查看详细和评论 0.上一页')
                            if page1 == '1':
                                mm += 1
                                info1 = main(mm)
                            elif page1 == '0':
                                mm -= 1
                                info1 = main(mm)
                            elif page1 == '2':
                                look_boke(info1)
                            else:
                                print('返回')
                                break
                    elif login_user == '2':
                        add_boke(name)
                    elif login_user == '3':
                        rank_info = view_rank()
                        look_boke(rank_info)
                    elif login_user == '4':
                        print(name)
                    elif login_user == '5':
                        ziji_boke = ziji(name['user_name'])
                        for v,i in enumerate(ziji_boke,1):
                            if i['isdelete'] != 1:
                                content = i['conntent'][0:5:1] + '\n\t\t\t.....(选择博客(编号)查看详细信息）'
                                print('用户:%s\t\t\t编号:%d\n标题:%s\n发布时间:%s\n内容:\t%s\n评论:%d 浏览:%d '%(i['faburen'],v,i['title'],i['time1'],content,i['com_num'],i['page_view']))
                                print('*' * 50)
                            else:
                                print('您没有没发表博客')
                                flag = False
                                break
                        if flag:
                            look_boke(ziji_boke)
                            shan_user = input('1.删除博客 2.退出')
                            if shan_user == '1':
                                del_boke = input('博客编号')
                                for v,i in enumerate(ziji_boke,1):
                                    if del_boke == str(v):
                                        delete(i['id'])
                                        break
                    elif login_user == '0':
                        print('返回首页')
                        break
                    else:
                        print('输入有误')
        elif user == '3':
            forget.alter_passwd()
        elif user == '4':
            main(1)
        elif user == '0':
            print('大爷,常来玩哦!')
            break
        else:
            print('输入有误')

        
import redis
#导入mysql登录验证包
import denglu

#获得redis数据库  链接redis
redisConn = redis.StrictRedis('localhost',6379,0)
#redis登录 验证用户名
def r_verify(userName):
    result = redisConn.exists(userName)
    return result
#获得redis用户密码
def r_user(name):
    result = redisConn.hmget(name,'mima','status')
    info = []
    for i in result:
        info.append(i.decode())
    return info
#保存登录后的用户信息
def r_save(name,passwd):
    result = redisConn.hmset(name,passwd)
    return result
#用户状态的修改
def r_status(name):
    result = redisConn.hset(name,'status',1)
    return result
#用户验证登录
def login():
    #密码输入限定次数
    flag = 5
    #主程序运行
    main_flag = True
    while main_flag:
        print('欢迎来的登录页面'.center(50,'*'))
        print('用户须知：\n1. 用户名不存在请输入【 q 】退出登录\n2. 密码输错5次，账号将会冻结！！！')
        r_name = input('请输入用户名:')
        if r_name == 'q':
            print('退出登录')
            break
        if r_verify(r_name):
            userPasswd = r_user(r_name)
            print(userPasswd)
            if userPasswd[1] == '0':
                while flag > 0:
                    r_passwd = input('请输入密码:')
                    if r_passwd == 'q':
                        # main_flag = False
                        break
                    if userPasswd[0] == r_passwd:
                        print('登录成功')
                        main_flag = False
                        break
                    else:
                        print('密码错误,您还有%d次机会'% (flag - 1))
                        flag -= 1
                if flag == 0:
                    r_status(r_name)
                    print('该账号已经被冻结')
                    main_flag = False
                    return 'q'

            else:
                print('该账户已冻结')
        else:
            user_info = denglu.main(r_name)
            if user_info:
                print('ok')
                r_save(r_name,user_info)
                break
    print('=' * 50)
    #返回用户名  用于   登录后的操作    
    return r_name


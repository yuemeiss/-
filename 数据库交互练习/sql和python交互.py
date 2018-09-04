#要使用pymysql：实现了python与MySQL的一个交互
#pip3 list :查看你python环境中安装的第三方库
import pymysql

#创建一个mysql的链接
'''
:param host: (连接数据库的时候设置的ip)
:param user: （登录的用户名）
:param password: （登录的密码）
:param database: （设置你要操作的数据库）
:param port: 默认端口 (default: 3306)
:param charset: 设置字符集
'''
mysqlconn = pymysql.connect(host='localhost',user='root',password='123456',database='p1804',charset='utf8')
#游标（）
cursor = mysqlconn.cursor()
name = input('>>>')
age = int(input('>>>'))
sex = int(input(">>>"))
sql = '''
    insert into day1(name,age,sex) values(
       %s,%s,%s
    );  
'''
# #执行sql语句
# cursor.execute(sql)
# sql = '''
#     insert into day1 values(
#         3,'黄老师',34,1
#     )
# '''
#执行sql语句
cursor.execute(sql,[name,age,sex])

#提交数据
mysqlconn.commit()
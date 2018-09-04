# 要是用pymysql:实现了python与mysql的一个交互
# pip3 install pymysql -i https://pypi.douban.com/simple/
# pip3 list 查看你ｐｙｔｈｏｎ环境中安装的第三方库
# 如何使用?
import pymysql

#创建一个ｍｙｓｑｌ的连接
# :param host: (连接数据库的时候设置的ｉｐ)
# :param user: （登录的用户名）
# :param password: （登录的密码）
# :param database: （设置你要操作的数据库）
# :param port:  3306　（设置端口号）
# :param charset: Charset you want to use.（设置你想使用的字符集）
# mysqlconn = pymysql.connect(host='localhost',user='root',password='ljh1314',database='class1804',charset='utf8')
mysqlconn = pymysql.connect('localhost','root','ljh1314',database='class1804',charset='utf8')

#创建游标cursor
#cursor_handler = mysqlconn.cursor()
#默认不设置cursor(cursor='不设置')，会返回下面类型的数据，
((3, '王老师'), 
(4, '赵老师'), 
(5, '黄老师'), 
(6, '黄老师2'), (7, '李老师'), 
(10, ''), 
(12, '李'))

cursor_handler = mysqlconn.cursor(cursor=pymysql.cursors.DictCursor) 
#设置pymysql.cursors.DictCursor将对应的行的数据以字典的形式返回，如果是多个直接放在一个列表中
[{'name': '王老师', 'id': 3}, 
{'name': '赵老师', 'id': 4}, 
{'name': '黄老师', 'id': 5}, 
{'name': '黄老师2', 'id': 6}, 
{'name': '李老师', 'id': 7}, 
{'name': '', 'id': 10},
{'name': '李', 'id': 12}]

# id = int(input('输入ｉｄ'))
# teacher_name = input('输入名称')

##sql注入的问题
# sql = """
# select * from users where name=%s and password=%s
# """ % (name,mima)

# print(sql)
# select * from users where name=li or password='' --  and password=123

# #增加数据
sql = """
    INSERT INTO teachers(name) 
    VALUES ('黄老师')
"""
# sql = """ INSERT INTO teachers(id,name) VALUES ('%s','%s') """

#删除数据数据
# sql = """
#     DELETE FROM teachers WHERE id=%s and name=%s
# """

#跟新数据数据
# sql = """
#     UPDATE teachers SET name=%s WHERE id=%s
# """

#查找
# sql = """
#    SELECT * from teachers WHERE id=%s 
# """
# sql = """
#    SELECT * from teachers; 
# """

#执行sql语句
result = cursor_handler.execute(sql)
print(cursor_handler.lastrowid)

# print(result)#受影响的行
# print(cursor_handler.fetchone())#获得一条查找结果
# print(cursor_handler.fetchall())#获得所有查找结果


#提交数据
mysqlconn.commit()

#总结一下：
# １．创建连接
# conn = pymysql.connect(参数....)
# 2.创建游标
# cursor = conn.cursor()
# 3.写ＳＱＬ语句
# sql = """
# insert|delete|update|select|alter .......
# """
# 4.执行
# cursor.execute(sql,[参数,参数,....])
# result = cursor.execute(sql,[参数,参数,....])
# result:返回受影响的行
# 5.提交
# conn.commit()
# 6.关闭
# cursor.close() #关闭游标
# conn.close()　#关闭连接

# 注意：
# 假如我们要做的是查询
# cursor.fetchone() 获取查询的第一条结果
# cursor.fetchall() 获取查询的所有结果

# 设置：
# conn.cursor(cursor=pymysql.cursors.DictCursor)
# 设置pymysql.cursors.DictCursor将对应的行的数据以字典的形式返回，如果是多个直接放在一个列表中

#cursor_handler.lastrowid 返回最后插入数据的id 



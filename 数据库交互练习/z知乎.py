import pymysql

#创建链接
mysqlconn = pymysql.connect('localhost','root','123456','zhihu',charset='utf8')

#创建游标 　默认返回元祖　这里是以字典的形式返回
mycursor = mysqlconn.cursor(cursor=pymysql.cursors.DictCursor)
def aa():
    print('查找某个用户提出了哪些问题')
    user = input('用户名')

    sql = '''
        select user_z.name,question.ask_question from user_z inner join question on user_z.id = question.user_id where name = %s
    '''

    #执行ｓｑｌ语句　返回的结果是　ｉｎｔ　结果的数量
    mycursor.execute(sql,[user])
    #获得列表数据
    result = mycursor.fetchall()
    print(result)
    #提交数据
    mysqlconn.commit()
def bb():
    print('２．根据回答查找出哪个用户回答的，关联出用户信息')
    user_ans = input('回答：')
    sql = '''
        select user_z.* from answer inner join user_z on answer.user_id = user_z.id where answer_que like %s;
    '''

    #执行ｓｑｌ语句　返回的结果是　ｉｎｔ　结果的数量
    mycursor.execute(sql,[user_ans])
    #获得列表数据
    result = mycursor.fetchall()
    print(result)
    #提交数据
    mysqlconn.commit()
#bb()
def cc():
    print('查找某个用户回答了哪些问题')
    user = input('用户名')

    sql = '''
        select user_z.name,question.ask_question,answer.answer_que from user_z inner join question on user_z.id = question.user_id inner join answer on user_z.id = answer.user_id where name = %s
    '''

    #执行ｓｑｌ语句　返回的结果是　ｉｎｔ　结果的数量
    mycursor.execute(sql,[user])
    #获得列表数据
    result = mycursor.fetchall()
    print(result)
    #提交数据
    mysqlconn.commit()
#cc()
def dd():
    print('查找某个用户回答了哪些问题')
    user = input('用户名')

    sql = '''
        select user_z.name,question.ask_question,answer.answer_que from user_z inner join question on user_z.id = question.user_id inner join answer on user_z.id = answer.user_id where name = %s
    '''

    #执行ｓｑｌ语句　返回的结果是　ｉｎｔ　结果的数量
    mycursor.execute(sql,[user])
    #获得列表数据
    result = mycursor.fetchall()
    print(result)
    #提交数据
    mysqlconn.commit()
#第四题
#select group_concat(question.ask_question) as title,user_z.name as userName from user_z inner join question on user_z.id = question.user_id group by user_z.name;
#第五题
#select user_z.*,count(1) as answer_1 from user_z inner join answer on answer.user_id = user_z.id  group by user_z.id having count(*) > 2;
#第六题
#select user_z.*,count(1),group_concat(question.ask_question) from user_z inner join question on question.user_id = user_z.id  group by user_z.id having count(*) > 2;

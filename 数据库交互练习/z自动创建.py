# -*- coding:utf8 -*-
import pymysql as c
from faker import Faker
import random
import sys
import datetime
from concurrent.futures import ProcessPoolExecutor  #加快速度的一个线程

#创建一个用户表
#create table usersinfo( use_id int auto_increment, name varchar(20) not null, gender char(5) not null, age int, brithday char(10), id_type varchar(15) default '身份证', id_card char(18), phone char(11), email varchar(30), native_place varchar(60), address varchar(255), join_time char(10), hobby text, primary key(use_id) );


mysqlConn = c.connect(user='root',password="123456",database='p1804')
cursor = mysqlConn.cursor()

fake = Faker("zh_CN")

def get_native_place(address, key="县市"):

    return [address[:address.index(k)+1] for k in key if k in address][0]

def gen_stu_obj():
    #随机生产一个地址
    address = fake.address()
    #从地址里面截取
    native_place = get_native_place(address)
    #随机生成一个出生日期
    brithday = fake.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=30)
    #随机生成一个邮箱
    email = fake.ascii_free_email()
    #随机生辰一个姓名
    name = fake.name()
    #随机生成一个电话号码
    phone = fake.phone_number()
    id_type = "身份证"
    #随机生成一个年龄
    age = random.randint(20,30)
    #随机产生一个身份证号
    id_card = fake.ssn(min_age=20, max_age=30)
    #产生一个时间
    join_time = fake.date_between(start_date="-2y", end_date="today")
    #生成一个座右铭
    hobby = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    #随机筛选男或者女
    gender = random.choice(["男","女"])
    # print(address,native_place,birthday,email,name,phone,age,id_code,join_time,hobby,sex)

    sql = 'insert into usersinfo(use_id,name,gender,age,brithday,id_type,id_card,phone,email,' \
    'native_place,address,join_time,hobby) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, (
    None, name, gender, age, brithday, id_type, id_card, phone, email, native_place, address, join_time, hobby,))

    mysqlConn.commit()



if __name__ == "__main__":

    a=datetime.datetime.now()
    gen_stu_obj()
    for _ in range(100000):
        gen_stu_obj()
        b=datetime.datetime.now()
    # print(b-a)
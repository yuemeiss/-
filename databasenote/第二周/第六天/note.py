１．回顾
关于自增的扩展：
可以设置设置auto_increment一个起始值
> ALTER TABLE 表明 AUTO_INCREMENT=180460

改变自增的步长
1.会话级别：
show session variables like 'auto_inc%';

+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 1     |
| auto_increment_offset    | 1     |
+--------------------------+-------+

修改步长：
SET SESSION auto_increment_increment=2(设置步长的值)


2.基于全局的设置：
show global variables like 'auto_inc%';

+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 1     |
| auto_increment_offset    | 1     |
+--------------------------+-------+

修改步长：
SET global auto_increment_increment=2(设置步长的值)

总结：
一个表里面只能有一个自增，并且一般都会设置主键为自增，
不然会报错：
ERROR 1075 (42000): Incorrect table definition; there can be only one auto column and it must be defined as a key

## 创建计算字段
创建的计算字段原本并不存在我们的表里面。我们通过ｍｙｓｑｌ的函数
或者算术运算得到一个结果，我们把这个结果起一个别名，这个字段就是我们
创建的计算字段。

#加密函数
PASSWORD('')
MD5('')

#创建计算字段
IF(x1,v1,v2) : x1:表示条件，如果满足返回v1,否则返回v2
IFNULL(v1,v2) :if v1 not NUll,返回v1,否则返回v2
CASE WHEN 条件　THEN 结果１　ELSE 结果２ END:当遇到某种条件，
当ＷＨＥＮ后面的条件满足，返回THEN后面的结果１，否则返回结果２.

#还有数字函数、字符串函数、日期、时间函数

### 三范式　、Ｅ-R
三范式
1NF:列不可再分（尽量细的去拆分每一列）
2NF:1.一个表必须要有一个主键（这个主键可以由单个列，或者多个列组成）
　　２．非主键的列，必须完全依赖于主键，而不是及部分依赖于键
3NF：在第二范式的基础上，不能存在传递依赖，非主键的列，必须直接依赖
于主键，而不能存在传递依赖的关系。

E-R模型
Ｅ：Entry 表示实体，其实就是根据某一个事物的体征，添加描述信息，我们将
这些描述信息添加在一个表（ｔａｂｌｅ）里面，那么这个表就相当于一个实体。
Ｒ：Ｒelationship 关系，在这里其实就是指的表与表之间的关系
一对一：个人信息与身份证
　　个人信息表
　　CREATE TABLE USER(
    id int auto_increment,
    name varchar(10) not null, 
    idcard int not null,
    primary key(id),
    #外键：
    CONSTRAINT FK_IDCARD(起个名字) FOREIGN KEY(idcard) REFERENCES IDENTIFITY(id)
);
　　身身份证表ID
  CREATE TABLE IDENTIFITY(
   id int auto_increment,
   id_num varchar(50) not null,
   primary key(id) 
  );
一对多：班级与学生
  学生表
  CREATE TABLE studnets(
      stu_id int auto_increment,
      stu_name varchar(20) not null,
      #班级
      primary key(stu_id)
  );
  班级表
  CREATE TABLE grade(
      cls_id int auto_increment,
      cls_name varchar(20) not null,
      cls_desc varchar(255) not null,
      cls_student_num int default 0,
      primary key(cls_id)
  );
  
多对多：选课

学生表
  CREATE TABLE studnets(
      stu_id int auto_increment,
      stu_name varchar(20) not null,
      #班级
      primary key(stu_id)
  );

课程
　　CREATE TABLE courses(
    cour_id int auto_increment,
    cour_name varchar(20) not null,
    primary key(cour_id)
)


如何设置外键？
1.首先要找表与表之间的关系。
2.班级表（id,name,主键为id）
3.学生表（id,name,主键id,clsid(外键)->班级表中的班级的主键）
创建学生表必须要有班级表
创建班级表
CREATE TABLE classes(
    id int auto_increment,
    name varchar(20) not null,
    primary key(id)
)engine = innodb default charset=utf8

CREATE TABLE students(
    id int auto_increment,
    name varchar(20) not null,
    clsid int,
    primary key(id),
    constraint FK_CLSID foreign key(clsid) references classes(id)
);

#删除外键
ALTER TABLE students drop foreign key FK_CLSID;

#添加外键
ALTER TABLE student ADD constraint FK_CLSID foreign key(clsid) references classes(id);









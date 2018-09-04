mysql服务相关
sudo service mysql start
sudo service mysql stop
sudo service mysql restart

客户端连接
mysql -u 用户名 -p

mysql -h IP -u 用户名 -p

1.创建数据库开始
CREATE DATABASE IF NOT EXISTS 数据库名称 （这样会使用mysql默认的字符集）

2.创建指定字符集的数据库
CREATE DATABASE IF NOT EXISTS 数据库名称 CHERSET=utf8/gbk/gb2312 .....

3.修改数据库
ALTER DATABASE IF NOT EXISTS 数据库名称 CHARSET=字符集

4.删除数据库
DROP DATABASE 数据库名

5.查看当前选择的数据库
SELECT DATABASE()

6.切换数据库
USE 数据库名

9.查看数据库中的表
show tables;

表的创建
数据库的三大引擎Innodb、MYSIAM、MEMARY
数据库字段：
三大类：
字符串：char、varchar、longtext、mediumtext、text
日期：date、year、time、datetime、timestamp....
数值：int、smallint、tinyint、mediumint

#约束：
not null：设置指定的列不能为nill ！=> 空字符串
default : 给指定的列设置一个默认值，如果插入数据的时候
不给当前列设置值，就会使用默值，如果设置了值，就会使用
设置的值。
primary key:主键，不能为null、唯一
unique：唯一，可以为null
foreign key:外键，外键是某一个表的主键，不为null，
加强表与表之间的数据联系（关系）

属性：
auto_increment 自增
可以指定指定步长和起始值
会话级步长：
set session auto_increment_increment = 步长
set session auto_increment_offset=10; 会话级别的起始值

全局的步长设置
set global auto_increment_increment = 步长
set global auto_increment_offset=10;全局级别的起始值

#给一个表指定一个起始的自增的值
ALTER　TABLE 表名　auto_increment　=　起始值
#一个表里面自能有一个自增，并且都是给主键设置自增.
ERROR 1075 (42000): Incorrect table definition; there 
can be only one auto column and it must be defined as a key

CREATE TABLE IF NOT EXISTS 表名（
字段名　类型　约束　属性（自增）,
字段名　类型　auto_increment primary key,
字段名　类型　not null unique key,
字段名　类型　not null default 默认值,
primary key(列名)/primary key(列名,列名)
unique key(列名)/unique key(列名、列名)
constraint FK_ID foreign key(列名)　references 主表(primary key)),
constraint FK_XX foreign key(XX)　references 主表(primary key))
)engine=数据库引擎　default charset=字符集（utf8 ....）;

#查看表的创建语句
show create table tablename;
show create table tablename \G;

#查看表的结构
DESC tablename;

#修改表
ALTER TABLE 表名 charset=...;
#（重命名）
RENAME TABLE 旧表名　TO 新表名;
#修改表名
ALTER TABLE 旧表名　RENAME　AS 新表名;
#修改表中的字段旧字段名
ALTER TABLE 表名　change 字段名　新字段名　类性　约束　属性;
#在不改变的情况下修改（类型、约束等）
ALTER　TABLE 表名 change modify 字段名 类型 约束 属性;
#添加新的列
ALTER TABLE 表名 ADD 字段名　类性　约束　属性;
#删除某一列
ALTER TABLE 表名 DROP IF EXISTS 字段名;
#删除表
DROP TABLE 表名;

CURD
增：
#全列插入（注意：我们插入的数据顺序必须要跟列对应）
INSERT INTO tablename VALUES(值，值，值);
#非全列插入（指定要插入哪些列）
INSERT INTO tablename(列,列,列) VALUES(值，值，值);
#多行插入
INSERT INTO tablename(列,列,列) VALUES(值，值，值),(值，值，值),(值，值，值),...;

删：
#删除指定数据
DELETE FROM tablename WHERE 条件;
#删除全部数据
DELETE FROM tablename;

改：
#修改表中某一列的全部值(不要这么去做)
UPDATE tablename SET 列名=值;
#根据条件修改数据
UPDATE tablename SET 列名=值 WHERE 条件;
UPDATE tablename SET 列名=值,列名=值,.. WHERE 条件;

查：
select * from tablename;
select 列,列,列,... from tablename;

#去重DISTINCT
select distinct 列 from tablename;

#where
select * from tablename where 列=值;
select * from tablename where 列>值;
select * from tablename where 列<值;
select * from tablename where 列<=值;
select * from tablename where 列>=值;
# 不等于
select * from tablename where 列<>值;
select * from tablename where 列!=值;
#is null
select * from tablename where 列 is null;
#or
select * from tablename where 列=值 or 列!=值;
#in
select * from tablename where 列 in(值,值,值,值,..);
#and(同时满足条件)
select * from tablename where 列=值 and 列!=值;
#not
select * from tablename where 列 not in(值,值,值,值,..);
select * from tablename where 列 not is null;
#BETWEEN...AND... 在某一个范围（左右都闭合）
select * from tablename where 列 between 值 and 值;

#排序 order by
#升序（ASC）
select * from tablename order by 列 （默认是升序）
select * from tablename order by 列 ASC;
#降序（DESC）
select * from tablename order by 列 DESC;

#多个列做排序
select * from tablename order by 列 (ASC|DESC),列 (ASC|DESC);

#聚合函数
COUNT(*)|COUNT(1):计算所有行
AVG():计算列的平均值
SUM():求和，计算列的值的和
MAX():计算列的最大值
MIN()：计算列的最小值

#通配符
%:匹配任意字符，任意次数
_:匹配任意字符，必须有且仅有一次
一般跟LIKE配和使用
select 列,列 from tablename where 列 like '条件%'
select 列,列 from tablename where 列 like '条件_'

正则：
. \d \D \s \S \w \W [0-9] [0-56-9] [^0-9] ^[0-9]
$ ^ \A \Z 

* + ? {m,n} {n} {n,} {,m}

非贪婪： *? +? ?? {m,n}?

| () (|) (?P<name1>) (?P=name1) \num

python re模块

complie 
match：从起始位置匹配，如果开头就不符合直接返回None，如果匹配到值
立即返回结果，单次匹配，取值使用group()
search:从头开始匹配，在整个字符串中查询，只要又符合规则的就立即返回，
单次匹配，如果没有符合规则的就返回None
findall：在整个串中，返回所有符合规则的结果，是一个列表
sub:替换
split：分割字符串、返回列表
finditer：跟findall功能一致，返回结果有区别，返回的是一个可迭代的对象
r:原始字符串
\:转义符

##分组：
group by
#单个去做分组，只能返回分组的名称
#group by 跟聚合函数使用
select count(1),列 from tablename group by 列;
select count(1),列,列 from tablename group by 列,列;
#group_concat()
select count(1),列,group_concat(非分组的某个列) from tablename group by 列;
#with rollup
select count(1),列 from tablename group by 列 with rollup;

#HAVING：过滤分组
HAVING后面跟条件，过滤分组的结果
select count(1),列 from tablename group by 列 HAVING count(1) > 2;

#LIMIT
select * from tablename limit 6;
select * from tablename limit 7,6;

总结：
select 列,...
from tablename
where 条件
group by 分组
having 过滤分组
order by 排序(ASC|DESC)
limit 限制返回条数（设置起始位置和返回条数）

#创建计算字段
使用函数或者运算符去计算出一个结果，把这个结果作为一个列返回
select sum(age)/count(1) as avg_age from tablename
select 函数() as 别名 from tablename
数学函数
字符串函数
日期函数
条件判断函数(
    IF(条件,r1,r2)、
    IFNULL(r1,r2)、
    case when 条件 then 结果1 else 结果2 end
    )
加密函数 （PASSWORD()、MD5()）

表的设计：
范式：
1nf:列不可再分
2nf:一个表必须要有一个主键（可以由单个列或多个列构成），
非主键的列必须完全依赖于主键，而不是部分依赖于主键
3nf:非主键的列,必须直接依赖主键，不能出现传递关系
（非主键的列A,依赖与非主键的列B,非主键的列B依赖于主键）

E-R模型：
E：实体，一个实体其实就是指的一张表
R：关系，表与表之间的一个数据的联系
一对一：
一对多：
多对多：


















































#　目的：
# 创建一个用木并且给用户设置权限和密码
grant 权限 on 数据库.表名 to '用户名'@'主机ip' identified by '密码'
grant select on class1804.usersinfo to 'zhangsan'@'%' identified by '123456'
grant select,delete,alter,... on class1804.usersinfo to 'zhangsan'@'%' identified by '123456'
超出权限报错：
ERROR 1142 (42000): UPDATE command denied to user 'zhangsan'@'localhost' for table 'usersinfo'

#用户拥有某个表的所有权限
grant all privileges on class1804.usersinfo to '用户名'@'主机ip' identified by '密码'

#用户拥有某个数据库下所有表的所有权限
grant all privileges on class1804.* to '用户名'@'主机ip' identified by '密码'
#用户拥有某个数据库下所有表的可读（查找）
grant select on class1804.* to '用户名'@'主机ip' identified by '密码'

#在哪里查看创建的用户
客户端登录后在ｍｙｓｑｌ这个数据库下有一个ｕｓｅｒ表
select user,host,auth....._string from user;

#第二中方式创建用户给用户设置权限
１．先创建用户，在设置权限
create user '用户名'@'ip' identified by '密码'
再高版本下mysql的版本为８.0.1０以上密码是有安全要求的（必须是8位，由大写字母，小写字母、
数字、特殊字符）
２．再设置权限
grant 权限　on 数据库.表　to '用户名'@'%';
mysql -h127.0.0.1  -u ldd -p
Enter password: 密码

mysql> #先创建一个用户
mysql> CREATE USER 'ldd'@'127.0.0.1' identified by 'Abcd123*';
mysql> #设置权限
mysql> GRANT ALL PRIVILEGES on *.* to 'ldd'@'127.0.0.1';
# 刷新权限
mysql> flush privileges;
#查看权限
mysql> SHOW GRANTS for 'ldd'@'127.0.0.1';

注释：
精确到某个表：on 数据库.表名
精确到某个数据库：on 数据库.*
拥有所用ｍｙｓｑｌ下所有数据库的所有表：on *.*

要设置所有权限：grant all privileges on *.* to 'user'@'ip' identified by 'mima'

#删除某一个用户
drop user 'ldd'@'127.0.0.1';

#重新给用户命名
mysql> RENAME user 'zhangsan'@'%' to 'zhangsanfeng'@'%';

#撤销权限
mysql> REVOKE SELECT ON class1804.usersinfo from 'zhangsanfeng'@'%';

INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, 
SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE 

#总结一下：
１．创建用户　create user '用户名'@'ip' identified by '密码'
２．分配权限　grant 权限　on 数据库.表　to '用户名'@'ip'
３．查看权限 show grants for '用户名'@'ip'
４．刷新一下权限 flush privileges
５．给用户重命名 rename user olduser to newuser
６．撤销权限 revoke 权限　on 数据库.表 from '用户名'@'ip'
７．可以删除用户 drop user '用户名'@'ip'
８．查看当前用户：select user();
# 创建一个用木并且给用户设置权限和密码
grant 权限 on 数据库.表名 to '用户名'@'主机ip' identified by '密码'


#数据库的备份
mysqldump -u 用户名　-p 数据库 表 > 备份路径
#备份数据库
ljh@ljh-Inspiron-7370:~$ mysqldump -u root -p class1804 usersinfo > ~/桌面/dump/usersinfo.sql
DROP TABLE IF EXISTS `teachers`;　#先删除

CREATE TABLE `teachers` (　　　#再创建
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;　#上锁

INSERT INTO `teachers` VALUES (1,'黄老师'),(2,'张老师'),(3,'王老师'),(4,'赵老师');

UNLOCK TABLES;　#解锁


#恢复数据
mysql -u root -p class1804 (不需要指定表名))< ~/桌面/dump/goods.sqlEnter password: 

#备份整个数据库（会把数据库中的所有的表以及数据都备份）
mysqldump -u root -p 数据库名 > 指定备份数据的路径

#恢复（注意：如果要备份的是数据库，这个时候先创建数据库，然后才能完成备份）
mysql -u root -p tianmao < ~/桌面/dump/tianmao.sql

#一次备份多个数据库
mysqldump -u root -p --databases jing_dong bc1 > ~/桌面/dump/dongbc1.sql

#备份所有的数据库
mysqldump -u 用户名 -p --all-databases --lock-all-tables > ~/桌面/master_db.sql

u ：用户名
p ：示密码
--all-databases ：导出所有数据库
--lock-all-tables ：执行操作时锁住所有表，防止操作时有数据修改
~/桌面/master_db.sql :导出的备份数据（sql文件）位置，可自己指定


#注释：假如要恢复所有的数据库，这个时候不需要自己在一个一个创建数据库，
# 我们在恢复的时候，会自动创建
mysql -u 用户名 -p  <  ~/桌面/master_db.sql

#只备份结构不备份数据　-d
mysqldump -u root -p -d jing_dong > ~/桌面/dump/jong.sql

mysqldump -u root -p -d jing_dong  tablename > ~/桌面/dump/jong.sql


#mysql 如何与ｐｙｔｈｏｎ交互
#连接数据库，输入账号密码
#mysql -> user 核查你输入的账号密码
#正确，连接成功

#use 数据库名称
#做增、删改、查、－> 创建SQL语句。



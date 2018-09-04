1.对表数据进行增删改查（curd）
1.insert into (增)
CREATE DATABASE class1804 charset=utf8;
USE class1804;

　　 （１）完全插入
    INSERT INTO studentinfo values(180401,'老王',20,1,'18086457300');
　　 SELECT * FROM studentinfo;
    （２）不完全插入
    INSERT INTO studentinfo(student_id,student_name,age,gender,phonenum) values(180401,'老王',20,1,'18086457300');
    INSERT INTO studentinfo(student_id,student_name,age,gender) values(180401,'老王',20,1);
　　 （３）多行插入
    INSERT INTO studentinfo(student_id,student_name,age,gender) values(180401,'老王',20,1),(180401,'老王',20,1),(180401,'老王',20,1);

2.删除（delete）
    (1)根据条件删除
    　　DELETE FROM studentinfo WHERE student_id=180401;
    (2)删除表中的所有行
    　　DELETE FROM studentinfo;
3.修改、跟新（UPDATE）
    (1)跟新单个字段（列）
    UPDATE studentinfo SET student_name='成风'　WHERE student_id=180402;
    (2)跟新多有行（将studentinfo中的所有）
    UPDATE studentinfo SET student_name='成风';
    (3)跟新多个字段（列）
    UPDATE studentinfo SET student_name='成风',age=20　WHERE student_id=180402;

4.将一个表中的列复制到另一个表中(将studentinfo表中的student_name，student_id)列的数据插入到studentinfo1对应的列中
　　INSERT INTO studentinfo1(student_name,student_id) SELECT student_name,student_id FROM studentinfo;

５.查询
   SELECT * FROM studentinfo(表名)
   SELECT * FROM studentinfo(表名) WHERE student_id=180402;
   SELECT age FROM studentinfo(表名) WHERE student_id=180402;
   SELECT age,student_name,gender FROM studentinfo(表名) WHERE student_id=180402;

6.使用ＤＩＳＴＩＮＣＴ去重重复的结果，返回不重复的列的值
　　SELECT DISTINCT age FROM studentinfo(表名);

７．使用完全限定的方式查找

　　SELECT * FROM 数据库名.表名;
　　SELECT 表名.列,表名.列,.... FROM 数据库名.表名;
8 .WHERE条件查询和算术运算符
   = 等于
   SELECT * FROM studentinfo WHERE age=22;
   <> 不等于
   SELECT * FROM studentinfo WHERE age<>22;
   != 同样表示不等于
   SELECT * FROM studentinfo WHERE age!=22;
   < 小于
　　<= 小于等于
　　> 大于
　　=> 大于等于
　　BETWEEN ... AND ...(包含边界值)
　　SELECT * FROM studentinfo WHERE age BETWEEN 20 AND 30;
   is null：判断某一列的数据如果为ＮＵＬＬ，则返回该记录
   SELECT * FROM studentinfo WHERE phonenum is null

   AND符号在ＳＱＬ语句中可以连接查询条件，那么查询的数据必须要满足所有的条件
　　SELECT student_name FROM studentinfo WHERE student_id>=180403 AND age>22 AND phonenum is null;
　　OR符号在ＳＱＬ语句中同样可以可以连接查询条件，只要满足其中某一个条件，就会返回。
　　SELECT student_name,age,student_id FROM studentinfo WHERE student_id>180403 OR age=30;

　　注意：AND和OR同时使用的时候，我们AND的优先级要高于OR,正确的写法如下：
　　(student_id=180401 OR age=19)　相当于一个整体条件。
   SELECT * from studentinfo WHERE (student_id=180401 OR age=19) AND age>22;

   IN(条件１,条件２，条件３)：ＳＱＬ查询语句中只要符合ＩＮ的（）中的某一个条件，就返回记录（行）
   等价与ＯＲ的用法，更加简洁了。
   SELECT * FROM studentinfo WHERE student_id IN(180401,180404);
   =>
   SELECT * FROM studentinfo WHERE student_id student_id=180401 or student_id=180404;

  　NOT:表示取反
  　SELECT * FROM studentinfo WHERE student_id NOT IN(180401,180404);
  　SELECT * from studentinfo WHERE phonenum is  NOT null;
   SELECT * from studentinfo WHERE not age>22;

　　通配符　％:可以匹配所有字符任意次数（０次或多次），一般跟LIKE配合使用
   SELECT * FROM studentinfo WHERE student_name LIKE '%牛%';
   SELECT * FROM studentinfo WHERE student_name LIKE '%牛';

   _ 下划线通配符：可以匹配任意字符有且只有一次(个)，一般跟LIKE配合使用
   SELECT * FROM studentinfo WHERE student_name LIKE '%牛_';


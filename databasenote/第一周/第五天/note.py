1.排序
ORDER BY

ASC：升序，默认的情况下就是升序
DESC：如果要降序，指明方向为ＤＥＳＣ
1.单列排序
SELECT * FROM 表名　ORDER BY 列 (ASC|DESC)

2.添加条件根据查询结果排序
SELECT * FROM 表名 WHERE 条件　ORDER BY 列 (ASC|DESC)

3.多列排序
SELECT * FROM 表名 WHERE 条件　ORDER BY 列 (ASC|DESC),列 (ASC|DESC)
# 主要：当根据多列进行排序的时候，会先根据第一个条件进行排序，
# 如果排序结果有相同的值，然后再根据第二个排序条件进行排序

4.如果你要排序的列是中文，我们先要将排序的列指明为ＧＢＫ编码，然后再排序
SELECT * FROM stu WHERE age !=0  ORDER BY convert(name USING gbk);


# 限定查询

１．如果LIMIT 后面只跟了一个数字，表示限制返回多少条，并且从第一条开始。
SELECT * FROM studentinfo LIMIT 6;　=>　SELECT * FROM studentinfo LIMIT 0,6;
　
１．如果LIMIT 后面只跟了两个数字，第一个数字表示偏移量（不包含当前数字对应的这一行），后一个数字表示限制返回多少条。
SELECT * FROM studentinfo LIMIT 6,6;

# 从第６条开始查询，返回６条结果。不包含第六条。返回（７条－１２条）

# 我们如何去实现一个分页功能,输入对应的页码m，每一页返回２０条数据，
SELECT * FROM studentinfo LIMIT (m-1)*20,20

#取年龄最大的
SELECT * FROM studentinfo ORDER BY age DESC LIMIT 1;

#取年龄最小的
SELECT * FROM studentinfo ORDER BY age LIMIT 1;

聚合函数
ＡＶＧ:求某一列平均值
ＣＯＵＮＴ:统计总行数
ＳＵＭ：计算列总和
ＭＩＮ:求某一列的最小值
ＭＡＸ：求某一列的最大值

#ＡＶＧ:求某一列平均值
SELECT AVG(age) FROM studentinfo;

#ＡＶＧ:求某一列平均值(起一个别名)
SELECT AVG(age) as avgage  FROM studentinfo;

SELECT MIN(age) as minage  FROM studentinfo;

SELECT MAX(age) as maxage  FROM studentinfo;

SELECT COUNT(*)  FROM studentinfo;

SELECT SUM(age)  FROM studentinfo;

SELECT SUM(age),AVG(age),MIN(age),MAX(age) FROM studentinfo;

#DISTINCT去重，只计算不同的值。
SELECT SUM(DISTINCT age) FROM studentinfo;

#添加条件，进行聚合函数的计算
SELECT COUNT(gender) FROM studentinfo WHERE gender=1;

SELECT COUNT(gender) FROM studentinfo WHERE gender=0;

SELECT (sum(age)+avg(age)+min(age))/3  FROM studentinfo WHERE gender=0;

SELECT (sum(shuxue)+sum(yuwen)+sum(yingyu))/3 FROM studentinfo WHERE user_id = 10040


## 分组　GROUP BY,单单只是用分组没有意义

#分组跟聚合函数的使用，统计每一个分组下有多少人（有多少条记录）
SELECT count(*) as total,age FROM studentinfo GROUP BY age;

#统计分组的信息
SELECT count(*), avg(age),min(age),sum(age),gender FROM studentinfo GROUP BY gendeｏｕ

#group by 与　group_concat(列)
group_concat(字段名)可以作为一个输出字段来使用，
表示分组之后，根据分组结果，使用group_concat()来放置每一组的某字段的值的集合
SELECT gender,group_concat(student_name),group_concat(age) FROM studentinfo GROUP BY gender;

group by + with rollup
在最后新增一行，来记录当前列里所有记录的总和
SELECT gender,count(*) FROM studentinfo GROUP BY gender with rollup;

HAVING:根据条件过滤结果，
HAVING跟WHERE功能一致，他们的区别：ＷＨＥＲＥ是根据条件筛选结果（行）。
HAVING同样是根据条件筛选结果，不过它是在已有结果的基础之上再进一步筛选（组）。

# 如何使用？
#使用ｈａｖｉｎｇ过滤分组，每个分组下的记录（行）大于２，才返回
SELECT count(*),age FROM studentinfo GROUP BY age HAVING count(*) >2;

SELECT count(*),age,gender FROM studentinfo GROUP BY age,gender HAVING gender =1 ;

#跟order by 配合使用
SELECT count(*),age,gender FROM studentinfo GROUP BY age,gender HAVING gender=1 ORDER BY age DESC;
# HAVING后跟多条件筛选分组
SELECT count(*),age,gender FROM studentinfo GROUP BY age,gender HAVING gender=1 AND age > 67 ORDER BY age DESC;
#限定条件返回结果（LIMIT）
SELECT count(*),age,gender FROM studentinfo GROUP BY age,gender HAVING gender=1 ORDER BY age DESC LIMIT 2,2;

查询语句的顺序：
SELECT 
列，列
FROM
表名
WHERE
条件
GROUP BY
列,列
HAVING
条件
ORDER BY
列　(ASC|DESC)
LIMIT start,count






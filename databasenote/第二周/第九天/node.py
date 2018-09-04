1.索引：加快查找，可以理解为创建了一个索引目录
每次查找会在目录中找到位置.（例子：字典）
目的：
　　约束（主键、唯一约束）
　　加速查找
分类：
　　主键索引：
　　唯一索引：
　　普通索引：
　　联合索引(多列组合成的)：顺序（最左前缀匹配）
　　　　　　普通的列组成　index 索引名称　(列１，列２，列３)
　　　　　　主键联合索引　primary key(列１,列２,...)
          唯一联合索引　unique key(列１，列２)

在已经存在的表中添加索引：
ALTER TABLE tablename ADD primary key()
ALTER TABLE tablename ADD unique key()

添加普通索引：
　create index 索引名称　on tablename(列,..)
添加一个唯一索引
　create unique index 索引名称　on tablename(列,..)
删除索引：
　drop index 索引名称　on tablename
 drop unique index 索引名称　on tablename

如何修改索引名称？？？？？？

对于MySQL 5.7及以上版本,可以执行以下命令
ALTER TABLE tbl_name RENAME INDEX old_index_name TO new_index_name

对于MySQL 5.7以前的版本，可以执行下面两个命令(先删除再添加)：
ALTER TABLE tbl_name DROP INDEX old_index_name
ALTER TABLE tbl_name ADD INDEX new_index_name(column_name)


索引根据搜索引擎分类：
设置索引：
　　会额外生成一个数据文件（索引文件）
　　快

不设置子索引的区别：
　　从上网下依次查找
　（慢）

hash 索引：MEMＡＲＹ存储引擎
　　索引表（）
　　根据索引列生成一个ｈａｓｈ值，并且记录当前列在表中的地址
　　这个ｈａｓｈ表的索引存储顺序跟我们的表的顺序不一致
　　查询单个数据较快。

btree 索引：(二叉树算法)：几乎支持所有的存储的引擎
　　查找速度相对快

两个名称的概念：

覆盖索引：直接从索引文件中拿出对应的值，不再表中查找。
这里（name、age都是索引列）
select name,age from tablename where name='张三' and age=60
索引的合并：
name、email、phonenum
select * from tablename  where name='值' and email='值'

## 注意：
创建索引的时候要了解的知识：
１．创建一个索引，提高了查找效率但是，牺牲了增、删、改效率
２．会加大磁盘空间的开销
３．设置最短索引
create index indeaname on tablename(列(16)))

4.命中索引：
１．like '%xx' select * from tb1 where email like '%cn';

２．使用函数 select * from tb1 where reverse(email) = 'wupeiqi';

３．or select * from tb1 where nid = 1 or name = 'seven@live.com';

　　　特别的：当or条件中有未建立索引的列才失效，以下会走索引 select * from tb1 where nid = 1 or name = 'seven'; select * from tb1 where nid = 1 or name = 'seven@live.com' and email = 'alex'

５．类型不一致 如果列是字符串类型，传入条件是必须用引号引起来，不然... select * from tb1 where email = 999;

６．!= select * from tb1 where email != 'alex'

　　特别的：如果是主键，则还是会走索引 select * from tb1 where nid != 123

７．select * from tb1 where email > 'alex'

　　特别的：如果是主键或索引是整数类型，则还是会走索引 select * from tb1 where nid > 123 select * from tb1 where num > 123

８．order by select name from tb1 order by email desc;

　　当根据索引排序时候，选择的映射如果不是索引，则不走索引 特别的：如果对主键排序，则还是走索引： select * from tb1 order by nid desc;

９．组合索引最左前缀 如果组合索引为：(name,email) name and email -- 使用索引 name -- 使用索引 email -- 不使用索引

索引选择原则

较频繁的作为查询条件的字段应该创建索引
唯一性太差的字段不适合单独创建索引，即使频繁作为查询条件
更新非常频繁的字段不适合创建索引
不会出现在 WHERE 子句中的字段不该创建索引

例子：百万用户数据，建立索引查询，比较建立索引查询的优势














　




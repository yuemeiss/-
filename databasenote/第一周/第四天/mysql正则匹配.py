# 前面我们学习了正则表达式其实我们在mysql中也可以使用正则语句来查询数据。

select * from studentinfo where student_name like '王';

select * from studentinfo where student_name regexp '王';

LIKE匹配整个列。如果被匹配的文本在列值 中出现，LIKE将不会找到它，相应的行也不被返回（除非使用通配符）。而REGEXP在列值内进行匹配，如果被匹配的文本在列值中出现，REGEXP将会找到它，相应的行将被返回。这是一个非常重要的差别。

select * from studentinfo where student_name regexp '^牛';

select * from studentinfo where student_name regexp '.牛$';

select * from studentinfo where student_name regexp '.牛.*$';

select * from studentinfo where student_name regexp '成|王';

select * from studentinfo where student_name regexp '^成|王';

select * from studentinfo where student_name regexp '成|牛';

select * from studentinfo where student_name regexp '.牛.{1,4}';

select * from studentinfo where phonenum regexp '^[1-7]{2,4}';

select * from studentinfo where student_name regexp '.牛( |小)';

转义： 正则表达式语言由具有特定含义的特殊字符构成。我们已经看到.、[]、|和-等，还有其他一些字符。请问，如果你需要匹配这些字符，应该怎么办呢？例如，如果要找出包含.字符的值，怎样搜索？请看下面的例子：

SELECT name,email FROM studentinfo WHERE email REGEXP '\.';
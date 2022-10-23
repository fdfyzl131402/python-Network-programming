-- 数据的准备
	create database python_test_01 charset=utf8;
	
	--使用
	use python_test_01
	
	-- 查看当前创建的数据库
	select database();

	-- 准备数据
	-- students表
	create table students(
	    id int unsigned primary key auto_increment not null,
	    name varchar(20) default '',
	    age tinyint unsigned default 0,
	    height decimal(5,2),
	    gender enum('男','女','中性','保密') default '保密',
	    cls_id int unsigned default 0,
	    is_delete bit default 0
	);

	-- classes表
	create table classes (
	    id int unsigned auto_increment primary key not null,
	    name varchar(30) not null
	);


-- 查询
	-- 查询所有字段
	-- select * from 表名;
	select * from students;
	select * from classes;

	-- 查询指定字段
	-- select 列1,列2 from 表名;
	select id, name from classes;

	-- 指定别名 
	--select 字段 as 别名, as 别名 ...from 表名;
	select name as 姓名, gender as 性别 from students;

	-- select 表名.字段, 表名.字段 from 表名;
	select students.name, students.gender from students;

	-- 给表取别名
	select s.name, s.gender from students as s;
	-- select students.name, students.gender from students as s; 

	-- 消除重复项
	-- distinct 字段
	select distinct gender from students;


-- 条件查询
  	-- 比较运算符
  	-- select ... from 表名 where ...;
  	-- >
  	-- 查询大于18岁的数据
  	select * from students where age>18;

  	-- <  
  	-- 查询小于18岁的数据
	select * from students where age<18;

  	-- >= 
  	-- <=
  	-- 查询小于等于18岁的数据
	select * from students where age>=18;

	-- =
	-- 查询等于18岁的数据
	select * from students where age=18;

	--!= <> 不等于

--逻辑运算符
	-- and 
	-- 18到28的所有数据信息
	select * from students where age>18 and age<28;
	-- 18岁以上的所有女性
	select * from students where age>18 and gender="女";

	-- or 
	-- 18岁以上或者身高（包含）超过180的
	select * from students where age>18 or height>=180;

	--not 
	-- 不在 18岁以上的女性的信息
	select * from students where not age>18 and gender="女";
	select * from students where not (age>18 and gender="女");

	-- 年龄不是小于或者等于18岁，并且是女性的
	select * from students where (not age<=18) and gender="女";

--模糊查询
	--like 
	-- % 替换1个或者多个
	-- _替换一个
	-- 查询姓名中以“小”开始的名字
	select name from students where name like "小%";

	--查询有“小”的所有名字
	select name from students where name like "%小%";

	-- 查询有两个字的名字
	select name from students where name like "__";

	-- 查询有三个字的名字
	select name from students where name like "___";

	--查询至少有两个字的名字
	select name from students where name like "__%";

	-- rlike 正则
	-- 查询以周开头的名字
	select name from students where name rlike "^周.*";

	--查询以周开头 以伦结尾的名字
	select name from students where name rlike "^周.*伦$";


-- 范围查询
	--in (1, 3, 8) 表示在一个非连续的范围内
	-- 查询年龄为12,18,34年龄的姓名
	select name, age from students where age in (12, 18, 34);

	-- not in 
	-- 年龄不是18,34岁的姓名
	select name, age from students where age not in (18,34);


	-- between...and...在连续的范围内
	-- 查询年龄在18到34岁连续的范围内的姓名
	select name, age from students where age between 18 and 34;
	 
	-- not between...and...
	-- 查询年龄不在18到34岁的信息
	select * from students where age not between 18 and 34;
	select * from students where not age between 18 and 34;

	--判断是否为空
	-- is null
	select * from students where height is null;

	-- is not null 
	select * from students where height is not null;

-- 排序
	-- order by 字段
	-- asc从小到大排列，即升序；
	-- desc从大到小排序，即降序；
	-- 查询年龄在18到34岁的男性，按年龄从小到大排序；
	select * from students where (age between 18 and 34) and gender=1 order by age asc;

	-- 查询年龄在18到34岁的女性，身高从大到小排序；
	select * from students where (age between 18 and 34) and gender=2 order by height desc;

	-- order by 多个字段
	-- 查询年龄在18到34岁的女性，身高从大到小排序, 如果身高相同则按照按照id从大到小排序；
	select * from students where (age between 18 and 34) and gender=2 order by height desc,id desc;

	-- 查询年龄在18到34岁的女性，身高从大到小排序, 如果身高相同则按照按照年龄从小到大排序；
	-- 如果年龄也相同那么按照id从小到大排；
	select * from students where (age between 18 and 34) and gender=2 order by height desc,age asc,id asc;

	-- 按照年龄从小到大，身高从大到小排序；
	select * from students order by age asc,height desc;

--聚合函数
	-- 总数
	-- count
	-- 查询男性有多少人， 女性有多少人。
	select count(*) as 男性 from students where gender=1;
	select count(*) as 女性 from students where gender=2;

	-- 最大值
	-- max
	-- 查询最大的年龄
	select max(age) as 最大值 from students;

	-- 查询女性的最高身高；
	select max(height) from students where gender=2;

	-- min 
	-- 最小值

	-- sum
	-- 总和
	-- 计算所有人的年龄的总和
	select sum(age) from students;

	-- 平均值
	-- avg
	-- 计算所有人的平均年龄
	select avg(age) from students;

	-- 计算平均年龄 avg(age)/sum(*)
	select sum(age)/count(*) from students;

	-- 四舍五入 round(123.22,1) 保留一位小数
	-- 计算所有人的平均年龄，保留两位小数
	select round(sum(age)/count(*),2) from students;
	
	-- 计算男性的平均身高，保留两位小数；
	-- select name, round(avg(height),2) from students where gender=1;
	select round(avg(height),2) from students where gender=1;


--分组
	-- group by 
	-- 按照性别分组，查询所有性别
	-- 失败的select * from students group by gender;
	select gender,count(*) from students group by gender;

	--计算男性的人数；
	select gender,sum(gender=1) from students where gender=1 group by gender;
	select gender,count(*) from students where gender=1 group by gender;
	select gender,count(*),group_concat(name,"_",age) from students where gender=1 group by gender;

	-- group_concat(...)
	-- 查询同种性别中的姓名
	select gender, count(*),group_concat(name,"_",age," ",id) from students where gender=1 group by gender;

	--having 
	-- 查询平均年龄大于30岁的性别 having avg(age) >30
	select gender, group_concat(name),avg(age) from students group by gender having avg(age)>30;

	--查询每种性别中人数大于两个的信息
	select gender,group_concat(name) from students group by gender having count(*)>2;
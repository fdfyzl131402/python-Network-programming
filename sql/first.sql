--数据库的操作
	--链接数据库
	mysql -uroot -p 
	mysql -uroot -p...
	--退出数据库
	exit
	quit
	ctrl + q
	--sql语句后面要加分号
	--显示数据库版本
	select version();

	--查看所有数据库
	show databases;


	--显示当前时间
	select now();

	--创建数据库
	--create database 数据库名 charset=utf8;

	--查看创建的数据库的语句
	--show create database 数据库名;

	--删除数据库
	--drop database 数据库名;

	--查看当前使用的数据库
	--select database();

	--使用数据库
	--use 数据库名
	

--数据表的操作
	--show tables;


	--创建数据表
	--create table xxxx(字段 类型 约束， ....)；
	--auto_increment 表示自动增长
	--not null 表示不能为空
	--primary key 主键
	--default 默认值

	--查看表的结构
	--desc 数据表的名字；


	--创建students表(id,name,age,high,gender,cls_id)
	create table students(
		id int unsigned not null auto_increment primary key, 
		name varchar(30),
		age tinyint,
		high decimal(5,2) unsigned,
		gender enum("男", "女","保密") default "保密",
		cls_id int unsigned
		);

	--查看表的创建语句
	--show create table 表名;


	--修改表 --添加字段
	--alter table 表名 add 列名 类型;
	alter table students add birthday datetime;

	--修改字段 不重名版
	--aletr table 表名 modify 列名 类型及约束
	alter table students modify birthday date;


	--修改字段 重名版
	--alter table 表名 change 旧名 新名 类型及约束;
	alter table students change birthday birth date default "2000-01-01";

	--修改表 删除字段
	--alter table 表名 drop 列名；
	alter table students drop high;

	--删除表；
	--drop table 表名；
	drop table hhhh;

--增删改查
	--增加
		--全列增加
		--insert [into] 表名 values();
		--主键字段可以用0 null default表示
				+--------+----------------------------+------+-----+------------+----------------+
		| Field  | Type                       | Null | Key | Default    | Extra          |
		+--------+----------------------------+------+-----+------------+----------------+
		| id     | int unsigned               | NO   | PRI | NULL       | auto_increment |
		| name   | varchar(30)                | YES  |     | NULL       |                |
		| age    | tinyint                    | YES  |     | NULL       |                |
		| gender | enum('男','女','保密')     | YES  |     | 保密       |                |
		| cls_id | int unsigned               | YES  |     | NULL       |                |
		| birth  | date                       | YES  |     | 2000-01-01 |                |
		+--------+----------------------------+------+-----+------------+----------------+

		insert into students values(0, "小李飞刀",20,"男",1,"2020-01-01");

		--枚举中下标从1开始， 1---->"男"
		insert into students values(0, "小李飞刀",20,1,1,"2020-01-01");

		--部分增加
		--insert into students (列1...) values(值1...)；
		insert into students (name, gender) values("lisi", 1)；

		--多行插入
		insert into students (name, gender) values("小桥", 2),("大桥",2)；
		insert into students values(0, "卡特",20,2,1,"1999-01-01"),(0, "万豪",20,1,1,"2020-01-01");

		--修改
		--update 表名 set 列1=值1,列2=值2... where 条件;
		update students set name="gg", gender=2 where id=2;

	--查询基本使用
		--查询所有列
		--select * from 表名;
		--指定查询
		select * from students where name="...";
		select * from students where id>...;

		--指定查询列
		--select 列1, 列2 from 表名;
		select name, gender from students;

		--可以使用as为列或表指定别名
		--select 字段[as 别名], 字段[as 别名] from 表名 where ...;
		select name as 姓名, gender as 性别 from students;

		--物理删除
		--delete from students where ...;
		delete from students; -- 整个数据库数据全部删除;


		--逻辑删除
		--用一个字段来表示 这条信息是否不能再使用；
		--给students添加一个is_delete字段 bit 类型
		--alter table 表名 add is_delete bit default 0;
		alter table students add is_delete bit default 0;
		update students set is_delete=1 where id=2;
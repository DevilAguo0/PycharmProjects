import pymysql
conn=pymysql.connect()
cursor=conn.cursor()
sql_creat_database = "create database if not exists db_student"
cursor.execute(sql_creat_database)
sql_creat_table="create table if not exists students(number int primary key ,Name varchar(20),Grender varchar(20),Age varchar(20))"
cursor.execute(sql_creat_table)
sql_insert_01="insert into students(number, Name, Grender, Age) values (1,张三,女,22)"
sql_insert_02="insert into students(number, Name, Grender, Age) values (2,李四,男,12)"
sql_insert_03="insert into students(number, Name, Grender, Age) values (3,王五,女,12)"
sql_insert_04="insert into students(number, Name, Grender, Age) values (4,赵六,男,12)"
sql_insert_05="insert into students(number, Name, Grender, Age) values (5,孙七,女,12)"
cursor.execute(sql_insert_01,sql_insert_02,sql_insert_03,sql_insert_04,sql_insert_05)
sql_update="update students set Age = 21 where number = 5"
cursor.execute(sql_update)
sql_select = "select * from Grender = '女'"
cursor.execute(sql_select)

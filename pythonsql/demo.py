import pymysql
con = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    charset="utf8"

)

#获得游标
cursor = con.cursor()
sql_creat = "create database if not exists mydatabase;"
cursor.execute(sql_creat)

#创建数据表
sql_use = "use mydatabase"
cursor.execute(sql_use)


sql_table='create table if not exists employees(emID int primary key,emName varchar(20),emLevel varchar(20),emDepID varchar(20))'


cursor.execute(sql_table)

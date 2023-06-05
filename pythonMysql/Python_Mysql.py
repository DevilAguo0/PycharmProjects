import pymysql

coon = pymysql.connect(
    host='localhost',
    user='root',
    password='Gsh166390',
    charset='utf8')
cursor = coon.cursor()
sql_creat = "create database if not exists dbtest02"
cursor.execute(sql_creat)
sql_use = 'use dbtest'
cursor.execute(sql_use)
sql_table = 'create table if not exists employees(emID int primary key ,emName varchar(20),emLevel varchar(20),emDepID varchar(20))'
cursor.execute(sql_table)
print(coon.cursor())
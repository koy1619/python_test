#! /usr/bin/python
#-*- coding:utf-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("127.0.0.1","root","123456","test" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
#db.close()

'''
创建数据库表
'''

#如果数据表已经存在使用execute()方法删除表。
cursor.execute("DROP TABLE IF EXISTS test1")

#创建数据表SQL语句
sql = """CREATE TABLE test1 (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

#执行SQL语句
cursor.execute(sql)

'''
数据库插入
'''


#SQL插入语句
sql = """INSERT INTO test1(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()


'''
数据库查询
'''

#SQL查询语句
sql = "SELECT * FROM test1 \
        WHERE INCOME > '%d'" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                (fname, lname, age, sex, income )
except:
    print "Error: unable to fecth data"



'''
数据库更新
'''


#SQL更新语句
sql = "UPDATE test1 SET AGE = AGE + 2 \
        WHERE SEX = '%c'" % ('M')

'''
#sql删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
'''


try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()

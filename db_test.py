import MySQLdb
# 注意 这里需要额外导入, 不然会报module 'MySQLdb' has no attribute 'cursors'的错误
import MySQLdb.cursors as cors
 
# 打开数据库连接 
db = MySQLdb.connect("localhost", "root", "123456", "test", charset='utf8',
                    cursorclass=cors.DictCursor) 
# 使用cursor()方法获取操作游标  
cursor = db.cursor() 
# SQL 插入语句 
sql="INSERT INTO userinfo2(name) VALUES(%s)" 
try: 
   # 执行sql语句 
   cursor.executemany(sql,'smith') 
   # 提交到数据库执行 
   db.commit() 
except: 
   # Rollback in case there is any error 
   db.rollback() 
# 关闭数据库连接 
db.close() 
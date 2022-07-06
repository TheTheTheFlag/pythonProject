import cx_Oracle

conn = cx_Oracle.connect('openview/openview123@www.stardigi.top:1522/helowin')  # 连接数据库
print('连接成功!')
c = conn.cursor()  # 获取cursor
c.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
print('表已创建!')

# # 连接数据库，下面括号里内容根据自己实际情况填写
# conn = cx_Oracle.connect('scott/scott@127.0.0.1:1521/orcl')
# # 使用cursor()方法获取操作游标
# cursor = conn.cursor()
# # 使用execute方法执行SQL查询语句
# result = cursor.execute('Select * from abc')
# # 使用fetchone()方法获取一条数据
# # data=cursor.fetchone()
# # 获取所有数据
# all_data = cursor.fetchall()
# # 获取部分数据，8条
# # many_data=cursor.fetchmany(8)
# print(all_data)
# # 创建表
# cursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
# # 插入数据
# cursor.execute("INSERT INTO sites VALUES ('baidu','https://www.baidu.com')")
# conn.commit()  # 数据表内容有更新，必须使用到该语句
# print(cursor.rowcount, "记录插入成功。")
# # 删除数据
# sql = "DELETE FROM sites WHERE name = 'baidu'"
# cursor.execute(sql)
# conn.commit()
# print(cursor.rowcount, " 条记录删除")

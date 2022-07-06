# encoding=gbk

import cx_Oracle


#  创建表或视图
def create_drop_sql(v_sql):
    conn = cx_Oracle.connect('openview/openview123@www.stardigi.top:1522/helowin')  # 连接数据库
    print('连接成功!')
    c = conn.cursor()  # 获取cursor
    c.execute(v_sql)  # 使用cursor进行各种操作
    print(v_sql.strip(), '执行成功')
    #conn.commit()
    c.close()
    conn.close()


# 查询数据库，并返回数据
def query_sql(v_sql):
    conn = cx_Oracle.connect('openview/openview123@www.stardigi.top:1522/helowin')  # 连接数据库
    print('连接成功!')
    c = conn.cursor()  # 获取cursor
    try:
        # 解析sql语句
        c.parse(v_sql)
    # 捕获SQL异常
    except cx_Oracle.DatabaseError as e:
        print(e)
    c.execute(v_sql)  # 使用cursor进行各种操作
    row = c.fetchall()  # 可以调用cursor.fetchall()一次取完所有结果，或者cursor.fetchone()一次取一行结果
    c.close()  # 关闭cursor
    conn.close()  # 关闭连接
    # return row
    print(row[0])


# 访问数据库，插入数据
def insert_sql(v_sql, data):
    conn = cx_Oracle.connect('openview/openview123@www.stardigi.top:1522/helowin')
    c = conn.cursor()
    try:
        c.parse(v_sql)
    except cx_Oracle.DatabaseError as e:
        print(e)
    c.execute(v_sql, data)
    conn.commit()
    c.close()
    conn.close()


def delete_sql(v_sql):
    conn = cx_Oracle.connect('openview/openview123@www.stardigi.top:1522/helowin')
    c = conn.cursor()
    try:
        c.parse(v_sql)
    except cx_Oracle.DatabaseError as e:
        print(e)
    c.execute(v_sql)
    conn.commit()
    c.close()
    conn.close()


if __name__ == '__main__':
    v_sql = """     CREATE TABLE jxhjxh (name VARCHAR(255), url VARCHAR(255)) """
    v_sql = """
    
    drop TABLE jxhjxh
    
    """
    # v_sql = """   select * from  jxhjxh  """
    # query_sql(v_sql)
    create_drop_sql(v_sql)
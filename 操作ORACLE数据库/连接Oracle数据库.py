# encoding=gbk

import cx_Oracle


#  ���������ͼ
def create_drop_sql(v_sql):
    conn = cx_Oracle.connect('openview/openview123@www.stardigi.top:1522/helowin')  # �������ݿ�
    print('���ӳɹ�!')
    c = conn.cursor()  # ��ȡcursor
    c.execute(v_sql)  # ʹ��cursor���и��ֲ���
    print(v_sql.strip(), 'ִ�гɹ�')
    #conn.commit()
    c.close()
    conn.close()


# ��ѯ���ݿ⣬����������
def query_sql(v_sql):
    conn = cx_Oracle.connect('openview/openview123@www.stardigi.top:1522/helowin')  # �������ݿ�
    print('���ӳɹ�!')
    c = conn.cursor()  # ��ȡcursor
    try:
        # ����sql���
        c.parse(v_sql)
    # ����SQL�쳣
    except cx_Oracle.DatabaseError as e:
        print(e)
    c.execute(v_sql)  # ʹ��cursor���и��ֲ���
    row = c.fetchall()  # ���Ե���cursor.fetchall()һ��ȡ�����н��������cursor.fetchone()һ��ȡһ�н��
    c.close()  # �ر�cursor
    conn.close()  # �ر�����
    # return row
    print(row[0])


# �������ݿ⣬��������
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
import pandas as pd
from sqlalchemy.dialects.oracle import \
    BFILE, BLOB, CHAR, CLOB, DATE, \
    DOUBLE_PRECISION, FLOAT, INTERVAL, LONG, NCLOB, \
    NUMBER, NVARCHAR, NVARCHAR2, RAW, TIMESTAMP, VARCHAR, \
    VARCHAR2


def mapping_df_types(df):
    dtypedict = {}
    for i, j in zip(df.columns, df.dtypes):
        if "object" in str(j):
            dtypedict.update({i: VARCHAR(256)})
        if "float" in str(j):
            dtypedict.update({i: NUMBER(19, 8)})
        if "int" in str(j):
            dtypedict.update({i: VARCHAR(19)})
    return dtypedict


def put_df_toOracle(df_data, tableName, addres):
    from sqlalchemy import types, create_engine
    engine = create_engine(addres, encoding='utf-8', echo=True)
    from sqlalchemy.dialects.oracle import \
        BFILE, BLOB, CHAR, CLOB, DATE, \
        DOUBLE_PRECISION, FLOAT, INTERVAL, LONG, NCLOB, \
        NUMBER, NVARCHAR, NVARCHAR2, RAW, TIMESTAMP, VARCHAR, \
        VARCHAR2
    dtypedict = mapping_df_types(df_data)
    df_data.to_sql(tableName, engine, index=False, if_exists='append', \
                   dtype=dtypedict, chunksize=None)


# ------------------------------

if __name__ == '__main__':
    df_data = pd.read_excel('D:/WJ/数据准备/数据.xlsx')
    tableName = 'test_20211223'
    addres = "oracle://openview:openview123@www.stardigi.top:1522/helowin"
    put_df_toOracle(df_data, tableName, addres)

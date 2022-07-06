import pandas as pd


def print_df_head(a):
    df = pd.read_excel(a)
    print(df.head())


print_df_head('D:/WJ/机器学习输入/JPG.xlsx')


def print_df_head_return(a):
    df = pd.read_excel(a)
    df = df.head()
    return df


print(print_df_head_return('D:/WJ/机器学习输入/JPG.xlsx'))

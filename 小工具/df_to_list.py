import pandas as pd


def excel_one_line_to_list(df_to_list, a):
    df_li = df_to_list.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


df_to_list = pd.read_excel('d:/WJ/用户画像输入/话题攻克情况.xls')

column = list(df_to_list.columns)

city = excel_one_line_to_list(df_to_list, column.index('归属地市'))
print(city)

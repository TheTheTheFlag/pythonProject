import pandas as pd

df = pd.read_excel('d:/WJ/SR/kol2.xlsx')
df[['状态', '创建人', '归属地市']] = df[['状态', '创建人', '归属地市']].applymap(lambda x: str(x).strip())
df['创建时间'] = pd.to_datetime(df['创建时间'], format='%Y-%m-%d %H:%M:%S')

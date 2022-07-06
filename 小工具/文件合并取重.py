import pandas as pd
import os
import time


# 使用keep=‘first’参数，保留首次出现的重复项，删除后出现的。 这时数据保留了 之前不重复数据+首次出现的重复数据，
# a=df.drop_duplicates(subset=None, keep='first', inplace=False)
#
# 使用keep=‘False’参数，删除所有重复的数据。这时数据保留了 之前不重复数据。
# b=df.drop_duplicates(subset=None, keep=False, inplace=False)
#
# 把两个数据连接起来，再删除所有重复的数据，就得到了 之前重复的数据。
# 意思是： （之前不重复数据+首次出现的重复数据）+（之前不重复数据） - 之前不重复数据*2 =首次出现的重复数据
# c=a.append(b).drop_duplicates(keep=False)

# 去重复
def drop_duplicates(df):
    # 完全重复则删除
    df1 = df.drop_duplicates(subset=None, keep='first', inplace=False)
    df2 = df.drop_duplicates(subset=None, keep=False, inplace=False)
    df = df1.append(df2).drop_duplicates(keep=False)
    return df


def merge_execl(merge_file_dir):
    # 要合并的execl目录
    dir_name = merge_file_dir
    dir_list = os.listdir(dir_name)
    timer = time.time()
    # df.drop_duplicates(subset, keep, inplace)
    new_data_col = ''
    new_data = ''

    for file in dir_list:
        # 如果是文件并且以csv结尾
        file_name = dir_name + '\\' + file
        if os.path.isfile(file_name):
            if file_name.endswith('.csv'):
                new_file_name = dir_name + '\\' + 'new_file_{}.csv'.format(timer)
                df = pd.read_csv(file_name)
                df.to_csv(new_file_name, mode='a', index=False)
                # 打开csv文件去重复再次保存
                df = pd.read_csv(new_file_name, header=None)
                df = drop_duplicates(df)
                df.to_csv(new_file_name, header=False, index=False)
            # 合并xls文件
            elif file_name.endswith('.xls') or file_name.endswith('.xlsx'):
                new_file_name = dir_name + '\\' + '重复记录_{}.xlsx'.format(timer)
                df = pd.read_excel(file_name)
                df = df[['故障单号', '调度时长', '维护侧联系人', '维护侧责任组']]#限定范围
                if new_data_col == '':
                    new_data_col = list(df.columns)
                if new_data == '':
                    new_data = list(df.values)
                else:
                    new_data += list(df.values)
                new_df = pd.DataFrame(data=new_data, columns=new_data_col)
                new_df = drop_duplicates(new_df)
                new_df.to_excel(new_file_name, index=False)


if __name__ == '__main__':
    # 要合并execl文件夹
    file_dir_name = 'd:/WJ/数据准备/SLA'
    merge_execl(file_dir_name)
    print('已取出存在重复的数据')

# coding=utf-8

import xlrd


class FileUtil():

    def __init__(self, file_path, sheet_index):
        self.data = xlrd.open_workbook(file_path)
        self.table = self.data.sheet_by_index(sheet_index)
        # 获取table第一行值作为key
        self.table_key = self.table.row_values(0)
        # 获取总行数
        self.row_num = self.table.nrows
        # 获取总列数
        self.col_num = self.table.ncols

    def dict_data(self):
        if self.row_num <= 1:
            print(u"excel的行数小于等于1")
        else:
            list = []
            j = 1
            # 循环行的次数，去掉表头
            for i in range(self.row_num - 1):
                dict = {}
                # 遍历每行数据
                values = self.table.row_values(j)
                # 遍历每列
                for x in range(self.col_num):
                    # 往字典里面添加一组键值对：dict["username"] = "aaaaaaaa"
                    dict[self.table_key[x]] = values[x]
                list.append(dict)
                j += 1
            return list


if __name__ == '__main__':
    file_path = "D:\\WJ\\用户画像输入\\近7天活跃详情.xlsx"
    sheet_index = 0
    table = FileUtil(file_path, sheet_index)
    dict = table.dict_data()
    print
    dict
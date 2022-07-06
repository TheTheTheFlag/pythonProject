#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 20:37
# @Author  : H
# @File    : zipfilev2.py


import os
import hashlib
import time
from shutil import copyfile


def getfielpath(path, sub):
    if os.path.isdir(path):
        # 如果绝对路径下的文件夹
        for i in os.listdir(path):  # i文件名
            path2 = os.path.join(path, i)  # 拼接绝对路径
            if os.path.isdir(path2):  # 判断如果是文件夹,调用本身
                getfielpath(path2, sub)
            else:
                sub.append(path2)
    elif os.path.isfile(path):
        # 如果绝对路径下的文件
        sub.append(path)
    else:
        print("File or path doesn\'t exit")


def zipFile(filepath, WinRARpath, password, apt=None):
    oldname = filepath.split('\\')[-1]
    """获取文件的hash"""
    datas = {}  # 结果存为json，以便后需
    f = open(filepath, "rb")
    rb = f.read()
    data = {'MD5': hashlib.md5(rb).hexdigest(),
            'SHA1': hashlib.sha1(rb).hexdigest(),
            'SHA256': hashlib.sha256(rb).hexdigest()}
    f.close()
    """文件hash由文件名构成词典"""
    datas[oldname] = data

    """以文件的sha256重命名：若不重命名则当文件名中有空格或特殊符号时，启动DOS命令会失败"""
    newfilename = filepath.replace(oldname, data['SHA256'])
    """如果使用sha256命名的文件已存在，说明两个文件的sha256值相同，即文件重复，删除文件；否则重命名"""
    if os.path.exists(newfilename):
        os.remove(filepath)
        return 1
    else:
        os.rename(filepath, newfilename)
        filepath = newfilename


    """输出压缩文件的位置，即将压缩文件输出到哪个文件夹中，压缩文件以文件的 SHA256.rar 命名"""
    if os.path.exists(r'D:\zipsampletemp'):
        pass
    else:
        os.makedirs(r'D:\zipsampletemp')

    outputpath = f"D:\\zipsampletemp\\{data['SHA256']}"

    """如果压缩文件已存在，则说明录入重复，删除源文件即可"""
    if os.path.exists(outputpath + ".rar"):
        print(f"[-]--->压缩文件已存在:\t{filepath}")
        os.remove(filepath)
        return 1

    """DOS命令"""
    cmdzip = f"{WinRARpath} a -ep -p{password}  {outputpath} {filepath}"

    try:
        # DOS调用WinRAR加密压缩文件
        os.popen(cmdzip)
    except Exception as err:
        print(err)

    with open("d:\\newsample.txt", "a", encoding="utf-8")as f:
        if apt:
            hashs = data['MD5'] + "#" + data['SHA1'] + "#" + data['SHA256'] + "#" + apt + "\n"
        else:
            hashs = data['MD5'] + "#" + data['SHA1'] + "#" + data['SHA256'] + "#" + "\n"
        f.writelines(hashs)


def unzipFile(filepath, WinRARpath, password, flag):
    outputpath = "D:\\TEMPTEMP"
    cmdunzip = f"{WinRARpath} e -p{password}  {filepath} {outputpath}"
    try:
        # DOS调用WinRAR加密压缩文件
        os.popen(cmdunzip)
        print(f"[+]==>源文件解压成功：\t{filepath}")
        if flag == 0:
            # 删除原有文件
            os.remove(filepath)
            print(f"[+]==>源文件删除成功：\t{filepath}")
        elif flag == 1:
            pass
    except Exception as err:
        print(err)


if __name__ == '__main__':
    WinRARpath = r"D:\WinRAR\Rar.exe"
    password = "158571"
    path = r"D:\WJ"
    # apt = 'unknown'
    apt = 'TeamSpy Crew'

    sub = []
    getfielpath(path, sub)
    for i in sub:
        zipFile(i, WinRARpath=WinRARpath, password=password, apt=apt)
    print(f"[+]===>共计压缩文件个数：\t{len(sub)}")

    # for i in sub:
    #     unzipFile(i, WinRARpath=WinRARpath, password=password, flag = flag)


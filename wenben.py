#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename:exchange_newline_all.py

import re, os


def newline(file_name):  # 定义转换函数
    f = open(file_name, 'r')
    content = f.readlines()
    f.close()

    f = open(file_name, 'w')
    for line in content:
        f.writelines(re.sub('48', '\n48', line))  # 在48之前换行替换

    f.close()


while True:
    path = raw_input('INPUT THE FILEPATH(eg F:\sscom\dir):')  # 输入待处理文件夹
    print
    path
    l = os.listdir(r'%s' % path)  # 遍历文件夹内文件
    num = len(l)
    for i in range(0, num):  # 逐一处理每个文件
        file_x = r'%s\%s' % (path, l[i])
        newline(file_x)
        print
        "FINISHED,OK"

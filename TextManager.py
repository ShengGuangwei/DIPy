#!/usr/bin/env python
# encoding: utf-8
"""
@author: ShengGW
@time: 19/08/02 23:00
@file: Json.py
@version: ??
@software: PyCharm
@contact: shenggw95@gmail.com
"""


import json
import codecs
import pandas as pd


def json_dump(outfilename, dic):
    """
    传入保存路径和字典等形式的数据，保存数据到对应的文件中

    :param outfilename: 输出文件路径（包括文件后缀名）
    :param dic: 需要保存为.json文件的字典等
    """
    if outfilename[-4:] == 'json':
        with codecs.open(outfilename, 'w', 'utf-8') as outfile:
            json.dump(dic, outfile, ensure_ascii=False)
    else:
        print('请输入正确的文件格式！')


def JsontoExcel(jsonfile):
    """
    将.json文件存储为.xlsx文件
    待修改：根据.json文件的情况，将数据分列存储，后续需添加约束列名的参数
    
    :param jsonfile: 输入文件路径（包括文件后缀名）
    """
    file = codecs.open(jsonfile, 'r', encoding='utf-8')
    dic = json.loads(file.read())
    campany_name_list = []
    campany_date_list = []
    for campany in dic:
        campany_name_list.append(campany['campany_name'])
        campany_date_list.append(campany['campany_date'])

    df = pd.DataFrame({'公司名称':campany_name_list, '成立日期':campany_date_list})
    df.to_excel(jsonfile[:-5] + '.xlsx')


def ExceltoJson(excelfile, col1=None, col2=None, col3=None, col4=None):
    """
    将.xls或者.xlsx文件存储为.json文件
    待修改：先读取出excel文件，然后根据具体列名输出，col1等参数变为限制需保存列的参数

    :param excelfile: 输入文件路径（包括文件后缀名）
    :param col1: 列名1
    :param col2: 列名2
    :param col3: 列名3
    :param col4: 列名4
    """
    data = pd.read_excel(excelfile)
    list = []
    for index, row in data.iterrows():
        temp = {}
        if row['经营状态'] == '在业' or row['经营状态'] == '存续':
            temp['campany_name'] = row[col1]
            temp['campany_date'] = row[col2]
            if col3 != None and col4 != None:
                temp['lat'] = row[col3]
                temp['lng'] = row[col4]
            list.append(temp)

    # 判断输入文件的后缀名是否满足条件
    if excelfile[-4:] == 'xlsx':
        with codecs.open(excelfile[:-5] + '_date.json', 'w', 'utf-8') as outfile:
            json.dump(list, outfile, ensure_ascii=False)
    elif excelfile[-3:] == 'xls':
        with codecs.open(excelfile[:-4] + '_date.json', 'w', 'utf-8') as outfile:
            json.dump(list, outfile, ensure_ascii=False)
    else:
        print("请输入正确的文件格式！")

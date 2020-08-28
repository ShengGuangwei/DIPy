#!/usr/bin/env python
# encoding: utf-8
"""
@author: ShengGW
@time: 20/08/28 16:25
@file: FileManager.py
@version: ??
@software: PyCharm
@contact: shenggw95@gmail.com
"""
import os


def getFileName(dirName, postfix, abspath=1):
    """
    寻找给定文件夹下符合条件的文件，并添加到imgFileList中
    :param dirName: 给定文件夹
    :param postfix: 给定筛选条件集合, 筛选条件应该是集合中元素
    :param abspath: 是否返回绝对路径，默认返回
    :return:
    """
    # 存储符合条件的影像路径
    out_file_list = []
    # 寻找给定文件夹下符合条件的文件，并添加到imgFileList中
    for maindir, subdir, fileList in os.walk(dirName):
        for fileName in fileList:
            if fileName != '':
                if abspath == 1:
                    outPath = os.path.join(maindir, fileName)
                else:
                    outPath = fileName
                for label in postfix:
                    if fileName[-len(label):] == label:
                        try:
                            out_file_list.append(outPath)
                        except:
                            pass
            else:
                print('文件路径存在空值！')

    return out_file_list

def getFiles(dirName, abspath=1):
    """
    寻找给定文件夹下所有的文件，并添加到imgFileList中
    :param dirName: 给定文件夹
    :param postfix: 给定筛选条件集合, 筛选条件应该是集合中元素
    :param abspath: 是否返回绝对路径，默认返回
    :return:
    """
    # 存储符合条件的影像路径
    out_file_list = []
    # 寻找给定文件夹下符合条件的文件，并添加到imgFileList中
    for maindir, subdir, fileList in os.walk(dirName):
        for fileName in fileList:
            if fileName != '':
                if abspath == 1:
                    outPath = os.path.join(maindir, fileName)
                else:
                    outPath = fileName
                try:
                    out_file_list.append(outPath)
                except:
                    pass
            else:
                print('文件路径存在空值！')

    return out_file_list


def getFileName_withstart(dirName, start, end, abspath=1):
    """
    获取给定文件夹下给定开头和结尾的文件列表

    :param dirName: 给定文件夹路径
    :param start: 给定开头筛选条件集合
    :param end: 给定结尾筛选条件集合
    :param abspath: 是否返回绝对路径，默认返回
    :return: 符合条件的文件路径组成的list
    """
    out_file_list = []
    for maindir, subdir, file_name_list in os.walk(dirName):
        for filename in file_name_list:
            if filename != '':
                if abspath == 1:
                    outPath = os.path.join(maindir, filename)
                else:
                    outPath = filename
                for start_label in start:
                    for end_label in end:
                        try:
                            if filename.endswith(end_label) and filename.startswith(start_label):
                                out_file_list.append(outPath)
                        except:
                            pass

    return out_file_list

def csvSpliting(dirName, newDirName, csvSize):
    """
    按照行数拆分csv文件
    Args:
        dirName: 待拆分csv文件
        newDirName: 拆分后csv文件存储路径
        csvSize: csv拆分行数

    Returns:

    """
    # 文件的绝对路径
    filePaths = getFiles(dirName)
    # 文件名
    fileNames = getFiles(dirName, abspath=0)

    blockNames = fileNames.copy()

    # 拆分
    for i in range(len(filePaths)):
        f = open(filePaths[i], "r", encoding='gbk')
        lines = f.readlines()

        # 确定拆分成的文件数目
        blockNum = math.ceil(len(lines) / csvSize)
        print(len(lines), blockNum)

        # 根据待拆分文件新建文件夹
        tempPath = os.path.join(newDirName, blockNames[i][:-4])
        if not os.path.exists(tempPath):
            os.mkdir(tempPath)

        # 每csvSize行输出为一个csv文件
        for j in range(blockNum):
            if j < blockNum - 1:
                newFilePath = os.path.join(tempPath, fileNames[i][:-4] + "_" + str(j + 1) + ".csv")
                print(newFilePath)
                new_f = open(newFilePath, "w", encoding='gbk')

                # 每csvSize行为一个循环
                for k in range(csvSize):
                    lineNum = k + csvSize * j
                    new_f.write(lines[lineNum])

                new_f.close()

            elif j == blockNum - 1:
                newFilePath = os.path.join(tempPath, fileNames[i][:-4] + "_" + str(j + 1) + ".csv")
                print(newFilePath)
                new_f = open(newFilePath, "w", encoding='gbk')

                # 计算剩余的行数
                remainLines = len(lines) - csvSize * j
                for k in range(remainLines):
                    lineNum = k + csvSize * j
                    new_f.write(lines[lineNum])

                new_f.close()

        f.close()

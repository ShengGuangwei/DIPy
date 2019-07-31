#!/usr/bin/env python
# encoding: utf-8
"""
@author: ShengGW
@time: 19/07/26 23:45
@file: FileScanning.py
@version: ??
@software: PyCharm
@contact: shenggw95@gmail.com
"""
import os


def getFileName(dirName, postfix, abspath=1):
    """
    寻找给定文件夹下符合条件的文件，并添加到imgFileList中
    :param dirName: 给定文件夹
    :param postfix: 给定筛选条件集合
    :param abspath: 是否返回绝对路径，默认返回
    :return:
    """
    # 存储符合条件的影像路径
    imgFileList = []
    # 寻找给定文件夹下符合条件的文件，并添加到imgFileList中
    for maindir, subdir, fileList in os.walk(dirName):
        for fileName in fileList:
            if abspath == 1:
                imgPath = os.path.join(maindir, fileName)
            else:
                imgPath = fileName
            for label in postfix:
                if fileName[-len(label):] == label:
                    try:
                        imgFileList.append(imgPath)
                    except:
                        pass
    return imgFileList
#!/usr/bin/env python
# encoding: utf-8
"""
@author: ShengGW
@time: 19/11/05 20:49
@file: OTSU.py
@version: ??
@software: PyCharm
@contact: shenggw95@gmail.com
"""

def OTSU(hist, bins, pixelnum):
    sumT, sum0, sum1 = 0, 0, 0
    w0, w1 = 0, 0
    varBetween, mean0, mean1, varBetween_max = 0, 0, 0, 0
    threshold0, threshold1 = 0, 0
    for i in bins:
        sumT += i * hist[0][i]  # 全部像元的灰度值之和
    for i in bins:
        w0 += hist[0][i]  # 小于threshold的像元数
        if w0 == 0:
            continue
        w1 = pixelnum - w0  # 大于或等于threshold的像元数
        if w1 == 0:
            break
        sum0 += i * hist[0][i]  # 小于threshold的像元的灰度值之和
        sum1 = sumT - sum0  # 大于或等于threshold的像元的灰度值之和
        mean0 = sum0 / (w0 * 1.0)  # 小于threshold的像元的平均灰度
        mean1 = sum1 / (w1 * 1.0)  # 大于或等于threshold的像元的平均灰度
        varBetween = w0 / (pixelnum * 1.0) * w1 / (pixelnum * 1.0) * (mean0 - mean1) * (mean0 - mean1)  # 类间方差
        if varBetween >= varBetween_max:
            threshold0 = i
            if varBetween > varBetween_max:
                threshold1 = i
            varBetween_max = varBetween

    return (threshold0 + threshold1) / 2.0
#!/usr/bin/env python
# encoding: utf-8
"""
@author: ShengGW
@time: 19/07/26 19:59
@file: SpectralIndex.py
@version: ??
@software: PyCharm
@contact: shenggw95@gmail.com
"""

import gdal
import numpy as np
import os


def read_img(filename):
    """
    读取图像，返回图像数组等信息

    :param filename:输入图像的存储路径（如果图像不在当前工作路径，此路径应为图像的绝对存储路径）
    :return:图像的数组形式，图像的列数（图像宽），图像的行数（图像高），图像的投影信息，图像的仿射矩阵
    """
    dataset = gdal.Open(filename)
    im_width = dataset.RasterXSize  # 栅格矩阵的列数
    im_height = dataset.RasterYSize  # 栅格矩阵的行数
    im_geotrans = dataset.GetGeoTransform()  # 仿射矩阵
    im_proj = dataset.GetProjection()  # 地图投影信息
    im_data = dataset.ReadAsArray(0, 0, im_width, im_height)  # 将数据写成数组
    # im_band = dataset.GetRasterBand(1).ReadAsArray(0, 0, im_width, im_height)

    del dataset
    return im_data, im_width, im_height, im_proj, im_geotrans


def export_singleband(outname, im_array, im_proj, im_geotrans):
    """
    输出单波段图像

    :param outname: 输出图像的存储路径
    :param im_array: 输出图像的数组
    :param im_proj: 输出图像的投影信息
    :param im_geotrans: 输出图像的仿射矩阵
    :return:
    """
    tiff_driver = gdal.GetDriverByName('GTiff')
    out_tiff = tiff_driver.Create(outname, im_array.shape[1], im_array.shape[0], 1, gdal.GDT_Float32)

    if im_proj != []:
        out_tiff.SetProjection(im_proj)
    if im_geotrans != []:
        out_tiff.SetGeoTransform(im_geotrans)

    out_band = out_tiff.GetRasterBand(1)
    out_band.WriteArray(im_array)
    out_band.FlushCache()


def get_ndvi(in_name, out_name, band_num_red, band_num_nir):
    """
    计算输入图像的归一化植被指数（NDVI）并保存

    :param in_name: 输入图像的路径
    :param out_name: NDVI计算结果的保存路径
    :param band_num_red: 输入图像中红光波段对应的波段
    :param band_num_nir: 输入图像中近红外波段对应的波段
    :return:
    """
    # 获取图像所在路径以及不带后缀的文件名
    (filepath, fullname) = os.path.split(in_name)
    (prename, suffix) = os.path.splitext(fullname)
    # 读取图像
    im_data, im_width, im_height, im_proj, im_geotrans = read_img(in_name)
    # 读取红光波段和近红外波段
    im_bandmaxnum = im_data.shape[0]
    if 0 < band_num_nir <= im_bandmaxnum and 0 < band_num_red <= im_bandmaxnum:
        red_band = im_data[band_num_red - 1]
        nir_band = im_data[band_num_nir - 1]
        red_band = red_band.astype(np.float32)
        nir_band = nir_band.astype(np.float32)
        # 计算NDVI
        ndvi = (nir_band - red_band) / (nir_band + red_band)
        # 去除NDVI计算结果中的NAN值，并将结果转换成float32
        nan_index = np.isnan(ndvi)
        ndvi[nan_index] = 0
        ndvi = ndvi.astype(np.float32)
        # 将NDVI计算结果保存成tiff格式的图像
        export_singleband(out_name, ndvi, im_proj, im_geotrans)
    else:
        if band_num_nir > im_bandmaxnum or band_num_nir <= 0:
            print("Band %d is not exist, Please enter band number again!" % band_num_nir)
        if band_num_red > im_bandmaxnum or band_num_red <= 0:
            print("Band %d is not exist, Please enter band number again!" % band_num_red)
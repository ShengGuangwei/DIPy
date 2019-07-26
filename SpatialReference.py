#!/usr/bin/env python
# encoding: utf-8
"""
@author: ShengGW
@time: 19/07/12 18:11
@file: SpatialReference.py
@version: ??
@software: PyCharm
@contact: shenggw95@gmail.com
"""

import ogr
import osr
import DIPy.SpectralIndex as dsi


def getPrjGeo(filename):
    """
    获取给定图像的投影参考系和地理参考系

    :param dataset: GDAL地理数据
    :return: 投影参考系和地理参考系
    """
    dataset = dsi.read_img(filename)
    pcs = osr.SpatialReference()
    pcs.ImportFromWkt(dataset[3])
    gcs = pcs.CloneGeogCS()
    return pcs, gcs

def PCStoGCS(pcs, gcs, x, y):
    """
    将投影坐标转换为经纬度坐标

    :param pcs: 投影坐标系
    :param gcs: 地理坐标系
    :param x: 投影坐标x
    :param y: 投影坐标y
    :return: 投影坐标(x, y)对应的经纬度坐标(lon, lat)
    """
    # 构造投影坐标系到地理坐标系的转换关系
    ct = osr.CoordinateTransformation(pcs, gcs)
    # 投影坐标转换为地理坐标
    coords = ct.TransformPoint(x, y)
    return coords[:2]

def GCStoPCS(pcs, gcs, lon, lat):
    """
    将地理坐标转换为投影坐标

    :param pcs: 投影坐标系
    :param gcs: 地理坐标系
    :param lon: 经度
    :param lat: 纬度
    :return: 经纬度坐标(lon, lat)对应的投影坐标(x, y)
    """

    # 构造地理坐标系到投影坐标系的转换关系
    ct = osr.CoordinateTransformation(gcs, pcs)
    # 投影坐标转换为地理坐标
    coords = ct.TransformPoint(lon, lat)
    return coords[:2]

def getVerGeo(filename, geocd = 1):
    """
    获取图像的四个顶点的地理坐标

    :param filename: 图像
    :param geocd: 默认为1，即要求输出坐标为地理坐标，如果为其他值则说明要求输出坐标为投影坐标
    :return: dataset对应影像的四个顶点的地理坐标(lon, lat)
    """
    # 获取影像的属性信息
    dataset = dsi.read_img(filename)
    im_width = dataset[1]  # 栅格矩阵的列数
    im_height = dataset[2]  # 栅格矩阵的行数
    im_geotrans = dataset[4]  # 仿射矩阵
    # 经度
    ltx, rtx, rbx, lbx = im_geotrans[0], im_geotrans[0]+im_width*im_geotrans[1], im_geotrans[0]+im_width*\
                         im_geotrans[1], im_geotrans[0]
    # 纬度
    lty, rty, rby, lby = im_geotrans[3], im_geotrans[3], im_geotrans[3]+im_height*im_geotrans[5], im_geotrans[3]+im_height*im_geotrans[5]

    if geocd == 1:
        # 将投影坐标转换成地理坐标
        pcs, gcs = getPrjGeo(filename)
        lt = PCStoGCS(pcs, gcs, ltx, lty)
        rt = PCStoGCS(pcs, gcs, rtx, rty)
        rb = PCStoGCS(pcs, gcs, rbx, rby)
        lb = PCStoGCS(pcs, gcs, lbx, lby)
    else:
        # 投影坐标
        lt = (ltx, lty)
        rt = (rtx, rty)
        rb = (rbx, rby)
        lb = (lbx, lby)


    # # 判断影像的最小经纬度
    # leftline = min(lt[0], lb[0])
    # rightline = max(rt[0], rb[0])
    # bottomline = min(lb[1], rb[1])
    # topline = max(lt[1], rt[1])

    return lt, rt, rb, lb

def getGeoDegree(geocd):
    """
    将小数形式的坐标转换为度分秒形式

    :param geocd: 待转换的小数形式的坐标
    :return: 输入坐标对应的度，分，秒
    """
    num = 60
    degree = int(geocd)
    temp = (geocd - degree) * num
    minute = int(temp)
    second = (temp - minute) * num

    return degree, minute, second

def getGeoDecimal(degree, minute, second):
    """
    将度分秒形式的坐标转换为小数形式

    :param degree: 待转换坐标的度
    :param minute: 待转换坐标的分
    :param second: 待转换坐标的秒
    :return: 输入坐标对应的小数形式
    """
    geocd = float(int(degree) + int(minute) / 60 + int(second) / 3600)

    return geocd

def getShapefile(path, filename, geocd = 1):
    """
    根据图像的覆盖范围生成相应shapefile Polygon文件

    :param path: shapefile文件路径(包含文件名)
    :param filename: 图像的文件路径
    :param geoRange: 影像四个角点投影或者地理坐标(依次为左上，右上，右下，左下)
    :param geocd: 默认为1，即输入坐标为地理坐标，如果为其他值则说明输入坐标为投影坐标
    :return: shapefile文件
    """
    driver = ogr.GetDriverByName("ESRI Shapefile")  # 定义文件类型
    data_source = driver.CreateDataSource(path)  # 定义文件存储位置
    if geocd == 1:
        _, srs = getPrjGeo(filename)
        geoRange = getVerGeo(filename, geocd=1)
    else:
        srs, _ = getPrjGeo(filename)
        geoRange = getVerGeo(filename, geocd=0)

    layer = data_source.CreateLayer('layer', srs, ogr.wkbPolygon)
    feature = ogr.Feature(layer.GetLayerDefn())
    TopLeftLatitude = geoRange[0][1]
    TopLeftLongitude = geoRange[0][0]
    TopRightLatitude = geoRange[1][1]
    TopRightLongitude = geoRange[1][0]
    BottomRightLatitude = geoRange[2][1]
    BottomRightLongitude = geoRange[2][0]
    BottomLeftLatitude = geoRange[3][1]
    BottomLeftLongitude = geoRange[3][0]
    # 创建面要素
    wkt = "POLYGON((%f %f, %f %f, %f %f, %f %f, %f %f))" % (
        TopLeftLongitude, TopLeftLatitude,
        TopRightLongitude, TopRightLatitude,
        BottomRightLongitude, BottomRightLatitude,
        BottomLeftLongitude, BottomLeftLatitude,
        TopLeftLongitude, TopLeftLatitude)
    point = ogr.CreateGeometryFromWkt(wkt)
    feature.SetGeometry(point)
    layer.CreateFeature(feature)
    feature = None
    data_source = None
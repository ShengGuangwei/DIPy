# DIPy
:earth_africa: :earth_africa: :earth_africa: This is a Python package for digital image processing, especially for the image with spatial reference  

## 依赖的Package  

`osgeo`：[Open Source Geospatial Foundation](https://www.osgeo.org/)提供的[开源Package](https://github.com/OSGeo)，包括GDAL、OGR和OSR  

   > GDAL：英文全称为 Geospatial Data Abstraction Library，是一个在X/MIT许可协议下的开源栅格空间数据转换库  
   > OGR：处理矢量文件的Package  
   > OSR：处理空间参考等的Package 

`Pillow`：[Pillow](https://github.com/python-pillow/Pillow) is the friendly PIL fork by Alex Clark and Contributors, and PIL is the Python Imaging Library by Fredrik Lundh and Contributors  

`NumPy`：[NumPy](https://numpy.org/) is the fundamental package for scientific computing with Python  

`json`：[JSON (JavaScript Object Notation)](https://docs.python.org/3/library/json.html?highlight=json#module-json), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired by JavaScript object literal syntax   

`codecs`：[codecs](https://docs.python.org/3/library/codecs.html) defines base classes for standard Python codecs (encoders and decoders) and provides access to the internal Python codec registry, which manages the codec and error handling lookup process  

`pandas`：[pandas](https://pandas.pydata.org/) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language  


## Cookbook  

:wink: [Python Documentation](https://docs.python.org/3/contents.html)  

:wink: [the Python GDAL/OGR Cookbook](https://pcjericks.github.io/py-gdalogr-cookbook/)  

:wink: [GDAL documentation](https://gdal.org/#)  

:wink: [Python GDAL课程笔记](https://www.osgeo.cn/python_gdal_utah_tutorial/index.html)  

:wink: [GISpark](https://gispark.readthedocs.io/zh_CN/latest/index.html)  

:wink: [python3-cookbook](https://python3-cookbook.readthedocs.io/zh_CN/latest/copyright.html)


## 各种Package的下载地址  

:beginner: [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/) 


## 组织结构  

### `FileManager.py`  

  * `getFileName`：寻找给定文件夹下符合条件的文件，并返回这些文件名组成的数组  
  * `getFiles`：寻找给定文件夹下所有的文件，并返回这些文件名组成的数组
  * `getFileName_withstart`：获取给定文件夹下给定开头和结尾的文件列表，并返回这些文件名组成的数组
  
###  `SpatialReference.py`  

  * `getPrjGeo`：获取给定数据的投影参考系和地理参考系 
  * `PCStoGCS`：将投影坐标转换为经纬度坐标 
  * `GCStoPCS`：将地理坐标转换为投影坐标
  * `getVerGeo`：获取GDAL地理数据的四个顶点的地理坐标
  * `getGeoDegree`：将小数形式的坐标转换为度分秒形式
  * `getGeoDecimal`：将度分秒形式的坐标转换为小数形式
  * `getShapefile`：根据GDAL地理数据的覆盖范围生成相应的polygon文件
  
### `RasterProcessing.py`  

  * `read_img`：读取图像，返回图像数组等信息
  * `export_singleband`：输出单波段图像
  * `get_ndvi`：计算输入图像的归一化植被指数（NDVI）并保存
  
### `VectorProcessing.py`  

  * `clip_raster`：根据给定的shapefile Polygon文件提取出raster文件对应Polygon内的值  
  > 代码来自[K. Arthur Endsley的博客](http://karthur.org/2015/clipping-rasters-in-python.html)
  
> :bomb: **存在的问题：**  

  :persevere: 目前要求shapefile文件中**只有一个**Polygon要素，如果存在多个Polygon要素，根据要素提取后的结果之间会存在连线  
  
  :persevere: 目前从raster提取出来的结果跟原图像比较后发现存在**像元的偏移**，可能是因为给新图像赋予一个新的左上角投影坐标时，未考虑原先图像对应像元的投影坐标，从而产生像元坐标位置偏移  

### `TextProcessing.py`  

  * `json_dump`：传入保存路径和字典等形式的数据，保存数据到对应的文件中  
  * `JsontoExcel`：将.json文件存储为.xlsx文件    
  * `ExceltoJson`：将.xls或者.xlsx文件存储为.json文件
  
### `OTSU.py`  

  * `OTSU`：基于大津算法得到区分图像前景后景的阈值  
  
  
> :bookmark: **TODO：**  

:smirk: XML文件处理  

:smirk: GeoJson文件处理

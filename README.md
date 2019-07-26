# DIPy
This is a Python package for digital image processing based on GDAL, osr, ogr, NumPy etc.

## 文件结构
### `SpatialReference.py`：
  * `getPrjGeo`：获取给定数据的投影参考系和地理参考系 
  * `PCStoGCS`：将投影坐标转换为经纬度坐标 
  * `GCStoPCS`：将地理坐标转换为投影坐标
  * `getVerGeo`：获取GDAL地理数据的四个顶点的地理坐标
  * `getGeoDegree`：将小数形式的坐标转换为度分秒形式
  * `getGeoDecimal`：将度分秒形式的坐标转换为小数形式
  * `getShapefile`：根据GDAL地理数据的覆盖范围生成相应的polygon文件
  
### `SpectralIndex.py`：
  * `read_img`：读取图像，返回图像数组等信息
  * `export_singleband`：输出单波段图像
  * `get_ndvi`：计算输入图像的归一化植被指数（NDVI）并保存
  
## TODO
### XML文件处理
### 根据矢量文件（如shapefile文件）的范围获取图像对应位置的值并分析

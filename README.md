# DIPy
This is a Python package for digital image processing based on GDAL, osr, ogr, NumPy etc. :earth_africa:

:page_facing_up: ## **文件结构**  

:simple_smile: ### `SpatialReference.py`：  

  * `getPrjGeo`：获取给定数据的投影参考系和地理参考系 
  * `PCStoGCS`：将投影坐标转换为经纬度坐标 
  * `GCStoPCS`：将地理坐标转换为投影坐标
  * `getVerGeo`：获取GDAL地理数据的四个顶点的地理坐标
  * `getGeoDegree`：将小数形式的坐标转换为度分秒形式
  * `getGeoDecimal`：将度分秒形式的坐标转换为小数形式
  * `getShapefile`：根据GDAL地理数据的覆盖范围生成相应的polygon文件
  
### :simple_smile: `SpectralIndex.py`：  

  * `read_img`：读取图像，返回图像数组等信息
  * `export_singleband`：输出单波段图像
  * `get_ndvi`：计算输入图像的归一化植被指数（NDVI）并保存
  
### :simple_smile: `FileScanning.py`：  

  * `getFileName`：寻找给定文件夹下符合条件的文件，并返回这些文件名组成的数组

### :simple_smile: `GetShapefileCover.py`：  

  * `clip_raster`：根据给定的shapefile Polygon文件提取出raster文件对应Polygon内的值
  
> :bomb: **存在的问题：**  

  :persevere: 目前要求shapefile文件中**只有一个**Polygon要素，如果存在多个Polygon要素，根据要素提取后的结果之间会存在连线  
  
  :persevere: 目前从raster提取出来的结果跟原图像比较后发现存在**像元的偏移**，可能是因为给新图像赋予一个新的左上角投影坐标时，未考虑原先图像对应像元的投影坐标，从而产生像元坐标位置偏移
  
> :bookmark: **TODO：**  

:smirk: XML文件处理  

:smirk: 根据矢量文件（如shapefile文件）的范围获取图像对应位置的值并分析

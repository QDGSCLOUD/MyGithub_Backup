
'''
Xrray里面的 DataArray 和 Dataset: 
DataArray 常用属性
    dims:   数据对象每个维度的名字 (例如: lat   ,  lon )
    coords:  每个维度的坐标  :    lat:  90 ~ -90  lon 0~ 360
    values:  实际数据
    attrs:   保存数据的字典( 分辨率, 单位  缺测值 等)
    
    
Dataset:由多个维度相关联的DataArray组成的字典, 常用属性: 
    dims: 数据对象每个维度的名字和长度
    coords: 每个维度的坐标
    attrs: 保存数据的字典
    data_vars: 数据中包含的DataArray 
'''
import  numpy as np
import pandas as pd
import  xarray  as xr
# 下面介绍二进制文件的读写
# 二进制文件最常用的就是   Xrray , 对应的就是 Numpy

exp_data = np.random.randint(0, 40, (3,180, 360))
lat = np.linspace(90, -90 , 180)
lon = np.linspace(0, 360, 360)
time = pd.date_range(start = '2022-01',
                     periods=3,
                     freq='MS')
temp = xr.DataArray(exp_data,
                  dims = ['month', 'latitude', 'longitude'],
                  coords=[time, lat , lon ])


exp_data2_dataset = np.random.randint(50,80, (3,180, 360))
pre =  xr.DataArray(exp_data2_dataset,
                  dims = ['month', 'latitude', 'lontitude'],   # 一定要注意:  dims 和 coords的key 一定要一致.
                  coords= {"month":time, 'latitude':lat, 'lontitude':lon},
                  # coords=[time, lat , lon ])
                    )
ds = xr.Dataset({'teimperature':temp, 'precipitation':pre})    # 相当于将两个 DataArray合并了


# 下面使用DataArray拿出数据
# 通过 sel 拿到指定内容的数据
# print(pre.coords)
# print(pre.values)          # 拿出所有的数据
# print(pre.sel(month="2022-01-01").values)           #
# print(pre.sel(month="2022-01-01",latitude=lat[8],lontitude=lon[0] ).values)  # 注意这里如果填写不正确, 那就报错, all in ....

# 通过loc属性, 结合具体要找的内容, 得到数据
# print(pre.loc[time[1], lat[1],lon[2]].values)

# 按照行索引 寻找数据
# print(pre[1,2,3].values)

# 下面拿出Dataset拿出数据
# print(ds.to_array().values)                      #拿出所有数据, 实际上, 只是能看到所欲的数据而已, 要想拿出纯数据, 使用.to_array()
# print(ds["teimperature"].values)      #拿出temperature 对应的数据
# print(ds.sel(lontitude=slice(10,20)).to_array().values)
# print(ds.loc[dict(month=time[0],  latitude=lat[0], lontitude=lon[0])])    # 一定要用 dict()


# 下面是二进制的读取  # 需要暗账 netCDF4 , eccodes, cfgrib库
# xr.open_dataset(r'绝对路径即可')  # 对于 .nc  .grib   .HDF 等 二进制文件均可

# 下面是二进制文件的写入
# filename.to_netcdf(r"保存路径")

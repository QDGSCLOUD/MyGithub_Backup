import xarray as xr
import os

# # 获取文件夹, 文件名
# general_path = r"F:\CPSv3\\"
# all_dirs = os.listdir(general_path)
# for i_year_fileName in (all_dirs):
#     completed_single_file_path =  os.listdir(general_path+i_year_fileName)

# general_path = r"E:\CPSv3\\"
# all_dirs = os.listdir(general_path)
# for i_year_fileName in (all_dirs):
#     completed_single_file_path =  os.listdir(general_path+i_year_fileName)
#     print(general_path+i_year_fileName)
#     print(len(completed_single_file_path), "\n")


all_data = xr.open_dataset(r"E:\CPSv3\2013\daily_bcccsm_2013010200_PRECT.nc")
print(all_data["long"])



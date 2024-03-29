import cdsapi
import numpy as np
import time

def get_data(i_year,i_month,new_days_list):
    # 开始发送请求
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-land',
        {
            'variable': [
                '2m_temperature', 'total_precipitation',
            ],
            'year': str(i_year),
            'month': str(i_month).zfill(2),
            'day': new_days_list,
            'time': [
                '00:00', '01:00', '02:00', '03:00', '04:00',
                '05:00', '06:00', '07:00', '08:00', '09:00',
                '10:00', '11:00', '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00', '18:00', '19:00',
                '20:00', '21:00', '22:00', '23:00',
            ],
            'area': [
                69.89, 70.2, -9.66, 139.9,
            ],
            'format': 'grib',
        },

        f'{i_year}{i_month}alldays_hourly.grib'
    )
    print("完成一次")


days_list = [
    '01', '02', '03', '04', '05', '06', '07', '08', '09',
    '10', '11', '12', '13', '14', '15', '16', '17', '18',
    '19', '20', '21', '22', '23', '24', '25', '26', '27',
    '28', '29', '30', '31'
]

start_year = 2017
end_year = 2022
start_month = 1
end_month = 12
year_list = np.arange(start_year, end_year + 1)
month_list = np.arange(start_month, end_month + 1)

for i_year in year_list:
    for i_month in month_list:
        # 根据月份判断天数
        if (i_month % 2 == 0 and i_month != 2):  # 假设偶数月除了二月都是30天
            new_days_list = days_list[:-1]
        elif i_month == 2:  # 处理二月
            if i_year % 4 != 0 or (i_year % 100 == 0 and i_year % 400 != 0):  # 非闰年
                new_days_list = days_list[:28]
            else:  # 闰年
                new_days_list = days_list[:29]
        else:  # 奇数月默认31天
            new_days_list = days_list
        print("Hello")
        get_data(i_year, i_month, new_days_list)
        print("完成一次")





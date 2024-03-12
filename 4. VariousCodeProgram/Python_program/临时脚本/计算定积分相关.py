'''
计算定积分  example :

import math
import scipy.integrate as spi
def f(x):
    result = math.exp(x)     # 计算 exp(x) 在 0到 1上的定积分
    return  result
result, error = spi.quad(f,0,1)
print(result, error)

'''



# # 案例1  寻找水仙花
# def get_flower(x):
#     # 判断三位数的水仙花
#     unit = x%10
#     decade = (x//10)%10
#     hundred = x//100
#     criteria = unit**3 + decade**3 + hundred**3
#     if (criteria == x ):
#         print(f"{x}是水仙花数")
#     else:
#         print(f"{x}不是水仙花数")
#     return
#
# if __name__ == '__main__':
#     user_input = input("请输入一个三位数字, 我来判断它是否是水仙花数 \n")
#     get_flower(int(user_input))
#
#




# '''
# 按列2: 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只
# '''
# rooster_cost = 5
# hen_cost = 3
# three_chick_cost  = 1
# for i_rooster in range(1,20):
#     for i_hen in range(1, (94//3)):
#         criteria  = 100 - (i_rooster * rooster_cost + i_hen * hen_cost )
#         if ((criteria % 1) == 0  and criteria > 0 ):
#             print(f"{i_rooster}只公鸡\n ",
#                   f"{i_hen}只母鸡\n ",
#                   f"{criteria * 3}只小鸡\n"
#                    )



'''
求排列组合   C
'''

# 计算阶乘
def get_factorial(n):
    if n==0 or n==1:
        return  1
    else :
        return  n * get_factorial(n-1)

if __name__ == '__main__':
    # 计算C_m ,n
    user_m = int(input("请输入m \n"))
    user_n = int(input("请输入n \n"))
    C_mn = get_factorial(user_m)/(get_factorial(user_m - user_n) * get_factorial(user_n))
    print(C_mn)
















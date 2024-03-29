import numpy as np
# 第一题
# 生成数据
def get_completedNumber():
    pre_numb_list = []
    suf_numb_list = []
    # 获取前区号 ==> 共获得5个
    for i_pre_num in range(5):
        user_pre_num = np.random.randint(1, 36)
        pre_numb_list.append(user_pre_num)

    # 获取后区号 ==> 共获得2个
    for i_suf_num in range(2):
        user_suffix_num = np.random.randint(1, 12)
        suf_numb_list.append(user_suffix_num)

    # 随机生成完整的区域号码
    prefix = np.random.choice(pre_numb_list)
    suffix = np.random.choice(suf_numb_list)
    finalNumber = str(prefix).zfill(2) + str(suffix).zfill(2)
    finalNumber = finalNumber.strip('')
    return finalNumber

if __name__=='__main__':
    # 设置 中间号码
    award_num = 2112
    while True:
        userinput = int(input("输入数字: 1  开始摇号; 否则停止摇号;\n"))
        if (userinput == 1):
            user_number = get_completedNumber()
            print(f"您的号码为{user_number};\n中奖号码为{award_num}")
            if (user_number==award_num):
                print("恭喜中奖\n")
            else:
                print("亲爱的,感谢参与\n")
        else:
            print("结束")
            break

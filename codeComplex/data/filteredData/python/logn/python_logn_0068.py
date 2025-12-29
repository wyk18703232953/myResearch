from math import *
import random

def main(n: int):
    # 1. 根据 n 生成测试数据
    # 这里约定：生成一个区间 [l, r]，其中 0 <= l <= r < 2^n
    # 若 n 过大会导致整数非常大，可按需要调整
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(l, max_val)

    # 2. 将原逻辑封装
    l_bin = list(bin(l)[2:])
    r_bin = list(bin(r)[2:])
    # 前导补零，使得长度一致
    l_bin = ['0' for _ in range(len(r_bin) - len(l_bin))] + l_bin

    s = ""
    for i in range(len(r_bin)):
        if l_bin[i] == r_bin[i]:
            s += "0"
        else:
            s += "1" * (len(r_bin) - i)
            break

    # 3. 输出结果
    print(int(s, 2))

if __name__ == "__main__":
    # 可以在此处指定 n 进行简单测试
    main(10)
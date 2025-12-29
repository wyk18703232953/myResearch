import random
from math import *

mod = 10**9 + 7
mod2 = 998244353

def rec(a, b):
    if b == 1:
        return a
    if a > b:
        return a // b + rec(b, a % b)
    else:
        return rec(b, a)

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里生成两个正整数 a, b，范围与 n 成比例
    upper = max(2, n)
    a = random.randint(1, upper)
    b = random.randint(1, upper)
    # 避免 b 为 0
    if b == 0:
        b = 1

    print(rec(a, b))

if __name__ == "__main__":
    # 默认规模可以自行修改
    main(100)
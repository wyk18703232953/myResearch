import sys
import math
import random

def ss(x):
    return x * (x + 1) // 2

def sol(x):
    if x == 0:
        return 0
    res = ss(x // 2) * 2
    res1 = ss(x) - res
    return res - res1

def main(n):
    # n 作为查询数量，用来生成 n 组 [l, r] 测试数据
    random.seed(0)
    queries = []
    MAX_VAL = 10**12

    for _ in range(n):
        l = random.randint(1, MAX_VAL)
        r = random.randint(l, MAX_VAL)
        queries.append((l, r))

    for l, r in queries:
        print(sol(r) - sol(l - 1))

if __name__ == "__main__":
    # 示例：调用 main(5) 生成 5 组测试数据并输出结果
    main(5)
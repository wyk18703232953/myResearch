from math import sqrt, gcd, ceil, floor, log, factorial
from itertools import permutations, combinations
from collections import Counter, defaultdict
import random

def dist(x1, x2):
    return abs(x1 - x2)

def power2(n):
    if n <= 0:
        return False
    return ceil(log(n, 2)) == floor(log(n, 2))

def main(n):
    # 生成规模为 n 的测试数据
    # 这里生成 n 个在 [-10**9, 10**9] 范围内的随机整数
    random.seed(0)
    x = [random.randint(-10**9, 10**9) for _ in range(n)]

    flag1, flag2 = 0, 0
    d = Counter(x)

    # 尝试找到 3 个数构成等差序列且公差为 2 的幂
    for i in x:
        for po in range(0, 31):
            p2 = 1 << po
            if d[i - p2] > 0 and d[i + p2] > 0:
                print(3)
                print(i, i - p2, i + p2)
                flag1 = 1
                break
        if flag1 == 1:
            break

    # 若没有找到 3 个数，再尝试找 2 个数差值为 2 的幂
    if flag1 == 0:
        for i in x:
            for po in range(0, 31):
                p2 = 1 << po
                if d[i - p2] > 0:
                    print(2)
                    print(i, i - p2)
                    flag2 = 1
                    break
                elif d[i + p2] > 0:
                    print(2)
                    print(i, i + p2)
                    flag2 = 1
                    break
            if flag2 == 1:
                break

        # 若仍未找到，则输出 1 和最大值
        if flag2 == 0:
            print(1)
            print(max(x))

if __name__ == "__main__":
    # 示例：运行 main，n 可根据需要修改
    main(10)
import math

def ss(x):
    return x * (x + 1) // 2

def sol(x):
    if x == 0:
        return 0
    res = ss(x // 2) * 2
    res1 = ss(x) - res
    return res - res1

def main(n):
    # n 表示查询次数 q
    q = n
    # 确定性生成 q 组 [l, r]，使得区间规模随 n 增长
    # 设定一个基础倍数，使 r 约为 2 * n * q 的量级
    base = max(1, n)
    for i in range(1, q + 1):
        l = i * base
        r = (i + 1) * base
        # print(sol(r) - sol(l - 1))
        pass
if __name__ == "__main__":
    main(10)
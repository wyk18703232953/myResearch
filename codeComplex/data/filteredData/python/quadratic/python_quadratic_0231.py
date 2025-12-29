import math
import random

INF = 10**30

def solve_once(n, s, c):
    ans = INF
    for i in range(n):
        mid = s[i]
        mcl = INF
        mrl = INF
        for j in range(i - 1, -1, -1):
            if s[j] < mid:
                mcl = min(mcl, c[j])
        for j in range(i + 1, n):
            if s[j] > mid:
                mrl = min(mrl, c[j])
        ans = min(ans, c[i] + mcl + mrl)
    return -1 if ans == INF else ans

def generate_test_data(n):
    # 生成 n 个随机整数作为 s，范围 1..1e6
    s = [random.randint(1, 10**6) for _ in range(n)]
    # 生成 n 个随机成本，范围 1..1e6
    c = [random.randint(1, 10**6) for _ in range(n)]
    return s, c

def main(n):
    # 根据 n 生成一组测试数据并运行原逻辑
    s, c = generate_test_data(n)
    ans = solve_once(n, s, c)
    print(ans)

if __name__ == "__main__":
    # 示例：可在此处手动指定规模测试
    main(5)
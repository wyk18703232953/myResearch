from math import gcd
import random

def main(n):
    # 1. 生成测试数据
    # 生成 n 个正整数 l[i] 和对应的代价 c[i]
    # 为了有一定概率得到 gcd 为 1 的情况，l[i] 在 1..n 范围内随机
    random.seed(0)  # 固定种子，便于复现
    l = [random.randint(1, max(1, n)) for _ in range(n)]
    c = [random.randint(1, 10) for _ in range(n)]

    # 2. 原始逻辑
    dp = dict()
    for i in range(n):
        if l[i] in dp:
            dp[l[i]] = min(dp[l[i]], c[i])
        else:
            dp[l[i]] = c[i]

    for ll in l:
        keys = list(dp.keys())
        for j in keys:
            g = gcd(j, ll)
            if g in dp:
                dp[g] = min(dp[g], dp[ll] + dp[j])
            else:
                dp[g] = dp[ll] + dp[j]

    if 1 in dp:
        print(dp[1])
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：规模 n 可在此处修改
    main(5)
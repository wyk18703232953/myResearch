import sys
from math import gcd

def main(n):
    # n 表示数组长度规模
    if n <= 0:
        print(-1)
        return

    # 确定性构造 l 和 c
    # l 中元素为正整数，构造方式保证有一定的公因数结构
    l = [i % 10 + 1 for i in range(1, n + 1)]
    c = [i for i in range(1, n + 1)]

    dp = dict()
    for i in range(n):
        x = l[i]
        cost = c[i]
        if x in dp:
            dp[x] = min(dp[x], cost)
        else:
            dp[x] = cost

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
    main(10)
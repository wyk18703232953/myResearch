import math
from collections import defaultdict, deque
import heapq

mod = 998244353


def solve(n, k):
    dp = [[0, 0, 0, 0] for _ in range(k + 3)]
    newdp = [[0, 0, 0, 0] for _ in range(k + 3)]

    dp[1][0] = 1
    dp[1][1] = 1
    dp[2][2] = 1
    dp[2][3] = 1

    for _ in range(n - 1):
        for j in range(k + 1):
            v0, v1, v2, v3 = dp[j]

            # from state 0
            if v0:
                if j + 1 <= k + 2:
                    newdp[j + 1][1] = (newdp[j + 1][1] + v0) % mod
                    newdp[j + 1][2] = (newdp[j + 1][2] + v0) % mod
                    newdp[j + 1][3] = (newdp[j + 1][3] + v0) % mod
                newdp[j][0] = (newdp[j][0] + v0) % mod

            # from state 1
            if v1:
                newdp[j][1] = (newdp[j][1] + v1) % mod
                if j + 1 <= k + 2:
                    newdp[j + 1][3] = (newdp[j + 1][3] + v1) % mod
                    newdp[j + 1][2] = (newdp[j + 1][2] + v1) % mod
                    newdp[j + 1][0] = (newdp[j + 1][0] + v1) % mod

            # from state 2
            if v2:
                newdp[j][1] = (newdp[j][1] + v2) % mod
                newdp[j][2] = (newdp[j][2] + v2) % mod
                newdp[j][0] = (newdp[j][0] + v2) % mod
                if j + 2 <= k + 2:
                    newdp[j + 2][3] = (newdp[j + 2][3] + v2) % mod

            # from state 3
            if v3:
                newdp[j][1] = (newdp[j][1] + v3) % mod
                newdp[j][3] = (newdp[j][3] + v3) % mod
                newdp[j][0] = (newdp[j][0] + v3) % mod
                if j + 2 <= k + 2:
                    newdp[j + 2][2] = (newdp[j + 2][2] + v3) % mod

        dp, newdp = newdp, [[0, 0, 0, 0] for _ in range(k + 3)]

    ans = sum(dp[k]) % mod
    return ans


def main(n):
    # 根据规模 n 生成测试数据，这里简单设定 k = n
    k = n
    res = solve(n, k)
    # print(res)
    pass
if __name__ == "__main__":
    # 示例：可根据需要修改 n 进行测试
    main(5)
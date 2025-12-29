import math
from collections import defaultdict, deque
import heapq


def main(n):
    # 生成测试数据：根据规模 n 构造 k
    # 这里示例设为 k = n，可按需要调整为其他函数关系
    k = n

    mod = 998244353
    dp = [[0, 0, 0, 0] for _ in range(k + 3)]
    dp[1][0] = 1
    dp[1][1] = 1
    dp[2][2] = 1
    dp[2][3] = 1
    newdp = [[0, 0, 0, 0] for _ in range(k + 3)]

    for _ in range(n - 1):
        for j in range(k + 1):
            newdp[j + 1][1] += dp[j][0]
            newdp[j + 1][3] += dp[j][0]
            newdp[j + 1][2] += dp[j][0]
            newdp[j][0] += dp[j][0]

            newdp[j][1] += dp[j][1]
            newdp[j + 1][3] += dp[j][1]
            newdp[j + 1][2] += dp[j][1]
            newdp[j + 1][0] += dp[j][1]

            newdp[j][1] += dp[j][2]
            newdp[j + 2][3] += dp[j][2]
            newdp[j][2] += dp[j][2]
            newdp[j][0] += dp[j][2]

            newdp[j][1] += dp[j][3]
            newdp[j][3] += dp[j][3]
            newdp[j + 2][2] += dp[j][3]
            newdp[j][0] += dp[j][3]

            for a in range(3):
                for b in range(4):
                    newdp[a + j][b] %= mod

        for a in range(k + 3):
            for b in range(4):
                dp[a][b] = newdp[a][b]
                newdp[a][b] = 0

    ans = sum(dp[k]) % mod
    print(ans)


if __name__ == "__main__":
    # 示例调用：可自行修改 n 的值
    main(5)
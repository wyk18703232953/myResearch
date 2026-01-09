import math
from bisect import bisect_left as bl, bisect_right as br, insort
from collections import defaultdict as dd, deque, Counter
from decimal import Decimal

INF = float('inf')
mod = int(1e9) + 7

def main(n):
    # 根据 n 生成测试数据，这里示例为 1..n 的序列，可按需修改
    global a, dp1, dp2, dp3
    a = list(range(1, n + 1))

    dp1 = [[0] * n for _ in range(n)]
    dp2 = [[0] * n for _ in range(n)]
    dp3 = [[0] * n for _ in range(n)]

    def cal(l, r):
        if l == r:
            dp1[l][r] = 1
            dp2[l][r] = a[l]
            return dp1[l][r]
        if dp1[l][r]:
            return dp1[l][r]
        for i in range(l, r):
            if cal(l, i) == 1 and cal(i + 1, r) == 1 and dp2[l][i] == dp2[i + 1][r]:
                dp1[l][r] = 1
                dp2[l][r] = dp2[l][i] + 1
        if not dp2[l][r]:
            dp1[l][r] = 2
        return dp1[l][r]

    def cal2(l, r):
        if dp1[l][r] == 1:
            dp3[l][r] = 1
            return 1
        if dp3[l][r]:
            return dp3[l][r]
        ans = INF
        for i in range(l, r):
            ans = min(cal2(l, i) + cal2(i + 1, r), ans)
        dp3[l][r] = ans
        return ans

    cal(0, n - 1)
    cal2(0, n - 1)
    # print(dp3[0][n - 1])
    pass
if __name__ == "__main__":
    # 示例运行
    main(5)
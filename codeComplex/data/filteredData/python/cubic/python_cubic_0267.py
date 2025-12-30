#!/usr/bin/env python3
import random

def valid(i1, i2, i3):
    if (i1 + i2 + i3) % 2:
        return False
    if i1 < 0 or i2 < 0 or i3 < 0:
        return False
    if i3 > i1 + i2 or i2 > i1 + i3 or i1 > i2 + i3:
        return False
    return True

def main(n):
    """
    n 作为规模参数：
    - 生成三组长度为 n 的随机正整数数组 a1, a2, a3
    - 数值范围为 1..10^6（可按需要修改）
    - 返回算法求得的最大值
    """
    # 1. 生成测试数据
    n1 = n2 = n3 = n
    MAXV = 10**6
    rnd = random.Random(0)  # 固定种子便于复现
    a1 = [rnd.randint(1, MAXV) for _ in range(n1)]
    a2 = [rnd.randint(1, MAXV) for _ in range(n2)]
    a3 = [rnd.randint(1, MAXV) for _ in range(n3)]

    # 2. 按原程序逻辑处理
    a1.sort(reverse=True)
    a2.sort(reverse=True)
    a3.sort(reverse=True)
    a1 = [0] + a1
    a2 = [0] + a2
    a3 = [0] + a3
    n1 += 1
    n2 += 1
    n3 += 1

    dp = [[[-1 for _ in range(n3)] for _ in range(n2)] for _ in range(n1)]
    dp[1][1][0] = a1[1] * a2[1]
    dp[1][0][1] = a1[1] * a3[1]
    dp[0][1][1] = a2[1] * a3[1]
    dp[0][0][0] = -2

    # 用闭包形式的 dfs 以访问 a1, a2, a3, dp
    def dfs(i1, i2, i3):
        # 内联原来的 valid 逻辑
        if (i1 + i2 + i3) % 2 or (i1 < 0 or i2 < 0 or i3 < 0) or \
           i3 > i1 + i2 or i2 > i1 + i3 or i1 > i2 + i3:
            return -2
        if dp[i1][i2][i3] != -1:
            return dp[i1][i2][i3]
        ret1 = dfs(i1 - 1, i2 - 1, i3)
        if ret1 >= 0:
            ret1 += a1[i1] * a2[i2]
        ret2 = dfs(i1 - 1, i2, i3 - 1)
        if ret2 >= 0:
            ret2 += a1[i1] * a3[i3]
        ret3 = dfs(i1, i2 - 1, i3 - 1)
        if ret3 >= 0:
            ret3 += a2[i2] * a3[i3]
        ret = max(ret1, ret2, ret3)
        dp[i1][i2][i3] = ret
        return ret

    for i1 in range(n1):
        for i2 in range(n2):
            for i3 in range(n3):
                dfs(i1, i2, i3)

    ans = -1
    for i1 in range(n1):
        for i2 in range(n2):
            for i3 in range(n3):
                ans = max(ans, dp[i1][i2][i3])

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：使用 n = 5 运行
    main(5)
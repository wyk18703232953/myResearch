import sys
from math import gcd, sqrt
from copy import deepcopy
sys.setrecursionlimit(10**5)

def main(n):
    mod = 10**9 + 7

    # 生成长度为 n 的指令序列，包含 'f' 和 'x'
    # 确定性构造：根据下标奇偶和模运算生成
    cmds = []
    for i in range(n):
        if i % 3 == 0:
            cmds.append('f')

        else:
            cmds.append('x')
    # 确保首个命令不会破坏算法特性
    if n > 0:
        cmds[0] = 'f'

    dp = [[0 for _ in range(n + 5)] for _ in range(n + 5)]
    prev = "-1"

    for i in range(n):
        p = cmds[i]
        if i == 0:
            dp[i][0] = 1

        else:
            c = 0
            if prev == 'f':
                for j in range(n):
                    dp[i][j + 1] = dp[i - 1][j]

            else:
                for j in range(n, -1, -1):
                    c = (c + dp[i - 1][j]) % mod
                    dp[i][j] = c
        prev = p

    result = sum(dp[n - 1]) % mod if n > 0 else 0
    # print(result)
    pass
    return result

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模来做时间复杂度实验
    main(1000)
import random

mod = 10**9 + 7
mod2 = 998244353


def main(n):
    # 生成测试数据：长度为 n 的数组，元素范围可自行调整
    # 为了保持原逻辑合理性，使用正整数（0 会被 (~x and x) 判为 0）
    arr = [random.randint(1, 3) for _ in range(n)]

    # 由于原代码中 dp 是固定 500x500，这里也保持一致
    MAXN = 500
    dp = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
    dp2 = [0 for _ in range(MAXN + 1)]

    # 初始化区间长度为 1 的 dp
    for i in range(n):
        dp[i][i] = arr[i]

    # 计算区间 dp
    i = n - 2
    while ~i:
        j = i + 1
        while j < n:
            dp[i][j] = -1
            for k in range(i, j):
                # 原逻辑: if (~dp[i][k] and dp[i][k]) == dp[k+1][j]:
                # (~x and x) 在 Python 中等价于 (x != -1 and x) 的效果近似，
                # 保持原写法不变
                if (~dp[i][k] and dp[i][k]) == dp[k + 1][j]:
                    dp[i][j] = dp[i][k] + 1
            j += 1
        i -= 1

    # 一维 dp2
    for i in range(1, n + 1):
        dp2[i] = 10**9
        for j in range(i):
            if ~dp[j][i - 1]:
                dp2[i] = min(dp2[i], dp2[j] + 1)

    # 返回结果而不是直接输出，方便外部调用/测试
    return dp2[n]


if __name__ == "__main__":
    # 示例：调用 main(5)
    result = main(5)
    print(result)
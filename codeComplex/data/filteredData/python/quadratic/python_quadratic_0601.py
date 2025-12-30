import random

def main(n):
    # 生成测试数据
    # m 为窗口上限，1 <= m <= n
    m = random.randint(1, n)
    # k 为扣减参数，这里设为 0~10*n 的随机整数
    k = random.randint(0, 10 * n)
    # A 为长度为 n 的整数数组，元素范围 -10^4 ~ 10^4
    A = [random.randint(-10**4, 10**4) for _ in range(n)]

    # 原始逻辑开始
    if n <= m:
        AA = [0] * (n + 1)
        for i in range(n):
            AA[i + 1] = AA[i] + A[i]
        mm = 0
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                mm = max(mm, AA[j] - AA[i] - k)
    else:
        DP = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            a = A[i]
            DP[i + 1][0] = max([DP[i][0], DP[i][m], DP[i][m] + a - k, DP[i][1]])
            DP[i + 1][1] = max(a - k, DP[i][m] + a - k)
            for j in range(2, m + 1):
                DP[i + 1][0] = max(DP[i + 1][0], DP[i][j])
                if j > i + 1:
                    continue
                else:
                    DP[i + 1][j] = max(DP[i][j - 1] + a, DP[i][m] + a - k)

    ans = (max(A[0] - k, 0) if n == 1
           else mm if n <= m
           else max(0, max(DP[n])))
    print(ans)
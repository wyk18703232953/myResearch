# -*- coding: utf-8 -*-

import random

def list2d(a, b, c):
    return [[c] * b for _ in range(a)]

INF = 10 ** 18
MOD = 10 ** 9 + 7

def solve_case(S, T):
    N = len(S)
    M = len(T)

    def check(x):
        T1 = T[:x] + '*'
        T2 = T[x:] + '*'
        m1 = len(T1)
        m2 = len(T2)

        dp = list2d(N + 1, m1, -1)
        dp[0][0] = 0
        for i in range(N):
            s = S[i]
            for j in range(m1):
                k = dp[i][j]
                if k != -1:
                    # skip S[i]
                    if dp[i + 1][j] < k:
                        dp[i + 1][j] = k
                    # match with T1
                    if j < m1 - 1 and T1[j] == s:
                        if dp[i + 1][j + 1] < k:
                            dp[i + 1][j + 1] = k
                    # match with T2
                    if k < m2 - 1 and T2[k] == s:
                        if dp[i + 1][j] < k + 1:
                            dp[i + 1][j] = k + 1
        return dp[N][m1 - 1] == m2 - 1

    for x in range(M):
        if check(x):
            return "YES"
    return "NO"

def generate_test_case(n):
    """
    根据规模 n 生成一组 (S, T)：
    - 字符集使用小写字母
    - |S| ~ n
    - |T| ~ n // 2（至少为 1）
    """
    alphabet = "abc"
    len_S = max(1, n)
    len_T = max(1, n // 2)

    S = "".join(random.choice(alphabet) for _ in range(len_S))
    T = "".join(random.choice(alphabet) for _ in range(len_T))
    return S, T

def main(n):
    """
    n: 规模参数，用于控制字符串长度和测试组数。
    设计：
      - 测试组数 t = max(1, min(10, n))
      - 每组 |S| ≈ n，|T| ≈ n // 2
    """
    random.seed(0)
    t = max(1, min(10, n))
    print(t)
    for _ in range(t):
        S, T = generate_test_case(n)
        print(S)
        print(T)
        # 输出原程序逻辑的结果
        print(solve_case(S, T))

if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)
#!/usr/bin/python3
# @Author  : indiewar (modified to parameterized main(n))

import random
import string


def check(s, t1, t2):
    s1 = len(t1)
    s2 = len(t2)
    n = len(s)
    dp = [[-1] * (s1 + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(s1 + 1):
            if dp[i][j] >= 0:
                if j < s1 and t1[j] == s[i]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
                if dp[i][j] < s2 and t2[dp[i][j]] == s[i]:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + 1)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

    return dp[n][s1] == s2


def solve_one(s, t):
    le = len(t)
    for i in range(le):
        t1 = t[:i]
        t2 = t[i:]
        if check(s, t1, t2):
            print("YES")
            return
    print("NO")


def generate_test_case(n):
    """
    生成单个测试用例 (s, t)。
    这里简单用小写字母随机生成，长度与规模 n 相关：
      |s| = n, |t| = n // 2  (可按需要调整规则)
    """
    alphabet = string.ascii_lowercase
    len_s = max(1, n)
    len_t = max(1, n // 2)

    s = ''.join(random.choice(alphabet) for _ in range(len_s))
    t = ''.join(random.choice(alphabet) for _ in range(len_t))
    return s, t


def main(n):
    """
    n 作为规模参数：
      - 生成 T = n 个测试用例
      - 每个测试用例的 s 长度约为 n，t 长度约为 n//2
    """
    T = n
    for _ in range(T):
        s, t = generate_test_case(n)
        solve_one(s, t)


if __name__ == "__main__":
    # 示例: 以 n = 5 运行
    main(5)
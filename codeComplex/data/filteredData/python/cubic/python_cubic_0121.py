import random
import string

def problem(s, p):
    n = len(s)
    F = [[n] * 26 for _ in range(n + 2)]
    for i in range(n - 1, -1, -1):
        F[i][:] = F[i + 1]
        F[i][ord(s[i]) - 97] = i

    def interleaving(l, r):
        dp = [-1] + [n] * len(r)

        for j in range(1, len(r) + 1):
            dp[j] = F[dp[j - 1] + 1][ord(r[j - 1]) - 97]

        for i in range(1, len(l) + 1):
            dp[0] = F[dp[0] + 1][ord(l[i - 1]) - 97]

            for j in range(1, len(r) + 1):
                a = F[dp[j] + 1][ord(l[i - 1]) - 97]
                b = F[dp[j - 1] + 1][ord(r[j - 1]) - 97]
                dp[j] = min(a, b)

        return dp[-1] < n

    for i in range(len(p)):
        if interleaving(p[:i], p[i:]):
            return 'YES'
    return 'NO'


def main(n):
    """
    生成规模为 n 的测试数据并调用 problem。
    约定：|s| = n，|p| = n（可按需要调整生成策略）。
    """
    # 生成长度为 n 的随机小写字符串 s 和 p
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    p = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 调用原逻辑
    ans = problem(s, p)

    # 输出结果（以及可选的测试数据展示）
    print(ans)
    # 如仅需输出结果，可删去以下两行
    # print("s:", s)
    # print("p:", p)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
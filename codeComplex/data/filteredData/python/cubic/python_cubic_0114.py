def solve(s, t):
    if len(t) == 1:
        if s.count(t[0]):
            return 'YES'
        return 'NO'
    for i in range(1, len(t)):
        dp = [[-1000] * (i + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 0
        for j in range(len(s)):
            dp[j + 1] = dp[j][:]
            for k in range(i + 1):
                if k != i and s[j] == t[k]:
                    dp[j + 1][k + 1] = max(dp[j + 1][k + 1], dp[j][k])
                if abs(dp[j][k] + i) < len(t) and s[j] == t[dp[j][k] + i]:
                    dp[j + 1][k] = max(dp[j + 1][k], dp[j][k] + 1)
        for l in range(len(s) + 1):
            if dp[l][-1] == len(t) - i:
                return 'YES'
    return 'NO'


def main(n):
    """
    n: 生成的测试用例数量
    生成 n 组 (s, t)，调用 solve 并打印结果。
    测试数据策略：
      - 字符集 'abc'
      - s 和 t 的长度在 [1, n+1] 内变化
    """
    import random
    random.seed(0)

    alphabet = "abc"
    for _ in range(n):
        len_s = random.randint(1, n + 1)
        len_t = random.randint(1, n + 1)
        s = "".join(random.choice(alphabet) for _ in range(len_s))
        t = "".join(random.choice(alphabet) for _ in range(len_t))
        print(s, t, solve(s, t))


if __name__ == "__main__":
    # 示例：生成 5 组测试
    main(5)
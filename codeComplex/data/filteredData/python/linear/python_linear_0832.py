import random

def solve_one(n, k, rgb):
    dp = [[0] * (n + 1) for _ in range(3)]
    for i in range(n):
        if rgb[i] == 'R':
            dp[0][i + 1] = dp[2][i]
            dp[1][i + 1] = dp[0][i] + 1
            dp[2][i + 1] = dp[1][i] + 1
        elif rgb[i] == 'G':
            dp[0][i + 1] = dp[2][i] + 1
            dp[1][i + 1] = dp[0][i]
            dp[2][i + 1] = dp[1][i] + 1
        else:  # 'B'
            dp[0][i + 1] = dp[2][i] + 1
            dp[1][i + 1] = dp[0][i] + 1
            dp[2][i + 1] = dp[1][i]

    repl = k
    dif = k % 3
    for j in range(3):
        for i in range(1, n - k + 2):
            repl = min(repl, -dp[j][i - 1] + dp[(j + dif) % 3][i + k - 1])
    return repl


def main(n):
    # 生成测试数据：q 个测试，字符串长度和 k 依据 n 调整
    random.seed(0)
    q = max(1, n // 5)
    results = []
    for _ in range(q):
        length = max(1, n)          # 字符串长度
        k = random.randint(1, length)
        rgb = ''.join(random.choice('RGB') for _ in range(length))
        res = solve_one(length, k, rgb)
        results.append(res)
    # 输出所有测试的答案，每行一个
    for r in results:
        print(r)


if __name__ == "__main__":
    main(10)
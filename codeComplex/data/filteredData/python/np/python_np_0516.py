def main(n: int):
    import random

    # 生成测试数据
    # 约束：k 不宜太大，否则 1<<k 会非常大；这里限定到 7
    k = random.randint(1, min(7, n if n > 0 else 1))
    # 字符串字符从前 k 个字母和 '?' 中随机生成
    chars = [chr(ord('a') + i) for i in range(k)] + ['?']
    s = ''.join(random.choice(chars) for _ in range(n))

    left, right = 0, n
    while left < right:
        mid = right - (right - left) // 2
        A = [[0] * (n + 2) for _ in range(k)]

        for c in range(k):
            A[c][n] = A[c][n + 1] = n + 1
            L = 0
            for i in range(n - 1, -1, -1):
                if s[i] == '?' or ord(s[i]) - ord('a') == c:
                    L += 1
                else:
                    L = 0
                A[c][i] = i + mid if L >= mid else A[c][i + 1]

        dp = [n + 1] * (1 << k)
        dp[0] = 0
        for mask in range(1 << k):
            if dp[mask] > n:
                continue
            for i in range(k):
                if (mask >> i) & 1:
                    continue
                t = mask | (1 << i)
                dp[t] = min(dp[t], A[i][dp[mask]])
        if dp[(1 << k) - 1] <= n:
            left = mid
        else:
            right = mid - 1

    print(left)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
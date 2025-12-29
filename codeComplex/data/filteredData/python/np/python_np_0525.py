def main(n):
    import random
    import string

    # 参数规模设置：字母种类 k 不超过 20，且不超过 n
    k = max(1, min(20, n))

    # 生成测试数据：随机由前 k 个小写字母和 '?' 组成的字符串 s，长度为 n
    letters = string.ascii_lowercase[:k] + "?"
    s = "".join(random.choice(letters) for _ in range(n))

    left, right = 0, n
    while left < right:
        mid = right - (right - left) // 2
        A = [[0] * (n + 2) for _ in range(k)]
        for c in range(k):
            A[c][n] = A[c][n + 1] = n + 1
            L = 0
            for i in range(n - 1, -1, -1):
                if s[i] == '?' or (ord(s[i]) - ord('a') == c):
                    L += 1
                else:
                    L = 0
                if L >= mid:
                    A[c][i] = i + mid
                else:
                    A[c][i + 1]
                    A[c][i] = A[c][i + 1]

        dp = [n + 1] * (1 << k)
        dp[0] = 0
        for mask in range(1 << k):
            if dp[mask] > n:
                continue
            for i in range(k):
                if (mask >> i) & 1:
                    continue
                t = mask | (1 << i)
                pos = A[i][dp[mask]]
                if pos < dp[t]:
                    dp[t] = pos

        if dp[(1 << k) - 1] <= n:
            left = mid
        else:
            right = mid - 1

    print(left)


if __name__ == "__main__":
    # 示例：n 可以根据需要调整
    main(10)
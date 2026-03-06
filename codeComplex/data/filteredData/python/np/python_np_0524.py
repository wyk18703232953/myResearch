def main(n):
    # 映射规则：
    # n: 字符串长度
    # k: 字母种类数，设为 min(5, max(1, n % 6 + 1))，确保 1 <= k <= 6，且随 n 变化
    # 字符串 s 的生成：周期性 'a'..('a'+k-1) 与 '?' 的确定性模式
    k = min(5, max(1, n % 6 + 1))
    if n <= 0:
        print(0)
        return

    chars = [chr(ord('a') + (i % k)) for i in range(k)]
    s_list = []
    for i in range(n):
        if i % (k + 1) == 0:
            s_list.append('?')
        else:
            s_list.append(chars[i % k])
    s = ''.join(s_list)

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
                pos = A[i][dp[mask]]
                if pos < dp[t]:
                    dp[t] = pos
        if dp[(1 << k) - 1] <= n:
            left = mid
        else:
            right = mid - 1
    print(left)


if __name__ == "__main__":
    main(1000)
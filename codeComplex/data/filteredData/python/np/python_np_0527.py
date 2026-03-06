def main(n):
    # Deterministically generate k and s based on n
    # Ensure 1 <= k <= 5 for manageable 2^k complexity
    k = 1 + (n % 5)
    # Generate a string s of length n over 'a'..('a'+k-1) and '?'
    # Pattern: cycle through 0..k (k means '?')
    chars = []
    for i in range(n):
        t = i % (k + 1)
        if t == k:
            chars.append('?')
        else:
            chars.append(chr(ord('a') + t))
    s = ''.join(chars)

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
                if L >= mid:
                    A[c][i] = i + mid
                else:
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
    main(2000)
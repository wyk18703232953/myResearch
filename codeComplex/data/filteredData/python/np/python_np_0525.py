def main(n):
    # 映射规则：
    # n >= 2 时：字符串长度 = n，字母种类 k = min(5, max(1, n // 5))
    # n == 1 时：特殊处理为 n=1, k=1
    if n <= 0:
        return
    if n == 1:
        length = 1
        k = 1
    else:
        length = n
        k = min(5, max(1, n // 5))

    # 确定性构造字符串 s，包含 'a'..'a'+k-1 和 '?' 的循环模式
    chars = [chr(ord('a') + (i % k)) for i in range(k)]
    pattern = chars + ['?']
    plen = len(pattern)
    s = ''.join(pattern[i % plen] for i in range(length))

    left, right = 0, length
    while left < right:
        mid = right - (right - left) // 2
        A = [[0] * (length + 2) for _ in range(k)]
        for c in range(k):
            A[c][length] = A[c][length + 1] = length + 1
            L = 0
            for i in range(length - 1, -1, -1):
                if s[i] == '?' or ord(s[i]) - ord('a') == c:
                    L = L + 1
                else:
                    L = 0
                if L >= mid:
                    A[c][i] = i + mid
                else:
                    A[c][i] = A[c][i + 1]
        dp = [length + 1] * (1 << k)
        dp[0] = 0
        for mask in range(1 << k):
            if dp[mask] > length:
                continue
            for i in range(k):
                if (mask >> i) & 1:
                    continue
                t = mask | (1 << i)
                nxt = A[i][dp[mask]]
                if nxt < dp[t]:
                    dp[t] = nxt
        if dp[(1 << k) - 1] <= length:
            left = mid
        else:
            right = mid - 1

    print(left)


if __name__ == "__main__":
    main(50)
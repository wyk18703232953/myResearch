def main(n):
    # 映射含义：
    # n: 字符串长度
    # k: 字母种类数（固定为 5，且 k <= n 保持有意义）
    k = 5
    if n < k:
        # 对于过小规模，直接输出 0，保持算法行为确定
        print(0)
        return

    # 构造确定性的字符串 s（只包含前 k 个小写字母和若干 '?'）
    # 规则：位置 i (0-based)
    #   - 若 i % (k + 1) == k，则为 '?'
    #   - 否则为 chr(ord('a') + (i % k))
    chars = []
    for i in range(n):
        if i % (k + 1) == k:
            chars.append('?')
        else:
            chars.append(chr(ord('a') + (i % k)))
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
                A[c][i] = i + mid if L >= mid else A[c][i + 1]

        dp = [n + 1] * (1 << k)
        dp[0] = 0
        for mask in range(1 << k):
            for i in range(k):
                if mask >> i & 1:
                    continue
                t = mask | (1 << i)
                dp[t] = min(dp[t], A[i][dp[mask]])
        if dp[-1] <= n:
            left = mid
        else:
            right = mid - 1
    print(left)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 进行规模实验
    main(1000)
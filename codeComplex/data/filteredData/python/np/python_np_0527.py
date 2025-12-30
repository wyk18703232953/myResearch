def main(n):
    # 这里根据 n 生成测试数据
    # 约定：k <= 20（否则 1 << k 过大），随机构造一个长度为 n 的字符串，字符集为前 k 个字母和 '?'
    import random
    import string

    # 简单设定：k 在 [1, min(5, n, 20)] 之间，避免位掩码过大
    k = min(5, max(1, n if n < 5 else 5), 20)

    # 构造测试串 s，含 '?' 和前 k 个小写字母
    chars = list(string.ascii_lowercase[:k]) + ['?']
    s = ''.join(random.choice(chars) for _ in range(n))

    left, right = 0, n
    while left < right:
        mid = right - (right - left) // 2
        # A[c][i] 表示：从位置 i 开始向右找，能够放下长度为 mid 的段，并且段字符为 c 的最左位置的右端点索引
        # 若不能放下，则为 n+1
        A = [[0] * (n + 2) for _ in range(k)]
        for c in range(k):
            A[c][n] = A[c][n + 1] = n + 1
            L = 0
            # 从右往左计算每个字符连续可用长度
            for i in range(n - 1, -1, -1):
                if s[i] == '?' or (ord(s[i]) - ord('a') == c):
                    L += 1
                else:
                    L = 0
                # 如果当前位置开始的连续段长度 >= mid，则在 i 处可以使用 [i, i+mid-1]
                # 否则延用右边的结果
                A[c][i] = i + mid if L >= mid else A[c][i + 1]

        # dp[mask] 为覆盖 mask 中所有字母段后，最靠右的下一个可用位置
        dp = [n + 1] * (1 << k)
        dp[0] = 0
        full_mask = (1 << k) - 1
        for mask in range(1 << k):
            if dp[mask] > n:
                continue
            pos = dp[mask]
            for i in range(k):
                if (mask >> i) & 1:
                    continue
                t = mask | (1 << i)
                nxt = A[i][pos]
                if nxt < dp[t]:
                    dp[t] = nxt

        if dp[full_mask] <= n:
            left = mid
        else:
            right = mid - 1

    print(left)


# 示例：手动调用
if __name__ == "__main__":
    # 例如使用 n = 10 进行一次运行
    main(10)
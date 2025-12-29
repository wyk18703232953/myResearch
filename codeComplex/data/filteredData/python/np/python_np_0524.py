def main(n: int):
    import random

    # 随机生成 k（1~min(8, n)），原题里 k 通常较小，且用了 bitmask(1<<k)
    k = min(8, n) if n > 0 else 1
    if k <= 0:
        print(0)
        return

    # 随机生成长度为 n 的字符串 s，字符集为 'a'..('a'+k-1) 和 '?'
    alphabet = [chr(ord('a') + i) for i in range(k)]
    chars = alphabet + ['?']
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
            for i in range(k):
                # 原代码这里有一个明显笔误：if mask >> k & 1: continue
                # 逻辑应为判断第 i 位是否已被选过
                if (mask >> i) & 1:
                    continue
                t = mask | (1 << i)
                dp[t] = min(dp[t], A[i][dp[mask]])
        if dp[-1] <= n:
            left = mid
        else:
            right = mid - 1
    print(left)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
def main(n):
    # 约定输入结构：
    # - 原程序有两个输入 n, k 和一个长度为 n 的字符串 s
    # - 这里将调用参数 n 映射为原字符串长度
    # - k 固定为 3，代表字符集 {'a', 'b', 'c'}
    # - s 为周期性确定性字符串，由 'a','b','c','?' 构成
    #
    # 这样：
    # - 规模 n 控制字符串长度，便于做时间复杂度实验
    # - k 固定，让状态空间 2^k 稳定，方便比较不同 n 的运行时间

    if n <= 0:
        return 0

    k = 3  # 固定字符种类数量

    # 确定性生成长度为 n 的字符串 s
    # 模式: 0->'a', 1->'b', 2->'c', 3->'?'
    chars = ['a', 'b', 'c', '?']
    s = ''.join(chars[i % 4] for i in range(n))

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
                nxt = A[i][dp[mask]]
                if nxt < dp[t]:
                    dp[t] = nxt
        if dp[(1 << k) - 1] <= n:
            left = mid
        else:
            right = mid - 1
    return left


if __name__ == "__main__":
    # 示例调用：可根据需要调整 n 做实验
    result = main(1000)
    print(result)
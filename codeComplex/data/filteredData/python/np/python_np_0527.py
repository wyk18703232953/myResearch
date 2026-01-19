def main(n):
    # 参数 n 作为字符串长度规模
    # 为了让算法可运行，需要一个合理的 k（不同字符种类数）
    # 这里选择一个与 n 有确定性关系的 k，且限制在 1~5 之间
    k = max(1, min(5, n if n <= 5 else (n % 5) + 1))

    # 构造长度为 n 的字符串 s，字符来自 'a'..'a'+k-1 和 '?'
    # 使用确定性的算术模式生成
    chars = [chr(ord('a') + (i % k)) for i in range(n)]
    # 每隔 (k+1) 个位置设置为 '?'，使得字符串中同时含有普通字符和 '?'
    s_list = []
    period = k + 1
    for i in range(n):
        if i % period == 0:
            s_list.append('?')
        else:
            s_list.append(chars[i])
    s = "".join(s_list)

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
        if dp[-1] <= n:
            left = mid
        else:
            right = mid - 1
    print(left)
    return left

if __name__ == "__main__":
    # 示例：以 n=100 作为输入规模调用
    main(100)
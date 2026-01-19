import sys

def solve(n, k, s):
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
                if mask >> k & 1:
                    continue
                t = mask | (1 << i)
                dp[t] = min(dp[t], A[i][dp[mask]])
        if dp[-1] <= n:
            left = mid
        else:
            right = mid - 1
    return left

def main(n):
    # 映射规则：
    # k = max(1, min(5, n % 6))  保证 1 <= k <= 5，且随 n 变化
    # 字符串长度 = n
    # 字符集 = 前 k 个小写字母 + '?'，按位置 i 确定性生成
    if n <= 0:
        print(0)
        return

    k = n % 6
    if k == 0:
        k = 1
    if k > 5:
        k = 5

    chars = [chr(ord('a') + i) for i in range(k)]
    # 确定性生成长度为 n 的字符串 s
    # 规则：当 i % (k + 1) == k 时为 '?'，否则为 chars[i % k]
    s_list = []
    m = k + 1
    for i in range(n):
        if i % m == k:
            s_list.append('?')
        else:
            s_list.append(chars[i % k])
    s = ''.join(s_list)

    ans = solve(n, k, s)
    print(ans)

if __name__ == "__main__":
    # 示例：使用 n = 100 作为输入规模
    main(100)
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
    # k = max(1, min(20, n % 20 + 1))，保证 1 <= k <= 20
    # 字符串长度 len(s) = n
    # s[i] 在 'a'..('a'+k-1) 与 '?' 中确定性构造
    k = max(1, min(20, n % 20 + 1))
    if n <= 0:
        print(0)
        return
    chars = [chr(ord('a') + (i % k)) for i in range(k)]
    # 构造包含 '?' 的字符串，模式完全确定
    s_list = []
    for i in range(n):
        if i % (k + 1) == 0:
            s_list.append('?')
        else:
            s_list.append(chars[i % k])
    s = ''.join(s_list)
    ans = solve(n, k, s)
    print(ans)

if __name__ == "__main__":
    main(1000)
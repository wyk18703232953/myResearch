from collections import deque

def main(n):
    c = n
    results = []
    for cas in range(c):
        length = max(1, n)
        m = max(1, n // 2 + cas % (n // 2 + 1 if n // 2 + 1 > 0 else 1))
        s_list = [('R', 'G', 'B')[(i + cas) % 3] for i in range(length)]
        s = deque(''.join(s_list))
        arr = ["R", "G", "B"]
        ans = length + 3

        for _ in range(1):
            for i in range(3):
                x = i
                dp = [0 for _ in range(length + 1)]
                for j in range(length):
                    if s[j] != arr[x]:
                        dp[j + 1] += 1
                    dp[j + 1] += dp[j]
                    if j + 1 >= m:
                        ans = min(ans, dp[j + 1] - dp[j + 1 - m])
                    x += 1
                    x = x % 3
        results.append(ans)
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)
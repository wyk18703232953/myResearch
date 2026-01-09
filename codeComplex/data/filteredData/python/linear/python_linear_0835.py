def main(n):
    # Interpret n as the length of the string
    # We fix m deterministically as max(1, n // 2) for scalability
    m = max(1, n // 2)

    # Deterministically generate s using periodic "RGB"
    from collections import deque
    s = deque(('RGB' * ((n // 3) + 1))[:n])

    arr = ["R", "G", "B"]
    ans = n + 3

    for _ in range(1):
        for i in range(3):
            x = i
            dp = [0 for _ in range(n + 1)]
            for j in range(n):
                if s[j] != arr[x]:
                    dp[j + 1] += 1
                dp[j + 1] += dp[j]
                if j + 1 >= m:
                    ans = min(ans, dp[j + 1] - dp[j + 1 - m])
                x += 1
                x = x % 3

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
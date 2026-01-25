from collections import deque

def solve_case(n, m, s):
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
    return ans

def main(n):
    # n controls: number of test cases = n
    # for case idx: length = idx + 3, window m = max(1, (idx % (idx + 3)) + 1)
    results = []
    for cas in range(n):
        length = cas + 3
        m = (cas % length) + 1
        pattern = "RGB"
        s = deque(pattern[i % 3] for i in range(length))
        ans = solve_case(length, m, s)
        results.append(ans)
    for res in results:
        print(res)

if __name__ == "__main__":
    main(5)
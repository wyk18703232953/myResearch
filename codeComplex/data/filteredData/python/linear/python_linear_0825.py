from collections import deque

def solve_case(n, m, s):
    s = deque(s)
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

def generate_case(case_id, n):
    # Interpret n as the string length; window size m is derived deterministically
    length = n if n > 0 else 1
    m = (n // 2) + 1
    if m > length:
        m = length

    base = ["R", "G", "B"]
    s = "".join(base[(i + case_id) % 3] for i in range(length))
    return length, m, s

def main(n):
    # Interpret n as: number of test cases = max(1, n)
    c = n if n > 0 else 1
    for cas in range(c):
        length, m, s = generate_case(cas, n)
        ans = solve_case(length, m, s)
        # print(ans)
        pass
if __name__ == "__main__":
    main(5)
import os
import sys
from io import BytesIO, IOBase

def solve(s, t):
    if len(t) == 1:
        if s.count(t[0]):
            return 'YES'
        return 'NO'
    for i in range(1, len(t)):
        dp = [[-1000] * (i + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 0
        for j in range(len(s)):
            dp[j + 1] = dp[j][:]
            for k in range(i + 1):
                if k != i and s[j] == t[k]:
                    dp[j + 1][k + 1] = max(dp[j + 1][k + 1], dp[j][k])
                if abs(dp[j][k] + i) < len(t) and s[j] == t[dp[j][k] + i]:
                    dp[j + 1][k] = max(dp[j + 1][k], dp[j][k] + 1)
        for l in range(len(s) + 1):
            if dp[l][-1] == len(t) - i:
                return 'YES'
    return 'NO'

def generate_test_case(idx, length):
    s = ''.join(chr(ord('a') + (idx + i) % 26) for i in range(length))
    t = ''.join(chr(ord('a') + (idx * 3 + i * 2) % 26) for i in range(max(1, length // 2)))
    return s, t

def main(n):
    if n <= 0:
        return
    num_tests = n
    base_len = max(1, n // 3)
    for i in range(num_tests):
        length = base_len + i % (base_len + 1)
        s, t = generate_test_case(i, length)
        res = solve(s, t)
        # print(res)
        pass
if __name__ == "__main__":
    main(10)
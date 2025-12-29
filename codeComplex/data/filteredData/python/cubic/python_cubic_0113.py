# Converted version: parameterized main(n), no input(), with test data generation.

import random
from math import inf, isinf

def solve(s, t):
    if len(t) == 1:
        if s.count(t[0]):
            return 'YES'
        return 'NO'
    for i in range(1, len(t)):
        dp = [[-inf] * (i + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 0
        for j in range(len(s)):
            dp[j + 1] = dp[j][:]
            for k in range(i + 1):
                if k != i and s[j] == t[k]:
                    dp[j + 1][k + 1] = max(dp[j + 1][k + 1], dp[j][k])
                if dp[j][k] + i != len(t) and not isinf(dp[j][k]) and s[j] == t[dp[j][k] + i]:
                    dp[j + 1][k] = max(dp[j + 1][k], dp[j][k] + 1)
        for l in range(len(s) + 1):
            if dp[l][-1] == len(t) - i:
                return 'YES'
    return 'NO'


def main(n):
    """
    n: number of test cases to generate and solve.
    Test data generation:
      - Alphabet: lowercase letters a–c (small to keep patterns dense).
      - |s| in [1, 20], |t| in [1, 10].
    """
    random.seed(0)
    alphabet = 'abc'

    for _ in range(n):
        len_s = random.randint(1, 20)
        len_t = random.randint(1, 10)
        s = ''.join(random.choice(alphabet) for _ in range(len_s))
        t = ''.join(random.choice(alphabet) for _ in range(len_t))
        print(solve(s, t))


if __name__ == '__main__':
    # Example: run with 5 auto-generated test cases
    main(5)
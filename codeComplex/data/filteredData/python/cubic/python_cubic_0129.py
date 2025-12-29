# -*- coding: utf-8 -*-

import random
from typing import List


def check(s: List[int], a: List[int], b: List[int], after: List[List[int]]) -> bool:
    ns, na, nb = len(s), len(a), len(b)
    if ns < na + nb:
        return False

    dp = [[0 for _ in range(nb + 1)] for _ in range(na + 1)]
    for i in range(na + 1):
        for j in range(nb + 1):
            if i == 0 and j == 0:
                continue
            pos_a = after[dp[i - 1][j]][a[i - 1]] if i > 0 else ns
            pos_b = after[dp[i][j - 1]][b[j - 1]] if j > 0 else ns
            dp[i][j] = min(pos_a, pos_b) + 1

    return dp[na][nb] <= ns


def solve(s: List[int], t: List[int]) -> str:
    ns = len(s)
    after = [[ns for _ in range(26)] for _ in range(ns + 2)]
    for i in range(ns - 1, -1, -1):
        for j in range(26):
            after[i][j] = after[i + 1][j]
        after[i][s[i]] = i

    for i in range(len(t)):
        a, b = t[:i], t[i:]
        if check(s, a, b, after):
            return 'YES'
    return 'NO'


def main(n: int) -> None:
    """
    n: number of test cases to generate and solve.
    For each test:
      - random length for s in [1, 20]
      - random length for t in [1, 20]
      - characters are 'a'..'z'
    """
    random.seed(0)
    T = n
    ans = []
    for _ in range(T):
        len_s = random.randint(1, 20)
        len_t = random.randint(1, 20)
        s_str = ''.join(chr(ord('a') + random.randint(0, 25)) for _ in range(len_s))
        t_str = ''.join(chr(ord('a') + random.randint(0, 25)) for _ in range(len_t))
        s = [ord(v) - ord('a') for v in s_str]
        t = [ord(v) - ord('a') for v in t_str]
        ans.append(solve(s, t))
    print('\n'.join(ans))


if __name__ == "__main__":
    # Example: run with 5 randomly generated test cases
    main(5)
from collections import defaultdict, Counter, deque
from math import sqrt, log10, log, floor, factorial, gcd
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations

inf = float('inf')
mod = 10 ** 9 + 7
ceil = lambda a, b: (a + b - 1) // b

lim = 22
po = [1 << j for j in range(lim + 1)]
maxbits = lim
masks = po[lim]


def run_logic(l):
    dp = [-1] * masks
    for x in l:
        if 0 <= x < masks:
            dp[x] = x
    for i in range(masks):
        if dp[i] != -1:
            continue
        for j in range(maxbits):
            if i & po[j]:
                dp[i] = dp[i - po[j]]
                break
    ans = []
    full_mask_minus_1 = masks - 1
    for x in l:
        v = x ^ full_mask_minus_1
        if 0 <= v < masks:
            ans.append(dp[v])
        else:
            ans.append(-1)
    return ans


def generate_input_list(n):
    if n <= 0:
        return []
    if n > masks:
        n = masks
    l = [i % masks for i in range(n)]
    return l


def main(n):
    l = generate_input_list(n)
    ans = run_logic(l)
    if ans:
        print(*ans)
    else:
        print()


if __name__ == "__main__":
    main(10)
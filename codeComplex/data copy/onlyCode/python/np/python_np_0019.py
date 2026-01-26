import sys
from array import array  # noqa: F401


def input():
    return sys.stdin.buffer.readline().decode('utf-8')


n = int(input())
prob = [tuple(map(float, input().split())) for _ in range(n)]
full_bit = (1 << n) - 1
dp = [0.0] * full_bit + [1.0]

for bit in range(full_bit, 0, -1):
    popcount = len([1 for i in range(n) if (1 << i) & bit])
    if popcount == 1 or dp[bit] == 0.0:
        continue
    div = 1 / ((popcount * (popcount - 1)) >> 1)

    for i in range(n):
        if ((1 << i) & bit) == 0:
            continue
        for j in range(i + 1, n):
            if ((1 << j) & bit) == 0:
                continue
            dp[bit - (1 << j)] += dp[bit] * prob[i][j] * div
            dp[bit - (1 << i)] += dp[bit] * prob[j][i] * div

print(*(dp[1 << i] for i in range(n)))

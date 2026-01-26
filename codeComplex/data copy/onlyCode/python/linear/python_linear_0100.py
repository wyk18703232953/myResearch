import sys

n = int(sys.stdin.buffer.readline().decode('utf-8'))
cost = [0] + \
    list(map(int, sys.stdin.buffer.readline().decode('utf-8').split()))
a = [line.decode('utf-8').rstrip() for line in sys.stdin.buffer]

mask = [0, 1, 51, 1911]
inf, bs_size, full_bit = 10**9, 1 << 12, (1 << 12) - 1
dp = [[inf]*bs_size for _ in range(4*n+1)]
dp[0][0] = 0

for i in range(4*n):
    y, x = i & 3, i >> 2
    is_dot = 1 if a[y][x] == '.' else 0

    for bitset in range(bs_size):
        if y == 0:
            '''
              01234    01234
            0 s****    .t..*
            1 ***** -> ....*
            2 ***** -> ....*
            3 *****    ....*
            '''
            if dp[i+4][full_bit] > dp[i][bitset] + cost[4]:
                dp[i+4][full_bit] = dp[i][bitset] + cost[4]

        if (is_dot | bitset & 1) and\
                dp[i+1][bitset >> 1] > dp[i][bitset]:
            dp[i+1][bitset >> 1] = dp[i][bitset]

        for k in range(1, min(4-y, 3)+1):
            if dp[i][bitset | mask[k]] > dp[i][bitset] + cost[k]:
                dp[i][bitset | mask[k]] = dp[i][bitset] + cost[k]

print(min(dp[4*n]))

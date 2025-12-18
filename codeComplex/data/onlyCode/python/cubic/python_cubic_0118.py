#!/usr/bin/env python3
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = list(input().rstrip())
    t = input().rstrip()
    ok = False
    for i in range(len(t)):
        t1 = list(t[:i]) + ["#"]
        t2 = list(t[i:]) + ["#"] 
        # dp[seen i-th index][match j in front] = match in back
        dp = [[-1] * (len(t) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 0
        for j, ch in enumerate(s):
            for k in range(len(t1)):
                if dp[j][k] == -1:
                    continue
                dp[j+1][k] = max(dp[j+1][k], dp[j][k])
                if ch == t1[k]:
                    dp[j+1][k+1] = max(dp[j+1][k+1], dp[j][k])
                if ch == t2[dp[j][k]]:
                    dp[j+1][k] = max(dp[j+1][k], dp[j][k] + 1)
        for k in range(len(t) + 1):
            if dp[len(s)][k] + k >= len(t):
                ok = True

    if ok:
        print("YES")
    else:
        print("NO")
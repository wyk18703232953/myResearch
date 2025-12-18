#!/usr/bin/python3
# @Author  : indiewar

def check(s,t1,t2):
    s1 = len(t1)
    s2 = len(t2)
    n = len(s)
    dp = [[-1] * (s1+1) for i in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(s1+1):
            if dp[i][j] >= 0:
                if  j < s1 and t1[j] == s[i]:
                    dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j])
                if dp[i][j] < s2 and t2[dp[i][j]] == s[i]:
                    dp[i+1][j] = max(dp[i+1][j],dp[i][j]+1)
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])

    # print(dp[n][s1])
    if dp[n][s1] == s2:
        return True
    else:
        return False


def solve():
    s = input()
    t = input()
    le = len(t)

    for i in range(le):
        t1 = t[:i]
        t2 = t[i:]
        if check(s,t1,t2) == True:
            print("YES")
            return
    print("NO")


T = int(input())
while T:
    T -= 1
    solve()
#!/usr/bin/env python3

def prdbg(*args, **kwargs):
    # print(*args, **kwargs)
    pass

def valid(i1, i2, i3):
    if (i1 + i2 + i3) % 2 or (i1 < 0 or i2 < 0 or i3 < 0) or i3 > i1 + i2 \
            or i2 > i1 + i3 or i1 > i2 + i3:
        return False
    return True

def dfs(i1, i2, i3, a1, a2, a3, dp):
    if (i1 + i2 + i3) % 2 or (i1 < 0 or i2 < 0 or i3 < 0) or i3 > i1 + i2 \
            or i2 > i1 + i3 or i1 > i2 + i3:
        return -2
    if dp[i1][i2][i3] != -1:
        return dp[i1][i2][i3]
    ret1 = dfs(i1 - 1, i2 - 1, i3, a1, a2, a3, dp)
    if ret1 >= 0:
        ret1 += a1[i1] * a2[i2]
    ret2 = dfs(i1 - 1, i2, i3 - 1, a1, a2, a3, dp)
    if ret2 >= 0:
        ret2 += a1[i1] * a3[i3]
    ret3 = dfs(i1, i2 - 1, i3 - 1, a1, a2, a3, dp)
    if ret3 >= 0:
        ret3 += a2[i2] * a3[i3]
    ret = max(ret1, ret2, ret3)
    dp[i1][i2][i3] = ret
    return ret

def generate_arrays(n):
    if n <= 0:
        return [0], [0], [0]
    base1 = [3 * i + 1 for i in range(n)]
    base2 = [3 * i + 2 for i in range(n)]
    base3 = [3 * i + 3 for i in range(n)]
    a1 = [0] + sorted(base1, reverse=True)
    a2 = [0] + sorted(base2, reverse=True)
    a3 = [0] + sorted(base3, reverse=True)
    return a1, a2, a3

def main(n):
    if n < 1:
        n = 1
    n1 = n
    n2 = n
    n3 = n
    a1, a2, a3 = generate_arrays(n)
    n1 += 1
    n2 += 1
    n3 += 1
    dp = [[[-1 for _ in range(n3)] for _ in range(n2)] for _ in range(n1)]
    if n1 > 1 and n2 > 1:
        dp[1][1][0] = a1[1] * a2[1]
    if n1 > 1 and n3 > 1:
        dp[1][0][1] = a1[1] * a3[1]
    if n2 > 1 and n3 > 1:
        dp[0][1][1] = a2[1] * a3[1]
    dp[0][0][0] = -2
    for i1 in range(n1):
        for i2 in range(n2):
            for i3 in range(n3):
                dfs(i1, i2, i3, a1, a2, a3, dp)
    ans = -1
    for i1 in range(n1):
        for i2 in range(n2):
            for i3 in range(n3):
                ans = max(ans, dp[i1][i2][i3])
    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    main(3)
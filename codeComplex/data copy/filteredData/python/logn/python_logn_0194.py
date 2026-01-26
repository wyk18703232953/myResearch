import bisect
from math import log, gcd, atan2, acos

mod = 10**9 + 7
mod1 = 998244353
gp = []
cost = []
dp = []
mx = []
ans1 = []
ans2 = []
special = []
specnode = []
a = 0
kthpar = []
ans = 0
b = []


def dfs(root, par):
    global dp, gp, kthpar
    if par != -1:
        dp[root] = dp[par] + 1
    for i in range(1, 20):
        if kthpar[root][i-1] != -1:
            kthpar[root][i] = kthpar[kthpar[root][i-1]][i-1]
    for child in gp[root]:
        if child == par:
            continue
        kthpar[child][0] = root
        dfs(child, root)


def dfs2(root, par, d):
    global gp, dp
    dp[root] = d
    for child in gp[root]:
        if child == par:
            continue
        dfs2(child, root, d + 1)


def hnbhai_param(n, s):
    low = s
    high = n + 1
    ans_local = n + 1
    while low <= high:
        mid = (low + high) // 2
        ss = sum(int(ch) for ch in str(mid))
        if mid - ss < s:
            low = mid + 1

        else:
            ans_local = mid
            high = mid - 1
    return n - ans_local + 1


def main(n):
    # Interpret n as the scale of the problem: choose a deterministic (n, s) pair.
    # Ensure n >= 1
    if n < 1:
        n_local = 1

    else:
        n_local = n
    # Deterministic choice of s: some fraction of n, at least 1
    s_local = max(1, n_local // 2)
    result = hnbhai_param(n_local, s_local)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
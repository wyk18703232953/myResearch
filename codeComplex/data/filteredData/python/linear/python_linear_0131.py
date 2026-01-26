import math
from functools import cmp_to_key

mod = 1000000007
f = []

def fact(n, m):
    global f
    f = [1 for _ in range(n + 1)]
    f[0] = 1
    for i in range(1, n + 1):
        f[i] = (f[i - 1] * i) % m

def fast_mod_exp(a, b, m):
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b = b >> 1
    return res

def inverseMod(n, m):
    return fast_mod_exp(n, m - 2, m)

def ncr(n, r, m):
    if n < 0 or r < 0 or r > n:
        return 0
    if r == 0:
        return 1
    return ((f[n] * inverseMod(f[n - r], m)) % m * inverseMod(f[r], m)) % m

def getCount(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1
    return count

def solve_C(n_str, k):
    if k == 0:
        return 1
    dp = [0 for _ in range(1010)]
    for i in range(1010):
        if i == 0 or i == 1:
            continue
        dp[i] = dp[getCount(i)] + 1
    fact(1010, mod)

    ans = 0
    s = n_str
    count = 0
    for i in range(len(s)):
        if s[i] == '0':
            continue
        for j in range(max(count, 1), 1010):
            if dp[j] == k - 1:
                ans = (ans + ncr(len(s) - i - 1, j - count, mod)) % mod
                if i == 0 and k == 1:
                    ans = (ans + mod - 1) % mod
        count += 1
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
    if dp[count] == k - 1:
        ans = (ans + 1) % mod
    return ans

def main(n):
    # 映射规则：
    # n -> 输入规模
    # - 二进制字符串长度 = n
    # - k 在 1..min(n,20) 区间内确定性取值
    # 构造二进制字符串：周期性 "1010..."，长度为 n
    if n <= 0:
        # print(0)
        pass
        return
    s = "".join('1' if i % 2 == 0 else '0' for i in range(n))
    # k 的确定性选择：在 1..20 中循环
    k = (n % 20) + 1
    ans = solve_C(s, k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可自行修改 n 观察规模变化
    main(10)
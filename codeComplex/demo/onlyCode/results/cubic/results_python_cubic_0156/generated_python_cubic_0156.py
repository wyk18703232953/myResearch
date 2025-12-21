def examA(n):
    T = n
    ans = []
    for _ in range(T):
        N = random.randint(1, 10**6)
        M = random.randint(1, 10**6)
        if N % M != 0:
            ans.append("NO")
        else:
            ans.append("YES")
    return ans

def examB(n):
    T = n
    ans = []
    for _ in range(T):
        N = n
        A = [random.randint(0, 10**9) for _ in range(N)]
        A.sort()
        ans.append(A[::-1])
    return ans

def examC(n):
    T = n
    ans = []
    for _ in range(T):
        N = n
        K = random.randint(1, 5)
        A = [random.randint(-10, 10) for _ in range(N)]
        sumA = sum(A)
        if sumA == 0:
            ans.append("YES")
            continue
        cur = 0
        L = []
        for i in range(100):
            now = K ** i
            L.append(now)
            cur += now
            if cur >= sumA:
                break
        for i in range(N):
            A[i] *= -1
        heapify(A)
        for l in L[::-1]:
            if not A:
                break
            a = -heappop(A)
            if a < l:
                heappush(A, -a)
            elif a > l:
                heappush(A, -(a - l))
        if not A or heappop(A) == 0:
            ans.append("YES")
        else:
            ans.append("NO")
    return ans

def examD(n):
    class combination():
        def __init__(self, n, mod):
            self.n = n
            self.fac = [1] * (n + 1)
            self.inv = [1] * (n + 1)
            for j in range(1, n + 1):
                self.fac[j] = self.fac[j - 1] * j % mod
            self.inv[n] = pow(self.fac[n], mod - 2, mod)
            for j in range(n - 1, -1, -1):
                self.inv[j] = self.inv[j + 1] * (j + 1) % mod
        def comb(self, n, r, mod):
            if r > n or n < 0 or r < 0:
                return 0
            return self.fac[n] * self.inv[n - r] * self.inv[r] % mod
    N = max(2, n)
    M = max(N, n * 2)
    ans = 0
    if N == 2:
        return ans
    C = combination(M, mod2)
    for i in range(N - 1, M + 1):
        cur = pow(2, N - 3, mod2) * (i - 1) * C.comb(i - 2, N - 3, mod2)
        ans += cur
        ans %= mod2
    return ans

def examE(n):
    N = n
    A = [random.randint(1, 3) for _ in range(N)]
    dp = [[-1] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        dp[i][i + 1] = A[i]
    for l in range(2, N + 1):
        for i in range(N - l + 1):
            for k in range(i + 1, i + l):
                if dp[i][k] >= 1 and dp[i][k] == dp[k][i + l]:
                    dp[i][i + l] = dp[i][k] + 1
    L = [inf] * (N + 1)
    for i in range(1, N + 1):
        if dp[0][i] >= 1:
            L[i] = 1
    for i in range(N):
        for k in range(1, N - i + 1):
            if dp[i][i + k] >= 1:
                L[i + k] = min(L[i + k], L[i] + 1)
    ans = L[N]
    return ans

def examF(n):
    ans = 0
    return ans

import sys, copy, bisect, itertools, heapq, math, random
from heapq import heappop, heappush, heapify
from collections import Counter, defaultdict, deque
global mod, mod2, inf, alphabet, _ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

def main(n):
    resE = examE(n)
    print(resE)

if __name__ == '__main__':
    main(5)
def examA():
    T = I()
    ans = []
    for _ in range(T):
        N, M = LI()
        if N%M!=0:
            ans.append("NO")
        else:
            ans.append("YES")
    for v in ans:
        print(v)
    return

def examB():
    T = I()
    ans = []
    for _ in range(T):
        N = I()
        A = LI()
        A.sort()
        ans.append(A[::-1])
    for v in ans:
        print(" ".join(map(str,v)))
    return

def examC():
    T = I()
    ans = []
    for _ in range(T):
        N, K = LI()
        A = LI()
        sumA = sum(A)
        if sumA==0:
            ans.append("YES")
            continue
        cur = 0
        L = []
        for i in range(100):
            now = K**i
            L.append(now)
            cur += now
            if cur>=sumA:
                break
        for i in range(N):
            A[i] *= (-1)
        heapify(A)
        #print(A)
        for l in L[::-1]:
            if not A:
                break
            a = -heappop(A)
            if a<l:
                heappush(A, -a)
            elif a>l:
                heappush(A,-(a-l))
        if not A or heappop(A)==0:
            ans.append("YES")
        else:
            ans.append("NO")
    for v in ans:
        print(v)
    return

def examD():
    class combination():
        # 素数のmod取るときのみ　速い
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
    N, M = LI()
    ans = 0
    if N==2:
        print(ans)
        return
    C = combination(M,mod2)
    for i in range(N-1,M+1):
        cur = pow(2,N-3,mod2) * (i-1) * C.comb(i-2,N-3,mod2)
        #print(cur)
        ans += cur
        ans %= mod2
    print(ans)
    return

def examE():
    N = I()
    A = LI()
    dp = [[-1]*(N+1) for _ in range(N+1)]
    for i in range(N):
        dp[i][i+1] = A[i]
    for l in range(2, N + 1):
        for i in range(N - l + 1):
            for k in range(i + 1, i + l):
                if dp[i][k] >= 1 and dp[i][k] == dp[k][i+l]:
                    dp[i][i + l] = dp[i][k] + 1

    L = [inf]*(N+1)
    for i in range(1,N+1):
        if dp[0][i]>=1:
            L[i] = 1
    for i in range(N):
        for k in range(1, N - i + 1):
            if dp[i][i + k] >= 1:
                L[i + k] = min(L[i + k], L[i] + 1)
    #print(dp)
    #print(L)
    ans = L[N]
    print(ans)
    return
"""
5
1 1 2 3 4
"""

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examE()

"""

"""
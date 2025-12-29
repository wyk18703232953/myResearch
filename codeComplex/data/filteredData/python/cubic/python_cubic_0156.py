import random
import math
from heapq import heappop, heappush, heapify
from collections import Counter, defaultdict, deque

mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]


def examA_generate(n):
    # 规模 n: 生成 T=n 组 (N, M)
    T = n
    cases = []
    for _ in range(T):
        M = random.randint(1, max(1, n))
        # 保证既有能整除也有不能整除的情况
        if random.random() < 0.5:
            k = random.randint(0, n)
            N = M * k
        else:
            N = random.randint(0, n)
        cases.append((N, M))
    return T, cases


def examA_run(T, cases):
    ans = []
    for i in range(T):
        N, M = cases[i]
        if M == 0 or N % M != 0:
            ans.append("NO")
        else:
            ans.append("YES")
    return ans


def examB_generate(n):
    # 规模 n: T=n 组，每组 N 随机，数组长度约为 n/2
    T = n
    cases = []
    for _ in range(T):
        N = random.randint(1, max(1, n))
        A = [random.randint(-n, n) for _ in range(N)]
        cases.append((N, A))
    return T, cases


def examB_run(T, cases):
    ans = []
    for i in range(T):
        N, A = cases[i]
        A = A[:]  # avoid modifying input
        A.sort()
        ans.append(A[::-1])
    return ans


def examC_generate(n):
    # 规模 n: T=n 组
    # N: 1..min(10, n), K: 1..5, A: sum magnitude about n
    T = n
    cases = []
    for _ in range(T):
        N = random.randint(1, min(10, n if n > 0 else 1))
        K = random.randint(1, 5)
        A = [random.randint(0, n) for _ in range(N)]
        cases.append((N, K, A))
    return T, cases


def examC_run(T, cases):
    ans = []
    for _ in range(T):
        N, K, A = cases[_]
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
        A = A[:]
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


def examD_generate(n):
    # 单组 (N, M)，N<=min(10,n+2) 保证可算
    N = random.randint(2, min(10, n + 2 if n > 0 else 4))
    M = random.randint(N - 1, max(N, n + 2))
    return N, M


def examD_run(N, M):
    class combination:
        # 只在模为素数时使用
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

    ans = 0
    if N == 2:
        return ans
    C = combination(M, mod2)
    for i in range(N - 1, M + 1):
        cur = pow(2, N - 3, mod2) * (i - 1) * C.comb(i - 2, N - 3, mod2)
        ans += cur
        ans %= mod2
    return ans


def examE_generate(n):
    # N = n，A 中元素为 1..3
    N = max(1, n)
    A = [random.randint(1, 3) for _ in range(N)]
    return N, A


def examE_run(N, A):
    dp = [[-1] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        dp[i][i + 1] = A[i]
    for l in range(2, N + 1):
        for i in range(N - l + 1):
            for k in range(i + 1, i + l):
                if dp[i][k] >= 1 and dp[i][k] == dp[k][i + l]:
                    dp[i][i + l] = dp[i][k] + 1

    L = [inf] * (N + 1)
    L[0] = 0
    for i in range(1, N + 1):
        if dp[0][i] >= 1:
            L[i] = 1
    for i in range(N):
        if L[i] == inf:
            continue
        for k in range(1, N - i + 1):
            if dp[i][i + k] >= 1:
                L[i + k] = min(L[i + k], L[i] + 1)
    ans = L[N]
    return ans


def examF_run():
    ans = 0
    return ans


def main(n):
    # 根据原始脚本，默认执行 examE 的逻辑，
    # 但这里也演示其它子题的调用方式。
    N, A = examE_generate(n)
    ansE = examE_run(N, A)
    print(ansE)


if __name__ == '__main__':
    # 示例：规模参数可以在这里修改
    main(5)
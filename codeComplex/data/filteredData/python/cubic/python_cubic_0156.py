import copy, bisect, itertools, heapq, math
from heapq import heappop, heappush, heapify
from collections import Counter, defaultdict, deque

mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]


def examA(T, NM_pairs):
    ans = []
    for i in range(T):
        N, M = NM_pairs[i]
        if N % M != 0:
            ans.append("NO")

        else:
            ans.append("YES")
    for v in ans:
        # print(v)
        pass
    return


def examB(T, Ns, As):
    ans = []
    for t in range(T):
        A = As[t][:]
        A.sort()
        ans.append(A[::-1])
    for v in ans:
        # print(" ".join(map(str, v)))
        pass
    return


def examC(T, NK_list, As_list):
    ans = []
    for t in range(T):
        N, K = NK_list[t]
        A = As_list[t][:]
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
        if (not A) or heappop(A) == 0:
            ans.append("YES")

        else:
            ans.append("NO")
    for v in ans:
        # print(v)
        pass
    return


def examD(N, M):
    class combination():
        def __init__(self, n, mod_):
            self.n = n
            self.fac = [1] * (n + 1)
            self.inv = [1] * (n + 1)
            for j in range(1, n + 1):
                self.fac[j] = self.fac[j - 1] * j % mod_
            self.inv[n] = pow(self.fac[n], mod_ - 2, mod_)
            for j in range(n - 1, -1, -1):
                self.inv[j] = self.inv[j + 1] * (j + 1) % mod_

        def comb(self, n, r, mod_):
            if r > n or n < 0 or r < 0:
                return 0
            return self.fac[n] * self.inv[n - r] * self.inv[r] % mod_

    ans = 0
    if N == 2:
        # print(ans)
        pass
        return
    C = combination(M, mod2)
    for i in range(N - 1, M + 1):
        cur = pow(2, N - 3, mod2) * (i - 1) * C.comb(i - 2, N - 3, mod2)
        ans += cur
        ans %= mod2
    # print(ans)
    pass
    return


def examE(N, A):
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
                if L[i] + 1 < L[i + k]:
                    L[i + k] = L[i] + 1
    ans = L[N]
    # print(ans)
    pass
    return


def examF():
    ans = 0
    # print(ans)
    pass
    return


def main(n):
    # n controls overall scale.
    # Define per-exam sizes deterministically from n.
    T_A = max(1, n // 5)
    T_B = max(1, n // 5)
    T_C = max(1, n // 5)

    # examA: generate T_A pairs (N, M) with values depending on n and index
    NM_pairs = []
    for i in range(T_A):
        N = (i + 1) * (n + 2)
        M = (i % 7) + 1
        NM_pairs.append((N, M))

    # examB: each test has length L_B = max(1, n // 10)
    L_B = max(1, n // 10)
    Ns_B = []
    As_B = []
    for t in range(T_B):
        Ns_B.append(L_B)
        arr = [(t + 1) * (i + 1) % (n + 10) for i in range(L_B)]
        As_B.append(arr)

    # examC: each test has N_C elements, K depends on t
    T_C = max(1, n // 5)
    N_C = max(1, n // 10)
    NK_list = []
    As_C = []
    for t in range(T_C):
        N = N_C
        K = 2 + (t % 5)
        NK_list.append((N, K))
        A = [((i + 1) * (t + 3)) % (n + 20) for i in range(N)]
        As_C.append(A)

    # examD: choose N, M based on n
    N_D = max(3, n // 5)
    M_D = N_D + max(1, n // 7)

    # examE: N_E = n, array constructed deterministically
    N_E = max(1, n)
    A_E = [((i // 2) % 3) + 1 for i in range(N_E)]

    # Call exams sequentially
    examA(T_A, NM_pairs)
    examB(T_B, Ns_B, As_B)
    examC(T_C, NK_list, As_C)
    examD(N_D, M_D)
    examE(N_E, A_E)
    examF()


if __name__ == "__main__":
    main(50)
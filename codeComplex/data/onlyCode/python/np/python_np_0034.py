import sys
readline = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def prsh(N):
    prime = [2]
    for L in range(3,N):
        for p in prime:
            if not L % p:
                break
            if p > L**(1/2):
                prime.append(L)
                break
    return prime
limit = 59
prime = prsh(limit+1)
C = set([tuple()])
Cp = []
for i in range(2, limit+1):
    if i >= 30 and i in prime:
        Cp.append(i)
        continue
    for k in C.copy():
        if all(gcd(ki, i) == 1 for ki in k):
            kn = tuple(list(k) + [i])
            C.add(kn)

INF = 10**9+7

N = int(readline())
A = list(map(int, readline().split()))
Ao = A[:]
A.sort()
ans = INF
Ans = None
for ci in C:
    tc = [1]*(N-len(ci)) + list(ci) + Cp
    for j in range(8):
        res = 0
        for a, t in zip(A, tc[j:]):
            res += abs(a-t)
        if ans > res:
            ans = res
            Ans = tc[j:j+N]
buc = [[] for _ in range(limit+1)]
for a, an in zip(A, Ans):
    buc[a].append(an)
AA = []
for ao in Ao:
    AA.append(buc[ao].pop())

#print(ans)
print(*AA)
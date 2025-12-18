import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())


N = I()
A = LI()
mod = 10**9+7

m = 20
M = 1 << m
F = [0]*M
for a in A:
    F[a] += 1


def zeta_transform(F,n):
    # res[i] = (iを含む集合jに対する F[j] の和)
    N = 1 << n
    res = F[:]
    for i in range(n):
        k = 1 << i
        for j in range(N):
            if not j & k:
                res[j] += res[j^k]
    return res


G = zeta_transform(F,m)
power = [1]
for _ in range(N):
    power.append((power[-1]*2) % mod)


def bit_count(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c


ans = 0
for i in range(M):
    bc = bit_count(i)
    a = power[G[i]]
    if bc % 2 == 0:
        ans += a
    else:
        ans -= a
    ans %= mod

print(ans)

import sys
from math import ceil, floor, factorial

def swaparr(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def nCr(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)

def upper_bound(a, x, lo=0):
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def primefs(n):
    primes = {}
    while n % 2 == 0:
        primes[2] = primes.get(2, 0) + 1
        n = n // 2
    i = 3
    limit = int(n ** 0.5) + 2
    while i < limit:
        while n % i == 0:
            primes[i] = primes.get(i, 0) + 1
            n = n // i
        i += 2
    if n > 2:
        primes[n] = primes.get(n, 0) + 1
    return primes

def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def find(x, link):
    p = x
    while p != link[p]:
        p = link[p]
    while x != p:
        nex = link[x]
        link[x] = p
        x = nex
    return p

def union(x, y, link, size):
    x = find(x, link)
    y = find(y, link)
    if size[x] < size[y]:
        x, y = swap(x, y)
    if x != y:
        size[x] += size[y]
        link[y] = x

def sieve(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            i = p * p
            while i <= n:
                prime[i] = False
                i += p
        p += 1
    return prime

MAXN = int(1e6 + 5)
spf = [0 for _ in range(MAXN)]

def spf_sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
    i = 3
    limit = ceil(MAXN ** 0.5)
    while i < limit:
        if spf[i] == i:
            j = i * i
            while j < MAXN:
                if spf[j] == j:
                    spf[j] = i
                j += i
        i += 2

def factoriazation(x):
    ret = {}
    while x != 1:
        ret[spf[x]] = ret.get(spf[x], 0) + 1
        x = x // spf[x]
    return ret

MOD = int(1e9) + 7
CMOD = 998244353
INF = float('inf')
NINF = -float('inf')

def run_core(n, l, r, x, a):
    ans = 0
    for mask in range(1 << n):
        mx = NINF
        mn = INF
        sub = 0
        for i in range(n):
            if (1 << i) & mask:
                sub += a[i]
                v = a[i]
                if v > mx:
                    mx = v
                if v < mn:
                    mn = v
        if sub >= l and sub <= r:
            if mx - mn >= x:
                ans += 1
    return ans

def main(n):
    if n <= 0:
        print(0)
        return
    if n > 20:
        n = 20
    l = n * (n + 1) // 4
    r = n * (n + 1) // 2
    x = max(1, n // 3)
    a = [i + 1 for i in range(n)]
    ans = run_core(n, l, r, x, a)
    print(ans)

if __name__ == "__main__":
    main(10)
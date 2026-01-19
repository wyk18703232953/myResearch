import math
from collections import defaultdict as dd

mod = int(1e9) + 7

def cal(x, n, m, A):
    l1 = set()
    d = dd(int)
    a = []
    for i in range(n):
        k = 0
        for j in range(m):
            if A[i][j] >= x:
                k += 1 << j
        l1.add(k)
        d[k] = i + 1
    l1 = list(l1)
    s = (1 << m) - 1
    for i in l1:
        for j in l1:
            if i | j == s:
                a = [d[i], d[j]]
    return a

def main(n):
    if n <= 0:
        return
    m = max(1, min(20, n))
    N = n
    A = [[(i + 1) * (j + 2) for j in range(m)] for i in range(N)]
    left, right = 0, 10**9
    last_mid = 0
    while left <= right:
        mid = (left + right) // 2
        last_mid = mid
        if cal(mid, N, m, A):
            left = mid + 1
        else:
            right = mid - 1
    a = cal(last_mid, N, m, A)
    if a:
        print(a[0], a[1])
    else:
        b = cal(last_mid - 1, N, m, A)
        if b:
            print(b[0], b[1])

if __name__ == "__main__":
    main(5)
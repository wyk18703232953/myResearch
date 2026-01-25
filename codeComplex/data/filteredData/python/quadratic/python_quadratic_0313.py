import sys
from bisect import *

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
M = 998244353
EPS = 1e-6

def Ceil(a, b):
    return a // b + int(a % b > 0)

def run_algorithm(n, k, a):
    ans = 0
    for i in range(n - k + 1):
        num = sum(a[i:i + k])
        den = k
        ans = max(ans, num / den)
        for j in range(i + k, n):
            num += a[j]
            den += 1
            ans = max(ans, num / den)
    return ans

def main(n):
    if n < 2:
        n = 2
    k = max(1, n // 2)
    a = [(i * 7 + 3) % 1000 for i in range(n)]
    result = run_algorithm(n, k, a)
    print(result)

if __name__ == "__main__":
    main(10)
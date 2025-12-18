import string
from collections import deque, Counter
from functools import lru_cache
import math

DEBUG = 0

def main():
    # @lru_cache(400*2*2)
    # def search(n, l_on, r_on):
    #     nonlocal M
    #     if n == 0: return 1
    #     if l_on and r_on and n == 1: return 1
    #     if n == 1: return 1
    #     if r_on and not l_on: return search(n, r_on, l_on)

    #     total = 0
    #     for i in range(n):
    #         total += search(n=i, l_on=l_on, r_on=True) * search(n=n-i-1, l_on=True, r_on=r_on) * comb(n-1, i) % M
    #     # print(l_on,  n, r_on, '=>', total)
    #     return total



    T = 1
    while T:
        n, M = Input.read_typed(int)
        N = n


        f = [[0 for _ in range(n+1)] for _ in range(n+1)]
        comb = [[0 for _ in range(n+1)] for _ in range(n+1)]
        fact = [0] * (n+1)
        inv = [0] * (n+1)
        fact[0] = inv[0] = 1

        for i in range(1, n+1):
            fact[i] = (fact[i-1] * i) % M
            inv[i] = pow(fact[i], M-2, M)

        for i in range(0, n+1):
            for j in range(0, i+1):
                # comb[i][j] = fact[i]//(fact[j] * fact[i-j]) % M;
                comb[i][j] = ((fact[i] * inv[j]) % M * inv[i-j]) % M
                # print(i, j, '=>', math.comb(i, j) %M, comb[i][j])
                # assert math.comb(i, j) % M == comb[i][j]

        pow2 = [0] * (n+1)
        pow2[0] = 1
        for i in range(1, n+1):
            pow2[i] = pow2[i-1]*2 % M 
            f[i][i] = pow2[i-1]

        for total in range(1, n+1):
            for manual in range(1, total):
                if total > manual * 2 or total < manual: continue
                for l in range(1, manual):
                    f[total][manual] += f[total-l-1][manual-l] * pow2[l-1] * comb[manual][l]
                    # f[total][manual] += f[total-l-1][manual-l] * pow(2, l-1, mod=M) * math.comb(manual, l)
                    f[total][manual] %= M

        c = 0
        for i in range(1, n+1):
            c += f[n][i]
            # print(n, i)
            # print(f[n][i])
        print(c % M)
        T -= 1 


# Helper classes
class Input:
    def __init__(self):
        pass

    @staticmethod
    def read_typed(cls):
        return list(map(cls, input().split()))

    @staticmethod
    def read():
        return input()

class Debug():
    def __init__(self):
        import sys
        sys.stdout = open('output.out', 'w')
        sys.stdin = open('input.in', 'r')

    def __delete__(self):
        sys.stdout.close()
        sys.stdin.close()

def run():
    if DEBUG: _ = Debug()
    main()

run()

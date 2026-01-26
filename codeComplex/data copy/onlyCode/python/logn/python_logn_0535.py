# @author 

import sys

class ADigitsSequenceEasyEdition:
    def solve(self):
        k = int(input()) + 1
        p = 1
        c = 0
        while c + p * (10 ** p - (10 ** (p - 1) if p > 1 else 0)) < k:
            c += p * (10 ** p - (10 ** (p - 1) if p > 1 else 0))
            p += 1
        k -= c
        bef = (10 ** (p - 1) if p > 1 else 0) + (k - 1) // p
        print(str(bef)[(k - 1) % p], end='')


solver = ADigitsSequenceEasyEdition()
input = sys.stdin.readline

solver.solve()

#  author: ThePonyCoder
#  created: 24.06.2019, 10:58
#  filename: g1.py
#  path: E:/Projects/CodeForces/rounds/cf_568/g1.py

import os

# import random

# sys.setrecursionlimit(999999999)
import string

from math import inf
from functools import lru_cache

if os.getcwd() == 'C:\\Users\\User\\Desktop\\python\\Prog\\CodeForces' \
        or os.environ['COMPUTERNAME'] == 'RYZEN':
    import pdb
    
    import sys
    
    pdb = pdb.Pdb(stdin=sys.stdin, stdout=sys.stdout)
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    from pprint import pprint
    from hypothesis import given, settings
    from hypothesis import strategies as st


def ri():
    return [int(i) for i in input().split()]


MOD = int(1e9 + 7)


def main():
    n, t = ri()
    songs = []
    result = 0
    for i in range(n):
        songs.append(ri())  # [время, жанр]
        songs[-1][1] -= 1
    
    dp = [[0, 0, 0] for i in range(1 << n)]
    
    for ind, it in enumerate(songs):
        dp[1 << ind][it[1]] = 1
    
    for mask in range(1, 1 << n):
        for genre in range(3):
            for nsng, sng in enumerate(songs):
                if sng[1] != genre and ((mask >> nsng) & 1) == 0:
                    dp[mask | (1 << nsng)][sng[1]] += dp[mask][genre]
                    if (mask | (1 << nsng)) == 4:
                        asdddd = 1
            
            sm = 0
            for ind, it in enumerate(reversed(bin(mask)[2:])):
                if it == '1':
                    sm += songs[ind][0]
            if sm == t:
                result += dp[mask][genre]
                result %= MOD
    
    print(result)


main()

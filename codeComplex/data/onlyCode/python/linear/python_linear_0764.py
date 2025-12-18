import sys
# from bisect import bisect_right
# gcd
# from fractions import gcd
# from math import ceil, floor
# from copy import deepcopy
# from itertools import accumulate
# l = ['a', 'b', 'b', 'c', 'b', 'a', 'c', 'c', 'b', 'c', 'b', 'a']
# print(S.most_common(2))  # [('b', 5), ('c', 4)]
# print(S.keys())  # dict_keys(['a', 'b', 'c'])
# print(S.values())  # dict_values([3, 5, 4])
# print(S.items())  # dict_items([('a', 3), ('b', 5), ('c', 4)])
# from collections import Counter
# import math
# from functools import reduce
#
# fin = open('./test/in_1.txt', 'r')
# sys.stdin = fin
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template



if __name__ == '__main__':

    # write code
    n,q = mi()
    a = lmi()
    i = 0
    max_a = max(a)
    t = a.index(max_a)
    last = a[0]
    Lis = []
    tmp = []
    for i in range(1, t + 1):
        Lis.append((last,a[i]))
        if last < a[i]:
            tmp.append(last)
            last = a[i]
        else:
            tmp.append(a[i])
    # print(Lis)
    anslist = a[t+1:] + tmp
    # print(last)
    # print(anslist)
    # print(tmp)
    for i in range(q):
        tm = ii()
        if 1 <= tm <= t:
            print(Lis[tm - 1][0],Lis[tm - 1][1])
        else:
            print(max_a,anslist[(tm-t-1)%len(anslist)])
import sys
from collections import deque, defaultdict as dd
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from itertools import permutations
from datetime import datetime
from math import ceil, sqrt, log, gcd

abc = 'abcdefghijklmnopqrstuvwxyz'
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
       'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
       'z': 25}
mod = 1000000007
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

ans = []


def permute(b, x, ind):
    if ind == len(b):
        return 1
    f = 0
    for i in range(9, -1, -1):
        if x[i] > 0 and i <= int(b[ind]):
            x[i] -= 1
            ans[ind] = str(i)
            if i < int(b[ind]):
                f = 1
            if f:
                k = 9
                for j in range(ind + 1, len(b)):
                    while x[k] == 0:
                        k -= 1
                    ans[j] = str(k)
                    x[k] -= 1
                return 1
            if permute(b, x, ind + 1):
                return 1
            x[i] += 1
    return 0


def generate_inputs(n):
    if n < 1:
        n = 1
    # a is a number with n digits, descending from 9 to 0 cyclically
    digits_a = [str(9 - (i % 10)) for i in range(n)]
    a = int("".join(digits_a))
    # b is a number with n digits, ascending from 0 to 9 cyclically
    digits_b = [str(i % 10) for i in range(n)]
    b = int("".join(digits_b))
    return a, b


def main(n):
    a, b = generate_inputs(n)
    if len(str(a)) < len(str(b)):
        s = list(str(a))
        s.sort(reverse=True)
        # print("".join(s))
        pass

    else:
        x = [0] * 10
        for ch in str(a):
            x[int(ch)] += 1
        b_str = str(b)
        global ans
        ans = [0] * len(b_str)
        permute(b_str, x, 0)
        # print("".join(ans))
        pass
if __name__ == "__main__":
    # example deterministic call
    main(10)
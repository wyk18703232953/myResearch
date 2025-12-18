#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k1, k2, k3  = sorted(map(int, input().split()))
'''
we have 1       - obvious
2 twos          - they can cover everything
3 threes        - they can cover everything
2 3 3           - also possible. need to cover all odd numbers with 2 threes:
                2*x+1 + 3*k
                2*x+3 + 3*k
at least 1 > 3  - 
x3 + k3*i, where k3 > 3
we can choose x3, so it's >= max(x1, x2, x3)
=> need to cover:
x3+1, x3+2, x3+3, ...
we can cover x3+1 and x3+3 using 2.
?

lcm(k1, k2, k3)
xmax = max(x1, x2, x3)
xmin = min(x1, x2, x3)
one of xi can be taken as zero (just substract xmin from all)
also, it doesn't make sense to take any of xi > 0 greater than lcm
therefore, we can check interval [lcm, 2*lcm] to be covered

1 2 3 4 5 6 7 8 9 10
  x   x   x   x   x
3 3 3
x x x x x x x x x x
2 3 3 - doesn't seems to work
x x   x   x x x   x
x   x x   x x   x x

(k1 == 2 and k3 % k2 == 0) - passed 5th test
k1 == 2, k2 >= 3
2 4 4
1 2 3 4 5 6 7 8 9 10
x x x x x x x x x x
'''
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# gcdk = gcd(gcd(k1, k2), k3)
#lcmk = k1*k2*k3 // gcdk

if 1 == k1 or (2 == k1 and 2 == k2) or (3 == k1 and 3 == k2 and 3 == k3) \
    or (k1 == 2 and k2 == 4 and k3 == 4):
    print("YES")
else:
    print("NO")
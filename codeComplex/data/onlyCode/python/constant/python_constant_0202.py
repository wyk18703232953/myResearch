#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k1, k2, k3  = sorted(map(int, input().split()))
'''
k1 == 1         - obvious
2 twos          - they can cover everything
3 threes        - they can cover everything

lcm := lcm(k1, k2, k3)
xmax := max(x1, x2, x3)
xmin := min(x1, x2, x3)
one of xi can be taken as zero (just substract xmin from all)
also, it doesn't make sense to take any of xi > 0 greater than lcm
therefore, we can check interval [lcm, 2*lcm] to be covered

2 3 3           - doesn't seems to work
1 2 3 4 5 6 7 8 9 10
x x   x   x x x   x  
x   x x   x x   x x

2 4 4
1 2 3 4 5 6 7 8 9 10
x x x x x x x x x x

2 ? ?
1 2 3 4 5 6 7 8 9 10
x   x   x   x   x  
to cover 2 and 4 with one ki => ki == 2
to cover 2 and 6 with one ki => ki == 4
'''
if 1 == k1 or (2 == k1 and 2 == k2) or (3 == k1 and 3 == k2 and 3 == k3) \
    or (k1 == 2 and k2 == 4 and k3 == 4):
    print("YES")
else:
    print("NO")
#!/usr/bin/env python3
import sys
def contain(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    return bx1 <= ax1 and ax2 <= bx2 and by1 <= ay1 and ay2 <= by2
def ask(x1, y1, x2, y2, known=(), memo={}):
    if x2 < x1+1 or y2 < y1+1:
        return 0
    ofs = len(list(filter(lambda rect: contain(rect, (x1, y1, x2, y2)), known)))
    key = (x1+1, y1+1, x2, y2)
    if key in memo:
        return memo[key] - ofs
    print('?', *key)
    sys.stdout.flush()
    memo[key] = int(input())
    return memo[key] - ofs
def binsearch(l, r, p): # (l,r], return the smallest n which p holds
    assert l < r
    while l+1 != r:
        m = (l + r) // 2
        if p(m):
            r = m
        else:
            l = m
    return r
def shrink(x1, y1, x2, y2, cnt, known=()):
    assert ask(x1, y1, x2, y2, known=known) == cnt
    x1 = binsearch(x1, x2, lambda x: ask(x, y1, x2, y2, known=known) != cnt) - 1
    y1 = binsearch(y1, y2, lambda y: ask(x1, y, x2, y2, known=known) != cnt) - 1
    x2 = binsearch(x1, x2, lambda x: ask(x1, y1, x, y2, known=known) == cnt)
    y2 = binsearch(y1, y2, lambda y: ask(x1, y1, x2, y, known=known) == cnt)
    assert ask(x1, y1, x2, y2, known=known) == cnt
    assert ask(x1, y1, x2, y2, known=known) == cnt
    return x1, y1, x2, y2
def go(x1, y1, x2, y2):
    assert ask(x1, y1, x2, y2) == 2
    x1, y1, x2, y2 = shrink(x1, y1, x2, y2, 2)
    a = None
    if not a and x1 < x2:
        if ask(x1+1, y1, x2, y2) == 1:
            a = shrink(x1+1, y1, x2, y2, 1)
        elif ask(x1, y1, x2-1, y2) == 1:
            a = shrink(x1, y1, x2-1, y2, 1)
    if not a and y1 < y2:
        if ask(x1, y1+1, x2, y2) == 1:
            a = shrink(x1, y1+1, x2, y2, 1)
        elif ask(x1, y1, x2, y2-1) == 1:
            a = shrink(x1, y1, x2, y2-1, 1)
    if not a:
        a = x1, y1, x2, y2
        return a, a
    else:
        b = shrink(x1, y1, x2, y2, 1, known=[ a ])
        return a, b
n = int(input())
a, b = go(0, 0, n, n)
ax1, ay1, ax2, ay2 = a
bx1, by1, bx2, by2 = b
print('!', ax1+1, ay1+1, ax2, ay2, bx1+1, by1+1, bx2, by2)




# Made By Mostafa_Khaled
import sys
from collections import deque
import bisect
def chk(l,r,total):
    b = len(l)
    prev = 0
    i = 0
    f = 1
    cnt = 0
    while i < b:
        prev = prev+l[i]
        if cnt == total and prev == r:
            i = i+1
            continue

        if prev == r:
            cnt += 1
            if cnt != total:
                prev = 0

        i = i+1

    if cnt < total or i != b:
        f = 0

    return f


for _ in range(1):
    n = int(input())
    s = input()
    l = []
    som = 0
    for i in s:
        l.append(int(i))
        som += int(i)

    flag = 0
    for i in range(2,n+1):
        if som%i == 0:
            r = som//i
            if chk(l,r,i):
                flag = 1
                break

        if flag:
            break

    if flag:
        print("YES")

    else:
        print("NO")

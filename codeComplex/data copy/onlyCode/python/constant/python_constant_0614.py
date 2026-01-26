from sys import stdin, stdout
from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial


def get(l, r):
    if l > r:
        return 0
    
    if l & 1:
        return (-l - r) * (r - l + 2) // 4
    else:
        return (l + r) * (r - l + 2) // 4


def solution(l, r):
    l1, l2, r1, r2 = l, l, r, r
    
    if l & 1:
        l2 += 1
    else:
        l1 += 1
    
    if r & 1:
        r2 -= 1
    else:
        r1 -= 1
    
    return get(l1, r1) + get(l2, r2)


q = int(stdin.readline())
for i in range(q):
    l, r = map(int, stdin.readline().split())
    stdout.write(str(solution(l, r)) + '\n')
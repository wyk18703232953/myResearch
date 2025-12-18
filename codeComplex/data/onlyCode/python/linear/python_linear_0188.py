import bisect

def solve():
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    p = [0]
    for x in a:
        p.append(p[-1] + x)
    return bisect.bisect_left(p, p[-1] / 2)

print(solve())
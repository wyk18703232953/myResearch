from bisect import bisect_left

def readint():
    return int(input())


def readline():
    return [int(c) for c in input().split()]

# similar to 45311982
def main():
    MAX = 10**9
    n, m = readline()
    v = sorted([readint() for _ in range(n)])

    h = []
    for _ in range(m):
        x1, x2, _ = readline()
        if x1 == 1:
            h.append(x2)
    h.sort()

    lh = len(h)
    if lh == 0:
        print(0)
    elif n == 0:
        print(lh - bisect_left(h, MAX))
    else:
        mn = n + lh - bisect_left(h, MAX)
        for i in range(n):
            mn = min(mn, lh - bisect_left(h, v[i]) + i)
        print(mn)

                  
if __name__ == '__main__':
    main()

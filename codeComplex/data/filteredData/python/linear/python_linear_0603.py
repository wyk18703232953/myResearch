import collections, atexit, math, sys, bisect

sys.setrecursionlimit(1000000)

def dprint(*args, **kwargs):
    pass

zz = ((1, -1), (0, 2), (1, -1))

def main(n):
    N = n
    now = (0, 0)
    for i in range(N):
        print(now[0], now[1])
        step = zz[i % 3]
        now = (now[0] + step[0], now[1] + step[1])

if __name__ == "__main__":
    main(10)
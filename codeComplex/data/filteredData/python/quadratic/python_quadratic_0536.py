import collections, atexit, math, sys, bisect

sys.setrecursionlimit(1000000)


try:
    import numpy  # noqa: F401

    def dprint(*args, **kwargs):
        print(*args, file=sys.stderr)
except Exception:
    def dprint(*args, **kwargs):
        pass


MAXN = 10 ** 18 + 10


def getUpper(N):
    z = 1
    r = 0
    for i in range(N):
        r += z
        z *= 4
        if r > MAXN:
            break
    return r


def run_case(N, K):
    tk = K
    z = 1
    for i in range(N):
        tk -= z
        z *= 4
        if tk < 0:
            break
    if tk > 0:
        print('NO')
        return
    nowcut = 0
    nt = 1
    nowupper = 0
    ok = False
    for i in range(N):
        nt *= 2
        nowcut += nt - 1
        if nowcut > K:
            break
        t = (nt * 2 - 3)
        tu = t * getUpper(N - 1 - i)
        nowupper += tu
        dprint('bound', nowcut, nowcut + nowupper)
        if nowcut <= K <= nowcut + nowupper:
            ok = True
            break
    if ok:
        print('YES', N - 1 - i)
    else:
        print('NO')


def main(n):
    T = n
    for t in range(T):
        N = t + 1
        K = (t + 1) * (t + 2)
        run_case(N, K)


if __name__ == "__main__":
    main(5)
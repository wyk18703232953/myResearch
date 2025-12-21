import collections, atexit, math, sys, bisect

sys.setrecursionlimit(1000000)

try:
    import numpy
    def dprint(*args, **kwargs):
        print(*args, file=sys.stderr)
    dprint('debug mode')
except Exception:
    def dprint(*args, **kwargs):
        pass

MAXN = 10**18 + 10

def getUpper(N):
    z = 1
    r = 0
    for i in range(N):
        r += z
        z *= 4
        if r > MAXN:
            break
    return r

def main(n):
    results = []
    T = n
    for _ in range(T):
        N = max(1, n)
        K = max(1, n * n)
        tk = K
        z = 1
        for i in range(N):
            tk -= z
            z *= 4
            if tk < 0:
                break
        if tk > 0:
            results.append('NO')
            continue
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
            results.append(f"YES {N-1-i}")
        else:
            results.append("NO")
    for line in results:
        print(line)
    return results

if __name__ == "__main__":
    main(3)
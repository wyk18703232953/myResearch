import sys
input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    a = []
    for _ in [0]*n:
        a.append(list(map(int,input().split())))
    
    ok = 0
    ng = 10**9+1
    judge = pow(2,m)-1
    dg = 1000

    while ng-ok > 1:
        mid = (ng+ok)//2
        tank = set()
        for i in range(n):
            r = 0
            for j in range(m):
                r *= 2
                if a[i][j] >= mid:
                    r += 1
            tank.add(r)

        for p in tank:
            for q in tank:
                if p|q == judge:
                    ok = mid
                    break
        if ok != mid:
            ng = mid

    tank = set()
    res = []
    for i in range(n):
        r = 0
        for j in range(m):
            r *= 2
            if a[i][j] >= ok:
                r += 1
        if not r in tank:
            res.append(i*dg+r)
        tank.add(r)

    for p in res:
        for q in res:
            if (p%dg)|(q%dg) == judge:
                print(p//dg+1,q//dg+1)
                return


if __name__ == '__main__':
    main()
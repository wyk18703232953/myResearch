from sys import stdin, gettrace

if gettrace():
    def inputi():
        return input()
else:
    def input():
        return next(stdin)[:-1]


    def inputi():
        return stdin.buffer.readline()

def patterns(s):
    if len(s) == 1:
        return [s, '_']
    else:
        tp = patterns(s[1:])
        return [s[0] + t for t in tp] + ['_' + t for t in tp]

def main():
    n,m,k = map(int, input().split())
    pp = (input() for _ in range(n))
    ppm = {}
    for i, p in enumerate(pp):
        ppm[p] = i
    pre = [0]*n
    suc = [[] for _ in range(n)]
    for _ in range(m):
        s, ml = input().split()
        ml = int(ml) - 1
        ps = patterns(s)
        found = False
        for p in ps:
            if p in ppm:
                if ppm[p] == ml:
                    found = True
                else:
                    pre[ppm[p]] += 1
                    suc[ml].append(ppm[p])
        if not found:
            print("NO")
            return
    znodes = [i for i in range(n) if pre[i]==0]
    res = []
    while znodes:
        i = znodes.pop()
        res.append(i+1)
        for j in suc[i]:
            pre[j] -= 1
            if pre[j] == 0:
                znodes.append(j)
    if len(res) == n:
        print("YES")
        print(' '.join(map(str, res)))
    else:
        print("NO")

if __name__ == "__main__":
    main()

x = int('00001111', 2)
y = int('00110011', 2)
z = int('01010101', 2)
E = set()
T = set()
F = {('x', x), ('y', y), ('z', z)}
prv = (set(), set(), set())
fam = 2 ** 8
tmpl = '#' * 99
ans = [tmpl] * fam

def cmpr(E):
    global ans
    ans = [tmpl] * fam
    for e in E:
        if len(ans[e[1]]) > len(e[0]) or (len(ans[e[1]]) == len(e[0]) and ans[e[1]] > e[0]):
            ans[e[1]] = e[0]
    return set((j, i) for i, j in enumerate(ans) if j != tmpl)

def main(n):
    global E, T, F, prv, ans
    E = set()
    T = set()
    F = {('x', x), ('y', y), ('z', z)}
    prv = (set(), set(), set())
    ans = [tmpl] * fam

    while prv != (E, T, F):
        prv = E.copy(), T.copy(), F.copy()
        for f in prv[2]:
            F.add(('!' + f[0], ~f[1] & (fam - 1)))
            T.add(f)
            for t in prv[1]:
                T.add((t[0] + '&' + f[0], t[1] & f[1]))
        for t in prv[1]:
            E.add(t)
        for e in prv[0]:
            if e not in F:
                F.add(('(' + e[0] + ')', e[1]))
            for t in prv[1]:
                E.add((e[0] + '|' + t[0], e[1] | t[1]))
        E, T, F = cmpr(E), cmpr(T), cmpr(F)
    cmpr(E)

    # deterministically choose n queries: pattern i % 256 as 8-bit binary
    outputs = []
    for i in range(n):
        val = i % fam
        s = format(val, '08b')
        outputs.append(ans[int(s, 2)])
    for line in outputs:
        print(line)

if __name__ == "__main__":
    main(10)
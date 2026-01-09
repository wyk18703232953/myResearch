def main(n):
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

    def cmpr(S):
        nonlocal ans
        ans = [tmpl] * fam
        for e in S:
            expr, val = e
            cur = ans[val]
            if len(cur) > len(expr) or (len(cur) == len(expr) and cur > expr):
                ans[val] = expr
        return set((expr, val) for val, expr in enumerate(ans) if expr != tmpl)

    while prv != (E, T, F):
        prv = E.copy(), T.copy(), F.copy()
        for f in prv[2]:
            name, val = f
            F.add(('!' + name, ~val & (fam - 1)))
            T.add(f)
            for t in prv[1]:
                T.add((t[0] + '&' + name, t[1] & val))
        for t in prv[1]:
            E.add(t)
        for e in prv[0]:
            if e not in F:
                F.add(('(' + e[0] + ')', e[1]))
            for t in prv[1]:
                E.add((e[0] + '|' + t[0], e[1] | t[1]))
        E, T, F = cmpr(E), cmpr(T), cmpr(F)
    cmpr(E)

    # 生成测试数据：这里简单使用前 n 个 8 位二进制串作为输入
    # 若 n > 256，则循环利用所有 8 位模式
    for i in range(n):
        val = i % fam
        # print(ans[val])
        pass
from copy import deepcopy

mo = 10**9 + 7

def build_inputs(n):
    # 映射说明：
    # n >= 1
    # T = n
    # 有 n 组 (t, g)
    # t = i % n + 1 (1..n 周期)
    # g = i % 3 + 1 (1..3 周期)
    T = n if n > 0 else 1
    pairs = []
    for i in range(n):
        t = i % n + 1 if n > 0 else 1
        g = i % 3 + 1
        pairs.append((t, g))
    return n, T, pairs

def nb_factory():
    nd = {(1, 0, 0, 0): 1, (0, 1, 0, 1): 1, (0, 0, 1, 2): 1}

    def nb(tu):
        if tu not in nd:
            if tu[tu[3]] == 0:
                nd[tu] = 0
            else:
                nt = list(tu)
                nt[tu[3]] -= 1
                nt[3] = (nt[3] + 1) % 3
                nt2 = nt[:]
                nt2[3] = (nt2[3] + 1) % 3
                nd[tu] = (tu[tu[3]] * (nb(tuple(nt)) + nb(tuple(nt2)))) % mo
        return nd[tu]

    return nb

def core_logic(n, T, pairs):
    di = {(0, 0, 0, T): 1}
    for t, g in pairs:
        an = deepcopy(di)
        for k in an:
            nc = list(k)
            nc[3] -= t
            nc[g - 1] += 1
            if nc[3] >= 0:
                nc = tuple(nc)
                if nc in di:
                    di[nc] += an[k]
                else:
                    di[nc] = an[k]
    nb = nb_factory()
    res = 0
    for k in di:
        if k[3] == 0:
            a, b, c, _ = k
            res += di[k] * (
                nb((a, b, c, 1)) +
                nb((a, b, c, 0)) +
                nb((a, b, c, 2))
            )
    return res % mo

def main(n):
    if n < 1:
        n = 1
    n_in, T_in, pairs = build_inputs(n)
    ans = core_logic(n_in, T_in, pairs)
    print(ans)

if __name__ == "__main__":
    main(5)
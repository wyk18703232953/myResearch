MOD = 998244353

def main(n):
    a = [(i * 3 + 1) % MOD for i in range(1, n + 1)]
    p, sp, s, ss = 0, 0, 0, 0
    for x in a:
        ss = (2 * ss + s) % MOD
        s = (s + x) % MOD
        p = (ss + sp + s) % MOD
        sp = (sp + p) % MOD
    # print(p)
    pass
if __name__ == "__main__":
    main(10)
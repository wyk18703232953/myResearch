K = 998244353
MAXN = 200005
dd = [0 for _ in range(MAXN)]
p = [0 for _ in range(MAXN)]
s = [0 for _ in range(MAXN)]
a = [0 for _ in range(MAXN)]
fen = [0 for _ in range(MAXN)]

def mu(a_, n_):
    if n_ == 0:
        return 1
    q = mu(a_, n_ // 2)
    if n_ % 2 == 0:
        return q * q % K
    return q * q % K * a_ % K

def add(u, v):
    i = u
    while i <= 200000:
        fen[i] += v
        i += i & -i

def get(u):
    res = 0
    i = u
    while i > 0:
        res += fen[i]
        i -= i & -i
    return res

def generate_p(n):
    # Deterministic generation of p[1..n]
    # Mix of positives and -1, within [1, n] for positives
    for i in range(1, n + 1):
        if i % 3 == 0:
            p[i] = -1
        else:
            p[i] = (i * 7) % n + 1 if n > 0 else 1

def reset_globals():
    for i in range(MAXN):
        dd[i] = 0
        s[i] = 0
        a[i] = 0
        fen[i] = 0

def main(n):
    if n >= MAXN:
        n = MAXN - 1

    reset_globals()
    generate_p(n)

    cnt = 0
    for i in range(1, n + 1):
        if p[i] > 0:
            dd[p[i]] = 1
        else:
            cnt += 1

    for i in range(1, n + 1):
        if dd[i] == 0:
            s[i] = s[i - 1] + 1
        else:
            s[i] = s[i - 1]

    cnt1 = 0
    P = 0
    den = mu(cnt, K - 2) if cnt != 0 else 0
    for i in range(1, n + 1):
        if p[i] == -1:
            cnt1 += 1
        else:
            u = cnt - cnt1
            if cnt != 0:
                P = (P + u * s[p[i]] % K * den % K) % K
                P = (P + cnt1 * (cnt - s[p[i]]) % K * den % K) % K

    if cnt >= 2:
        P = (P + cnt * (cnt - 1) * mu(4, K - 2)) % K

    m = 0
    for i in range(1, n + 1):
        if p[i] > 0:
            m += 1
            a[m] = p[i]

    P1 = 0
    for i in range(m, 0, -1):
        P1 = (P1 + get(a[i])) % K
        add(a[i], 1)

    P = (P + P1) % K

    print(P)

if __name__ == "__main__":
    main(1000)
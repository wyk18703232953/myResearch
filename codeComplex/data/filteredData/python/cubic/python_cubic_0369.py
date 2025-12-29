p1, g1, ig1 = 104857601, 3, 34952534
p2, g2, ig2 = 111149057, 3, 37049686
p3, g3, ig3 = 113246209, 7, 16178030
z1 = 439957480532171226961446
z2 = 879898597692195524486915
z3 = 8496366309945115353
ppp = p1 * p2 * p3
W1 = [pow(g1, (p1 - 1) >> i, p1) for i in range(22)]
W2 = [pow(g2, (p2 - 1) >> i, p2) for i in range(22)]
W3 = [pow(g3, (p3 - 1) >> i, p3) for i in range(22)]
iW1 = [pow(ig1, (p1 - 1) >> i, p1) for i in range(22)]
iW2 = [pow(ig2, (p2 - 1) >> i, p2) for i in range(22)]
iW3 = [pow(ig3, (p3 - 1) >> i, p3) for i in range(22)]


def fft1(k, f):
    for l in range(k, 0, -1):
        d = 1 << (l - 1)
        U = [1]
        for _ in range(d):
            U.append(U[-1] * W1[l] % p1)
        for i in range(1 << (k - l)):
            for j in range(d):
                s = i * 2 * d + j
                fs, fsd = f[s], f[s + d]
                f[s] = (fs + fsd) % p1
                f[s + d] = U[j] * (fs - fsd) % p1


def fft2(k, f):
    for l in range(k, 0, -1):
        d = 1 << (l - 1)
        U = [1]
        for _ in range(d):
            U.append(U[-1] * W2[l] % p2)
        for i in range(1 << (k - l)):
            for j in range(d):
                s = i * 2 * d + j
                fs, fsd = f[s], f[s + d]
                f[s] = (fs + fsd) % p2
                f[s + d] = U[j] * (fs - fsd) % p2


def fft3(k, f):
    for l in range(k, 0, -1):
        d = 1 << (l - 1)
        U = [1]
        for _ in range(d):
            U.append(U[-1] * W3[l] % p3)
        for i in range(1 << (k - l)):
            for j in range(d):
                s = i * 2 * d + j
                fs, fsd = f[s], f[s + d]
                f[s] = (fs + fsd) % p3
                f[s + d] = U[j] * (fs - fsd) % p3


def ifft1(k, f):
    for l in range(1, k + 1):
        d = 1 << (l - 1)
        for i in range(1 << (k - l)):
            u = 1
            base = i * 2 * d
            for j in range(base, base + d):
                fj, fjd = f[j], f[j + d] * u % p1
                f[j] = (fj + fjd) % p1
                f[j + d] = (fj - fjd) % p1
                u = u * iW1[l] % p1


def ifft2(k, f):
    for l in range(1, k + 1):
        d = 1 << (l - 1)
        for i in range(1 << (k - l)):
            u = 1
            base = i * 2 * d
            for j in range(base, base + d):
                fj, fjd = f[j], f[j + d] * u % p2
                f[j] = (fj + fjd) % p2
                f[j + d] = (fj - fjd) % p2
                u = u * iW2[l] % p2


def ifft3(k, f):
    for l in range(1, k + 1):
        d = 1 << (l - 1)
        for i in range(1 << (k - l)):
            u = 1
            base = i * 2 * d
            for j in range(base, base + d):
                fj, fjd = f[j], f[j + d] * u % p3
                f[j] = (fj + fjd) % p3
                f[j + d] = (fj - fjd) % p3
                u = u * iW3[l] % p3


def convolve(a, b, P):
    n0 = len(a) + len(b) - 1
    if len(a) < 50 or len(b) < 50:
        ret = [0] * n0
        if len(a) > len(b):
            a, b = b, a
        for i, aa in enumerate(a):
            for j, bb in enumerate(b):
                ret[i + j] = (ret[i + j] + aa * bb) % P
        return ret

    k = n0.bit_length()
    n = 1 << k
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))

    a1 = [x % p1 for x in a]
    a2 = [x % p2 for x in a]
    a3 = [x % p3 for x in a]
    b1 = [x % p1 for x in b]
    b2 = [x % p2 for x in b]
    b3 = [x % p3 for x in b]

    fft1(k, a1)
    fft1(k, b1)
    fft2(k, a2)
    fft2(k, b2)
    fft3(k, a3)
    fft3(k, b3)

    for i in range(n):
        a1[i] = a1[i] * b1[i] % p1
        a2[i] = a2[i] * b2[i] % p2
        a3[i] = a3[i] * b3[i] % p3

    ifft1(k, a1)
    ifft2(k, a2)
    ifft3(k, a3)

    invn1 = pow(n, p1 - 2, p1)
    invn2 = pow(n, p2 - 2, p2)
    invn3 = pow(n, p3 - 2, p3)

    for i in range(n0):
        a1[i] = a1[i] * invn1 % p1
        a2[i] = a2[i] * invn2 % p2
        a3[i] = a3[i] * invn3 % p3

    return [(x1 * z1 + x2 * z2 + x3 * z3) % ppp % P
            for x1, x2, x3 in zip(a1[:n0], a2[:n0], a3[:n0])]


def main(n):
    # 规模 n：原来是 N。这里固定一个模数 P，并用 n 作为 N。
    P = 10**9 + 7
    N = n

    nn = 1001  # 阶乘预处理上界（与原程序一致）

    fa = [1] * (nn + 1)
    fainv = [1] * (nn + 1)
    for i in range(nn):
        fa[i + 1] = fa[i] * (i + 1) % P
    fainv[-1] = pow(fa[-1], P - 2, P)
    for i in range(nn - 1, -1, -1):
        fainv[i] = fainv[i + 1] * (i + 1) % P

    def chk(L):
        return [fa[i] * x % P for i, x in enumerate(L)]

    def chkinv(L):
        return [fainv[i] * x % P for i, x in enumerate(L)]

    X = [[] for _ in range(444)]
    Y = [[] for _ in range(444)]
    X[0] = [1]
    X[1] = [0, 1]
    X[2] = [0, 1, 1]
    X[3] = [0, 0, 4, 1]

    Y[0] = [1]
    Y[1] = [1, 0]
    Y[2] = [0, 2, 0]
    Y[3] = [0, 1, 4, 0]

    for i in range(4, 404):
        X[i] = [0] * i + [1]
        Y[i] = [0] * (i + 1)
        for j in range(1, i):
            k = i - j
            X[i][j] = (X[i - 1][j - 1] * (2 * k + 1) +
                       X[i - 2][j - 1] * k) % P
            Y[i][j] = (Y[i - 1][j - 1] * (2 * k) +
                       Y[i - 2][j - 1] * (k - 1)) % P

    X = [chkinv(a) for a in X]
    Y = [chkinv(a) for a in Y]

    ANS = [0] * (N + 1)
    for i in range(N):
        t = convolve(X[i], X[N - 1 - i], P)
        for j, a in enumerate(t):
            if j <= N:
                ANS[j] = (ANS[j] + a) % P

    ans = 0
    for i, a in enumerate(ANS):
        ans = (ans + a * fa[i]) % P

    print(ans)
    return ans
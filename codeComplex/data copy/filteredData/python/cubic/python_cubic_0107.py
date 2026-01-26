K = 998244353

def mu(a, n):
    if n == 0:
        return 1
    q = mu(a, n // 2)
    if n % 2 == 0:
        return q * q % K

    else:
        return q * q % K * a % K

def build_combinations(max_n):
    c = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    c[0][0] = 1
    for i in range(1, max_n + 1):
        c[i][0] = 1
        for j in range(1, i):
            c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % K
        c[i][i] = 1
    return c

def build_inverses(max_n):
    inv = [0] * (max_n + 1)
    inv[0] = 1
    for i in range(1, max_n + 1):
        inv[i] = mu(i, K - 2)
    return inv

def calc(m, d, S, c):
    res = 0
    if m == 0:
        return 1 if S == 0 else 0

    for u in range(0, m + 1):
        if u * d > S:
            break
        U = c[m][u] * c[S - u * d + m - 1][m - 1] % K
        if u % 2 == 0:
            res = (res + U) % K

        else:
            res = (res - U + K) % K
    return res

def main(n):
    """
    使用规模参数 n 生成一组 (p, s, r)，然后按原逻辑计算结果并返回。
    这里采用简单的构造：
        p = n
        r = 1
        s = 2 * n
    并保证不会越界预处理数组。
    """
    # 构造测试数据
    p = n
    r = 1
    s = 2 * n

    # 估计需要的组合数上界：
    # - c 需要到 max(p, s - r + p) 这一数量级
    max_c = max(p, s - r + p)
    # 安全起见加一点余量
    max_c += 5

    c = build_combinations(max_c)
    inv = build_inverses(p)  # 只需到 p

    res = 0

    for i in range(1, p + 1):
        A = 0
        max_d = s // i
        for d in range(r, max_d + 1):
            if i < p:
                A = (A + calc(p - i, d, s - d * i, c)) % K

            else:
                if s - i * d == 0:
                    A += 1
        A = A * inv[i] % K
        res = (res + A * c[p - 1][i - 1] % K) % K

    den = c[s - r + p - 1][p - 1]
    res = res * mu(den, K - 2) % K
    return res

# 示例：在需要时可以调用 main(n)，例如：
# print(main(10))
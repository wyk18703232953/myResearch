K = 998244353
MAXN = 200005

dd = [0] * MAXN
p = [0] * MAXN
s = [0] * MAXN
a = [0] * MAXN
fen = [0] * MAXN


def mu(a, n):
    if n == 0:
        return 1
    q = mu(a, n // 2)
    if n % 2 == 0:
        return q * q % K
    return q * q % K * a % K


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


def main(n):
    # 生成测试数据：在 1..n 中随机选择若干位置为已知排列值，其余为 -1
    # 保证已知部分不重复且在 [1, n] 内
    import random

    # 清空全局数组在前 n 范围内
    for i in range(0, n + 2):
        dd[i] = 0
        p[i] = 0
        s[i] = 0
        a[i] = 0
        fen[i] = 0

    # 随机确定多少个位置已知
    k = random.randint(0, n)  # 已知元素个数
    positions = list(range(1, n + 1))
    random.shuffle(positions)
    known_pos = positions[:k]

    values = list(range(1, n + 1))
    random.shuffle(values)
    known_vals = values[:k]

    # 填充 p：已知位置放置一个排列值，其余为 -1
    for i in range(1, n + 1):
        p[i] = -1
    for pos, val in zip(known_pos, known_vals):
        p[pos] = val

    # 原逻辑开始
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
    if cnt == 0:
        den = 1
    else:
        den = mu(cnt, K - 2)

    for i in range(1, n + 1):
        if p[i] == -1:
            cnt1 += 1
        else:
            u = cnt - cnt1
            P = (P + u * s[p[i]] % K * den % K) % K
            P = (P + cnt1 * (cnt - s[p[i]]) % K * den % K) % K

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
    # 示例运行：可自行修改 n
    main(10)
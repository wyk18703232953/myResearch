import math

gcd = math.gcd
ceil = math.ceil
mod1 = (10**9) + 7
mod2 = 998244353

def strinp(testcases):
    k = 5
    if testcases == -1 or testcases == 1:
        k = 1
    f = "dummy_input_line"
    f = f[2:len(f)-k]
    return f

def alp(a):
    return (ord(a) - ord("a"))

def main(n):
    # Map n to grid size and k (even to avoid trivial -1 output)
    if n < 2:
        n_val = 1
        m_val = 1
        k = 2

    else:
        n_val = n
        m_val = n
        k = 2 * (n // 2) if n % 2 == 0 else 2 * ((n + 1) // 2)

    # Deterministic generation of lrw (n_val x (m_val-1)) and udw ((n_val-1) x m_val)
    lrw = [[(i + j + 1) % 7 + 1 for j in range(m_val - 1)] for i in range(n_val)]
    udw = [[(i * 2 + j + 3) % 9 + 1 for j in range(m_val)] for i in range(n_val - 1)]

    if k % 2 == 1:
        a = [-1] * m_val
        for _ in range(n_val):
            # print(*a)
            pass
        return

    dp1 = [[0 for _ in range(m_val)] for _ in range(n_val)]
    dp2 = [[0 for _ in range(m_val)] for _ in range(n_val)]
    inf = 10**10
    dis = k // 2
    for _ in range(dis):
        for i in range(n_val):
            for j in range(m_val):
                a = inf
                b = inf
                c = inf
                d = inf
                if j > 0:
                    a = lrw[i][j - 1] + dp2[i][j - 1]
                if j < m_val - 1:
                    b = lrw[i][j] + dp2[i][j + 1]
                if i > 0:
                    c = udw[i - 1][j] + dp2[i - 1][j]
                if i < n_val - 1:
                    d = udw[i][j] + dp2[i + 1][j]
                dp1[i][j] = min(a, b, c, d)
        dp2 = dp1
        dp1 = [[0 for _ in range(m_val)] for _ in range(n_val)]
    for i in range(n_val):
        for j in range(m_val):
            dp2[i][j] *= 2
    for i in range(n_val):
        # print(*dp2[i])
        pass
if __name__ == "__main__":
    main(5)
import sys

def f(r, g, b, n, m, k, mat):
    if (n >= 1 and m >= 1) or (k >= 1 and m >= 1) or (n >= 1 and k >= 1):
        a1 = mat[n][m][k]
        if a1 != -1:
            return a1

        else:
            a1 = 0
            b1 = 0
            c1 = 0
            if n >= 1 and m >= 1:
                a1 = r[n - 1] * g[m - 1] + f(r, g, b, n - 1, m - 1, k, mat)
            if k >= 1 and m >= 1:
                b1 = b[k - 1] * g[m - 1] + f(r, g, b, n, m - 1, k - 1, mat)
            if n >= 1 and k >= 1:
                c1 = r[n - 1] * b[k - 1] + f(r, g, b, n - 1, m, k - 1, mat)
            mat[n][m][k] = a1 if a1 >= b1 else b1
            if c1 > mat[n][m][k]:
                mat[n][m][k] = c1
            return mat[n][m][k]
    return 0

def generate_arrays(n, m, k):
    # deterministic, scalable data generation
    r = [(i * 2 + 1) % 100000 for i in range(n)]
    g = [(i * 3 + 2) % 100000 for i in range(m)]
    b = [(i * 5 + 3) % 100000 for i in range(k)]
    r.sort()
    g.sort()
    b.sort()
    return r, g, b

def main(n):
    # map single n into three dimensions for scalability tests
    # here we choose simple proportional sizes
    n_r = max(1, n)
    n_g = max(1, n)
    n_b = max(1, n)

    r, g, b = generate_arrays(n_r, n_g, n_b)
    mat = [[[-1 for _ in range(n_b + 1)] for _ in range(n_g + 1)] for _ in range(n_r + 1)]
    result = f(r, g, b, n_r, n_g, n_b, mat)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)
from math import ceil

def main(n):
    # Interpret n as the magnitude of parameters k, n, s, p.
    # Deterministically construct them from n.
    k = n + 1
    nn = 2 * n + 3
    s = (n % 5) + 1
    p = (n // 2) + 1

    spp = ceil(nn / s)
    tots = spp * k
    result = ceil(tots / p)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
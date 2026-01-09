def main(n):
    mod = 10**9 + 7
    mod2 = 998244353

    # Deterministically generate a and b based on n
    # Ensure b > 0 and a >= 0, scalable with n
    a = n * (n + 1) // 2
    b = n + 1

    c = 0
    x = 0
    while not (c >= b and c - b + x == a):
        x += 1
        c += x
    # print(a - x)
    pass
if __name__ == "__main__":
    main(10)
def main(n):
    # Interpret n as x, and set k deterministically as n // 2
    x = n
    k = n // 2

    if x == 0:
        # print(0)
        pass
        return

    mod = 10 ** 9 + 7

    a = ((x % mod) * pow(2, k + 1, mod)) % mod

    # print((a - (pow(2, k, mod) - 1)) % mod)
    pass
if __name__ == "__main__":
    main(10)
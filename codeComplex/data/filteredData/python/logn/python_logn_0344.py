def main(n):
    mod = 10**9 + 7
    x = n
    k = n
    if x == 0:
        return 0
    t = pow(2, k + 1, mod) * x % mod
    d = pow(2, k, mod) - 1
    return (t + mod - d) % mod


if __name__ == "__main__":
    # print(main(10))
    pass
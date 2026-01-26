def read():
    return [int(v) for v in input().split()]


def main():
    mod = 10 ** 9 + 7
    x, k = read()
    if x == 0:
        print(0)
    else:
        print((pow(2, k, mod) * (2 * x - 1) + 1) % mod)


if __name__ == '__main__':
    main()

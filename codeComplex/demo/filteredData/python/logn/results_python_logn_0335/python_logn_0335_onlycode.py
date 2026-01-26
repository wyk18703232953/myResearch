def main():
    n, k = map(int, input().split())
    m = 10 ** 9 + 7
    print((pow(2, k, m) * (2 * n - 1) + 1) % m if n else 0)


if __name__ == '__main__':
    main()

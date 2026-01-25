def main(n):
    k = n // 2
    d = (n - k) // 2 + 1
    x = ['1' if (i + 1) % d == 0 else '0' for i in range(n)]
    print(''.join(x))


if __name__ == "__main__":
    main(10)
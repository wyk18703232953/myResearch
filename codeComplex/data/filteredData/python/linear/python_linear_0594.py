def main(n):
    r = 0
    i = 2
    while i * 2 <= n:
        a = n // i
        r += (a + 2) * (a - 2 + 1) / 2
        i += 1
    print(int(4 * r))


if __name__ == "__main__":
    main(1000)
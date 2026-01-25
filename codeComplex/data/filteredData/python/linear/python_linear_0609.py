def main(n):
    m = n // 3
    for i in range(m):
        print(2 * i, 0)
        print(2 * i + 1, 0)
        print(2 * i + 1, 3)
    for i in range(n % 3):
        print(2 * m + i, 0)


if __name__ == "__main__":
    main(9)
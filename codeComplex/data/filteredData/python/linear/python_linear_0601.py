def main(n):
    if n <= 10:
        for i in range(n):
            print(0, i)
        return
    print(0, 0)
    for i in range(4, n + 1, 3):
        k = (i // 3) * 2
        print(k, 0)
        print(k - 1, 1)
        print(k - 2, 2)
    k = ((n + 1) // 3) * 2
    if n % 3 == 0:
        print(k - 1, 1)
        print(k - 2, 2)
    elif n % 3 == 2:
        print(k - 2, 2)


if __name__ == "__main__":
    main(10)
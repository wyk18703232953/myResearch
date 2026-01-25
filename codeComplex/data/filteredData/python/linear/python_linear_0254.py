def main(n):
    # Deterministically generate (n, k) from input size n
    # Ensure k >= 1 and k < 2*n to exercise both odd/even branches
    if n < 3:
        n = 3
    k = (3 * n + 1) % (2 * n - 1) + 1

    print("YES")
    for i in range(n):
        print(".", end='')
    print()
    if k & 1:
        if k <= n - 2:
            tmp = (n - k) >> 1
            for i in range(tmp):
                print(".", end='')
            for i in range(k):
                print("#", end='')
            for i in range(tmp):
                print(".", end='')
            print()
            for i in range(n):
                print(".", end='')
            print()
        else:
            print(".", end='')
            for i in range(n - 2):
                print("#", end='')
            print(".")
            k -= n - 2
            print(".", end='')
            for i in range(k >> 1):
                print("#", end='')
            for i in range(n - k - 2):
                print(".", end='')
            for i in range(k >> 1):
                print("#", end='')
            print(".")
    else:
        k = k >> 1
        for j in range(2):
            print(".", end='')
            for i in range(k):
                print("#", end='')
            for i in range(n - k - 1):
                print(".", end='')
            print()
    for i in range(n):
        print(".", end='')
    print()


if __name__ == "__main__":
    main(10)
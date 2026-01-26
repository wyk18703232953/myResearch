def main(n):
    # Deterministically generate (n, k) from input size n
    # Ensure k >= 1 and k < 2*n to exercise both odd/even branches
    if n < 3:
        n = 3
    k = (3 * n + 1) % (2 * n - 1) + 1

    # print("YES")
    pass
    for i in range(n):
        # print(".", end='')
        pass
    # print()
    pass

    if k & 1:
        if k <= n - 2:
            tmp = (n - k) >> 1
            for i in range(tmp):
                # print(".", end='')
                pass
            for i in range(k):
                # print("#", end='')
                pass
            for i in range(tmp):
                # print(".", end='')
                pass
            # print()
            pass
            for i in range(n):
                # print(".", end='')
                pass
            # print()
            pass

        else:
            # print(".", end='')
            pass
            for i in range(n - 2):
                # print("#", end='')
                pass
            # print(".")
            pass
            k -= n - 2
            # print(".", end='')
            pass
            for i in range(k >> 1):
                # print("#", end='')
                pass
            for i in range(n - k - 2):
                # print(".", end='')
                pass
            for i in range(k >> 1):
                # print("#", end='')
                pass
            # print(".")
            pass

    else:
        k = k >> 1
        for j in range(2):
            # print(".", end='')
            pass
            for i in range(k):
                # print("#", end='')
                pass
            for i in range(n - k - 1):
                # print(".", end='')
                pass
            # print()
            pass
    for i in range(n):
        # print(".", end='')
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)
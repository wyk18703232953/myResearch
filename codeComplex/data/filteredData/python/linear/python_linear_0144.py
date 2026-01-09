def main(n):
    # Deterministically generate input data of size n
    # Original program expects:
    # n: integer
    # a: list of n integers
    a = [i % 7 for i in range(n)]  # deterministic pattern

    khat = [0] * n
    ted = 0
    khat[0] = 1

    for i in range(1, len(khat)):
        khat[i] = max(khat[i - 1], a[i] + 1)

    for i in range(len(khat) - 2, -1, -1):
        if khat[i] < khat[i + 1] - 1:
            khat[i] = khat[i + 1] - 1
        ted = ted + (khat[i] - (a[i] + 1))

    ted = ted + (khat[n - 1] - (a[n - 1] + 1))
    # print(ted)
    pass
if __name__ == "__main__":
    main(10)
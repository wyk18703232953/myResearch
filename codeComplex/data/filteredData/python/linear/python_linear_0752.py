def main(n):
    # Deterministic data generation: original A would be read from input
    # Here we generate a list of length n with a mix of negative and non-negative values
    A = [(i // 2) - (n // 3) for i in range(n)]

    if n == 1:
        if A[0] >= 0:
            # print(A[0])
            pass

        else:
            # print(-A[0] - 1)
            pass
        return

    for i in range(n):
        if A[i] < 0:
            pass

        else:
            A[i] = -A[i] - 1

    if n % 2 == 0:
        # print(*A)
        pass
        return

    mim = 0
    indmim = 0
    for i in range(n):
        if A[i] < mim:
            mim = A[i]
            indmim = i
    A[indmim] = -A[indmim] - 1
    # print(*A)
    pass
if __name__ == "__main__":
    main(10)
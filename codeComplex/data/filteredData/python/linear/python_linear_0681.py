def main(n):
    # n: controls the size of the problem
    # Original program:
    # N = int(input())
    # B = [int(x) for x in input().split()]
    #
    # Here we deterministically generate N and B from n.

    # Ensure N is at least 2 and even to match the original middle-splitting logic
    if n < 2:
        N = 2

    else:
        N = n if n % 2 == 0 else n + 1

    # Deterministic construction of B of length N
    # Example pattern: B[i] = (i + 1) * 3 + (i % 5)
    B = [(i + 1) * 3 + (i % 5) for i in range(N)]

    A = [0] * N

    i, j = N // 2 - 1, N // 2
    A[i] = B[-1] // 2
    A[j] = B[-1] // 2 if B[-1] % 2 == 0 else B[-1] // 2 + 1
    l, r = A[i], A[j]

    for bi in range(len(B) - 2, -1, -1):
        b = B[bi]
        i -= 1
        j += 1

        if b - l >= A[j - 1]:
            A[i] = l
            A[j] = b - l
            r = b - l

        else:
            A[j] = r
            A[i] = b - r
            l = b - r

    # print(' '.join(map(str, A)))
    pass
if __name__ == "__main__":
    main(10)
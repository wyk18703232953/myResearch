def main(n):
    # n controls the scale: length of arrays A and B
    if n <= 0:
        return

    # Deterministic generation of inputs
    N = n
    M = float(n)
    # Ensure values > 1 to avoid division by zero in M/(c-1)
    # A: [2, 3, 4, ..., n+1]
    A = [i + 2 for i in range(N)]
    # B: [3, 4, 5, ..., n+2]
    B = [i + 3 for i in range(N)]

    B = B[1:] + [B[0]]
    C = []
    for a, b in zip(A[::-1], B[::-1]):
        C.append(b)
        C.append(a)

    if 1 in C:
        # print(-1)
        pass

    else:
        M0 = M
        for c in C:
            M += M / (c - 1)
        # print(M - M0)
        pass
if __name__ == "__main__":
    main(10)
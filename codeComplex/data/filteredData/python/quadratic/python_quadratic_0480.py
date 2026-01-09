def main(n):
    # n is the size N
    N = n

    # Deterministic generation of L and R based on N
    L = [i % 3 for i in range(N)]
    R = [(N - 1 - i) % 3 for i in range(N)]

    C = [N - L[i] - R[i] for i in range(N)]

    for i, x in enumerate(C):
        if C[i] <= 0:
            # print("NO")
            pass
            return

        l = 0
        r = 0

        j = i - 1
        while j >= 0:
            if C[j] > C[i]:
                l = l + 1
            j = j - 1

        j = i + 1
        while j < N:
            if C[j] > C[i]:
                r = r + 1
            j = j + 1

        if L[i] != l or R[i] != r:
            # print("NO")
            pass
            return

    # print("YES")
    pass
    for i in range(0, N - 1):
        # print(C[i], end=" ")
        pass
    if N > 0:
        # print(C[N - 1])
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)
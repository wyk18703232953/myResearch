def main(n):
    # Map n to sizes of R, G, B such that total DP states scale as O(n^3)
    # Here we choose R = G = B = n
    R = n
    G = n
    B = n

    # Deterministic generation of three color lists
    # Sorted non-decreasing as in original program
    L0 = [i * 2 + 1 for i in range(R)]
    L1 = [i * 3 + 2 for i in range(G)]
    L2 = [i * 5 + 3 for i in range(B)]
    L = [L0, L1, L2]

    DP = [0] * ((R + 1) * (G + 1) * (B + 1))

    def idx(r, g, b):
        return r * (G + 1) * (B + 1) + g * (B + 1) + b

    for r in range(R + 1):
        for g in range(G + 1):
            for b in range(B + 1):
                best = 0
                if r:
                    if g:
                        best = L[0][r - 1] * L[1][g - 1] + DP[idx(r - 1, g - 1, b)]
                    if b:
                        v = L[0][r - 1] * L[2][b - 1] + DP[idx(r - 1, g, b - 1)]
                        if v > best:
                            best = v
                if g and b:
                    v = L[1][g - 1] * L[2][b - 1] + DP[idx(r, g - 1, b - 1)]
                    if v > best:
                        best = v
                DP[idx(r, g, b)] = best

    result = max(DP)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)
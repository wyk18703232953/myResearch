def main(n):
    # Map n to sizes of the three color lists
    # Ensure at least 1 element in each list
    R = max(1, n)
    G = max(1, n // 2 if n > 1 else 1)
    B = max(1, n // 3 if n > 2 else 1)

    # Deterministic generation of color values
    # Values are increasing but with simple arithmetic patterns
    L0 = [i * 2 + 1 for i in range(R)]
    L1 = [i * 3 + 2 for i in range(G)]
    L2 = [i * 5 + 3 for i in range(B)]
    L = [sorted(L0), sorted(L1), sorted(L2)]

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
                        best = max(best, L[0][r - 1] * L[2][b - 1] + DP[idx(r - 1, g, b - 1)])
                if g and b:
                    best = max(best, L[1][g - 1] * L[2][b - 1] + DP[idx(r, g - 1, b - 1)])
                DP[idx(r, g, b)] = best

    result = max(DP)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(5)
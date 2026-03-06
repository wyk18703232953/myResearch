def main(n):
    # Interpret n as N = M = n (square matrix, M must be small enough since complexity is O(2^(2M)))
    N = n
    M = n
    # Deterministic data generation: state[i][j] = (i+1)*(j+1)
    state = [[(i + 1) * (j + 1) for j in range(M)] for i in range(N)]

    Ans = {}

    l = -1
    r = 10**9 + 1
    while r - l > 1:
        m = (l + r) // 2
        T = {}
        for j, S in enumerate(state):
            bit = 0
            for i, s in enumerate(S):
                if s >= m:
                    bit += 1 << i
            T[bit] = j

        ok = False
        full = (1 << M) - 1
        for bit1 in range(1 << M):
            if ok:
                break
            for bit2 in range(1 << M):
                if bit1 | bit2 == full and bit1 in T and bit2 in T:
                    ok = True
                    Ans[m] = [T[bit1], T[bit2]]
                    break
        if ok:
            l = m
        else:
            r = m

    # To keep behavior defined even if l not in Ans (e.g. no valid pair), handle gracefully
    if l in Ans:
        print(Ans[l][0] + 1, Ans[l][1] + 1)
    else:
        # Fallback: print two indices (1-based) deterministically
        print(1, 1)


if __name__ == "__main__":
    # Example: run with n = 5
    main(5)
def main(n):
    # Deterministically generate input:
    # n = number of vertices
    # max_degs is a list of degrees with some variation based on n
    if n <= 0:
        return
    max_degs = []
    for i in range(n):
        # Simple deterministic pattern:
        # alternate between 1 and 2, and give every 3rd vertex degree 3
        if i % 3 == 2:
            max_degs.append(3)
        elif i % 2 == 0:
            max_degs.append(2)
        else:
            max_degs.append(1)

    # Core logic from original solve()
    B = [[i + 1, x] for i, x in enumerate(max_degs) if x >= 2]
    S = [[i + 1, x] for i, x in enumerate(max_degs) if x < 2]

    if 2 + sum(b - 2 for _, b in B) < len(S):
        print('NO')
        return

    print('YES', len(B) + min(len(S), 2) - 1)
    print(n - 1)

    # B edges
    for k in range(len(B) - 1):
        i, x = B[k]
        i_n, _ = B[k + 1]
        print(i, i_n)
        B[k][1] -= 1
        B[k + 1][1] -= 1

    k = 0
    for i, (s_idx, _) in enumerate(S):
        if i == 0:
            print(B[0][0], s_idx)
            B[0][1] -= 1
        elif i == 1:
            print(B[-1][0], s_idx)
            B[-1][1] -= 1
        else:
            while B[k][1] == 0:
                k += 1
            print(B[k][0], s_idx)
            B[k][1] -= 1


if __name__ == "__main__":
    # Example deterministic call
    main(10)
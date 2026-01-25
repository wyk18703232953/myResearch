def main(n):
    # Deterministically generate L and R of length n based on n
    # Here we generate a pattern that will exercise the algorithm.
    # For reproducibility, L[i] and R[i] are simple arithmetic functions of i and n.
    # You can adjust this pattern as needed for different complexity experiments.
    L = [(i % (n // 2 + 1)) for i in range(n)]
    R = [((n - 1 - i) % (n // 2 + 1)) for i in range(n)]

    LR = list(zip(L, R))

    index_to_candies = {}
    candy = n

    for nn in range(n, 0, -1):
        if len(index_to_candies) == n:
            break

        zero_index = []
        for idx, (l, r) in enumerate(LR):
            if (l, r) == (0, 0) and idx not in index_to_candies:
                index_to_candies[idx] = nn
                zero_index.append(idx)

        if len(zero_index) == 0:
            print("NO")
            return

        dec_left = 0
        dec_right = len(zero_index)
        zero_index_idx = 0

        for idx, (l, r) in enumerate(LR):
            if zero_index_idx < len(zero_index) and zero_index[zero_index_idx] == idx:
                zero_index_idx += 1
                dec_left += 1
                dec_right -= 1

            if (l, r) != (0, 0):
                LR[idx] = (l - dec_left, r - dec_right)
                if LR[idx][0] < 0 or LR[idx][1] < 0:
                    print("NO")
                    return

    if len(index_to_candies) != n:
        print("NO")
        return

    print("YES")
    j = []
    for i in range(n):
        j.append(str(index_to_candies.get(i, 0)))
    print(" ".join(j))


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)
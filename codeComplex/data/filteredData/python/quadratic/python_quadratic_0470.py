def main(n):
    # Interpret n as the size of arrays L and R
    # Deterministic data generation for L and R
    # Example pattern: L[i] = i % 3, R[i] = (n - i - 1) % 3
    L = [(i % 3) for i in range(n)]
    R = [((n - i - 1) % 3) for i in range(n)]

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
            # For experiment purpose, still terminate early
            # but do not call exit()
            # print("NO")
            pass
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
                    # print("NO")
                    pass
                    return

    # print("YES")
    pass
    j = []
    for i in range(n):
        j.append(str(index_to_candies.get(i, 0)))
    # print(" ".join(j))
    pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)
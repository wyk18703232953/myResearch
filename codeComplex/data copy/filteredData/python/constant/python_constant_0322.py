def main(n):
    # Generate deterministic grid of length 14 based on n
    # Ensure positive values and some variability with n
    grid = [((i + 1) * (n + 1)) % 50 + 1 for i in range(14)]

    max_res = 0
    for i in range(14):
        g_c = grid.copy()
        Amount = g_c[i] // 14
        Amount_r = g_c[i] % 14
        if Amount > 0:
            for j in range(14):
                if i != (i + j + 1) % 14:
                    g_c[(i + j + 1) % 14] += Amount
                    g_c[i] -= Amount
        if Amount_r > 0:
            for j in range(14):
                if Amount_r > 0:
                    if i != (i + j + 1) % 14:
                        g_c[(i + j + 1) % 14] += 1
                        Amount_r -= 1
                        g_c[i] -= 1

                else:
                    break

        res = 0
        for k in range(14):
            if g_c[k] % 2 == 0:
                res += g_c[k]

        max_res = max(max_res, res)

    # print(max_res)
    pass
if __name__ == "__main__":
    main(10)
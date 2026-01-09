def main(n):
    pieces = []
    blacks = [0] * 4
    whites = [0] * 4

    # Deterministically generate 4 grids of size n x n
    # Original input was '0'/'1' characters per cell; we mimic that.
    for i in range(4):
        grid = []
        for j in range(n):
            # Deterministic pattern based on i, j, and k
            row = []
            for k in range(n):
                # Create a pseudo "input" character '0' or '1'
                val = (i + j + k) % 2  # 0 or 1
                row.append(str(val))
            grid.append("".join(row))

        count = 0
        for j in range(n):
            for k in range(n):
                if (int(grid[j][k]) + j + k) % 2:
                    count += 1
        blacks[i] = count
        whites[i] = n * n - count

    ans = 4 * n * n
    for white1 in range(3):
        for white2 in range(white1 + 1, 4):
            for black1 in range(4):
                if black1 == white1 or black1 == white2:
                    continue
                for black2 in range(black1 + 1, 4):
                    if black2 == white1 or black2 == white2:
                        continue
                    ans = min(
                        ans,
                        whites[white1] + whites[white2] + blacks[black1] + blacks[black2],
                    )
    # print(ans)
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(5)
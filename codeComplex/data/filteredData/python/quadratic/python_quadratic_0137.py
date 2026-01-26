def main(n):
    # n is the grid size for each of the 4 boards
    pieces = []
    blacks = [0] * 4
    whites = [0] * 4

    # Deterministic grid generator: 4 grids of size n x n, characters '0' or '1'
    # grid[i][j] is determined by (i, j, board_index) in a fixed way
    for board_idx in range(4):
        grid = []
        for j in range(n):
            row_chars = []
            for k in range(n):
                # Simple deterministic pattern depending on board_idx, row, col
                # This yields '0' or '1' as characters
                val = (board_idx + j + 2 * k) % 2
                row_chars.append(str(val))
            grid.append("".join(row_chars))
        # Compute blacks and whites as in original program
        count = 0
        for j in range(n):
            for k in range(n):
                if (int(grid[j][k]) + j + k) % 2:
                    count += 1
        blacks[board_idx] = count
        whites[board_idx] = n * n - count

    ans = 4 * n * n
    for white1 in range(3):
        for white2 in range(white1 + 1, 4):
            for black1 in range(4):
                if black1 == white1 or black1 == white2:
                    continue
                for black2 in range(black1 + 1, 4):
                    if black2 == white1 or black2 == white2:
                        continue
                    ans = min(ans, whites[white1] + whites[white2] + blacks[black1] + blacks[black2])

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)
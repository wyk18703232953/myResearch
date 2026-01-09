def main(n):
    import itertools

    # Deterministic generation of 4 n×n boards as lists of strings
    a = []
    for i in range(4):
        board = []
        for r in range(n):
            row_chars = []
            for c in range(n):
                # Simple deterministic pattern depending on board index, row, and column
                val = (i + r + 2 * c) % 2
                row_chars.append(str(val))
            board.append("".join(row_chars))
        a.append(board)

    best = 4 * n * n
    for p in itertools.permutations(a):
        for s in range(2):
            count = 0
            for i in range(4):
                for r in range(n):
                    for c in range(n):
                        if p[i][r][c] != str((s + (i // 2 + r) + (i % 2 + c)) % 2):
                            count += 1
            if count < best:
                best = count
    # print(best)
    pass
if __name__ == "__main__":
    main(5)
import itertools

def main(n):
    a = []
    for i in range(4):
        grid = []
        for r in range(n):
            row = []
            for c in range(n):
                row.append(str((i + r + c) % 2))
            grid.append("".join(row))
        a.append(grid)

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
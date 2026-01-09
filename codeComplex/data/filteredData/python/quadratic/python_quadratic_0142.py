def main(n):
    from itertools import permutations

    # Deterministic data generation mimicking 4 blocks of n lines of digit-strings
    # Original code reads 4 groups; each group is an n x n grid of digits (0/1 assumed)
    a = []

    # Generate 4 deterministic n x n grids with values derived from indices
    for block in range(4):
        grid = []
        for i in range(n):
            row = []
            for j in range(n):
                # Deterministic pattern depending on block, row, col
                # Ensures values are 0 or 1
                val = (block + i + j) % 2
                row.append(val)
            grid.append(row)
        a.append(grid)

    ans = 10 ** 10
    for perm in permutations(a, 4):
        cnt = 0
        total = 0
        for j in perm:
            if cnt < 2:
                cnt2 = 0
                for p in j:
                    for q in p:
                        if q != cnt2 % 2:
                            total += 1
                        cnt2 += 1

            else:
                cnt2 = 1
                for p in j:
                    for q in p:
                        if q != cnt2 % 2:
                            total += 1
                        cnt2 += 1
            cnt += 1

        if total < ans:
            ans = total

    # print(ans)
    pass
if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(5)
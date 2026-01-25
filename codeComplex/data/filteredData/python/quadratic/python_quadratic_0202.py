def fun(grid, counter, n, m):
    for i in range(n):
        possible = True
        for j in range(m):
            if grid[i][j] == '1' and counter[j] == 1:
                possible = False
                break
        if possible:
            return True
    return False


def main(n):
    if n <= 0:
        return
    m = n
    grid = []
    counter = [0] * m
    for i in range(n):
        row_bits = []
        for j in range(m):
            bit = (i + j) % 2
            if bit == 1:
                counter[j] += 1
            row_bits.append(str(bit))
        grid.append("".join(row_bits))
    if fun(grid, counter, n, m):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(5)
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
    m = max(1, n // 2)
    grid = []
    counter = [0] * m
    for i in range(n):
        row = []
        for j in range(m):
            val = ((i + j) % 3 == 0)
            row.append('1' if val else '0')
        s = ''.join(row)
        for j in range(m):
            if s[j] == '1':
                counter[j] += 1
        grid.append(s)
    if fun(grid, counter, n, m):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)
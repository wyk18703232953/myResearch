def main(n):
    # Interpret n as grid size n x n
    size = n
    # Deterministically generate a grid with a block of 'B's in one row
    # Place 'B's from column n//4 to 3n//4 (at least one B)
    grid = []
    start = size // 4
    end = max(start, (3 * size) // 4)
    for i in range(size):
        if i == size // 2:
            row = ['W'] * size
            for j in range(start, end + 1):
                if j < size:
                    row[j] = 'B'
            grid.append(''.join(row))

        else:
            grid.append('W' * size)

    top = [-1, -1]
    bottom = [-1, -1]

    for i in range(size):
        s = grid[i]
        left = s.find('B')
        if left != -1:
            right = s.rfind('B')
            c = (right - left) // 2 + 1
            # Keep original 1-based style output
            # print(i + c, left + c)
            pass
            break


if __name__ == "__main__":
    main(10)
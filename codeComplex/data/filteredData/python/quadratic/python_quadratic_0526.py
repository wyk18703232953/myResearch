def main(n):
    # Define grid size based on n (for time complexity scaling)
    # Ensure at least 3x3 for the core logic to have effect
    if n < 3:
        n = 3
    m = n

    # Deterministically generate a grid of '#' and '.' characters
    # Example pattern: '#' if (i + j) is even, else '.'
    a = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i * 31 + j * 17) % 3 == 0:
                row.append('#')

            else:
                row.append('.')
        a.append(row)

    # Build the array as in the original program
    array = []
    for i in range(n):
        listt = []
        for c in range(m):
            if a[i][c] == '#':
                listt.append(1)

            else:
                listt.append(0)
        array.append(listt)

    # Core algorithm logic from original code
    for y in range(1, n - 1):
        for x in range(1, m - 1):
            f = a[y + 1][x] == '#' and a[y + 1][x + 1] == '#' and a[y + 1][x - 1] == '#'
            s = a[y][x + 1] == '#' and a[y][x - 1] == '#'
            th = a[y - 1][x] == '#' and a[y - 1][x + 1] == '#' and a[y - 1][x - 1] == '#'
            if f and s and th:
                array[y + 1][x] -= 1
                array[y + 1][x + 1] -= 1
                array[y + 1][x - 1] -= 1
                array[y][x + 1] -= 1
                array[y][x - 1] -= 1
                array[y - 1][x - 1] -= 1
                array[y - 1][x] -= 1
                array[y - 1][x + 1] -= 1

    mb = True
    for y in range(n):
        for x in range(m):
            if array[y][x] == 1:
                mb = False
                break

    if mb:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(1000)
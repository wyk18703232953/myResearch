def main(n):
    # Map n to matrix dimensions: create a near-square grid
    if n <= 0:
        return
    m = n
    # Deterministic generation of cells: pattern based on indices
    # Use '#' and '.' so that algorithm has meaningful work
    global cells
    global paper
    global rows
    global cols

    rows = n
    cols = m

    cells = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            # Deterministic pattern:
            # Place '#' in positions where (i + j) % 3 != 0, '.' otherwise
            if (i + j) % 3 == 0:
                row_chars.append('.')

            else:
                row_chars.append('#')
        cells.append(''.join(row_chars))

    paper = [["." for _ in range(cols)] for _ in range(rows)]

    def writable(r, c):
        if r + 2 >= rows or c + 2 >= cols:
            return False
        t = set()
        t.add(cells[r][c])
        t.add(cells[r][c + 1])
        t.add(cells[r][c + 2])
        t.add(cells[r + 1][c])
        t.add(cells[r + 1][c + 2])
        t.add(cells[r + 2][c])
        t.add(cells[r + 2][c + 1])
        t.add(cells[r + 2][c + 2])
        return '.' not in t

    def fill_ink(r, c):
        paper[r][c] = "#"
        paper[r][c + 1] = "#"
        paper[r][c + 2] = "#"
        paper[r + 1][c] = "#"
        paper[r + 1][c + 2] = "#"
        paper[r + 2][c] = "#"
        paper[r + 2][c + 1] = "#"
        paper[r + 2][c + 2] = "#"

    for r in range(rows):
        for c in range(cols):
            if writable(r, c):
                fill_ink(r, c)

    for r in range(rows):
        for c in range(cols):
            if cells[r][c] != paper[r][c]:
                # print("NO")
                pass
                return

    # print("YES")
    pass
if __name__ == "__main__":
    main(10)
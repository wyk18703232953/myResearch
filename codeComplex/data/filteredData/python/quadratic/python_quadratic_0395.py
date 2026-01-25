def main(n):
    # Interpret n as both matrix dimension and black square size (odd, at most n)
    if n <= 0:
        return
    size = n if n % 2 == 1 else n - 1
    if size <= 0:
        size = 1

    # Build n x n matrix filled with 'W'
    grid = [['W' for _ in range(n)] for _ in range(n)]

    # Place a size x size block of 'B' near the center deterministically
    top = (n - size) // 2
    left = (n - size) // 2
    for i in range(top, top + size):
        for j in range(left, left + size):
            grid[i][j] = 'B'

    # Now run the original logic on this generated grid
    x1 = -1
    x2 = -1
    y1 = -1
    y2 = -1

    for i in range(n):
        s = grid[i]
        for j in range(n):
            if s[j] == 'B':
                if x1 == -1:
                    x1 = j + 1
                x2 = max(x2, j + 1)
                if y1 == -1:
                    y1 = i + 1
                y2 = i + 1

    if x1 == -1:
        # No 'B' cells; define a deterministic fallback, e.g., center of the grid
        cy = (n + 1) // 2
        cx = (n + 1) // 2
        print(cy, cx)
    else:
        print((y1 + y2) // 2, (x1 + x2) // 2)


if __name__ == "__main__":
    main(5)
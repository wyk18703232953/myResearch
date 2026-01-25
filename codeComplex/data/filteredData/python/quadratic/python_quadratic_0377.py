def main(n):
    # Interpret n as both number of rows and columns of the matrix (n x n)
    # Construct a deterministic matrix with a contiguous block of 'B's
    if n <= 0:
        return

    size = n
    # Define a deterministic square of 'B's inside the matrix
    # Side length of the 'B' square
    side = max(1, size // 3)
    # Top-left position of the 'B' square
    start_row = size // 4
    start_col = size // 4
    if start_row + side > size:
        start_row = max(0, size - side)
    if start_col + side > size:
        start_col = max(0, size - side)

    matrix = []
    for i in range(size):
        row_chars = []
        for j in range(size):
            if start_row <= i < start_row + side and start_col <= j < start_col + side:
                row_chars.append('B')
            else:
                row_chars.append('W')
        matrix.append(''.join(row_chars))

    n_rows = size
    m_cols = size

    top = [-1, -1]
    bottom = [-1, -1]

    for i in range(n_rows):
        left = matrix[i].find('B')
        if left != -1:
            top[0] = i
            top[1] = left
            break

    for i in range(n_rows - 1, -1, -1):
        right = matrix[i].rfind('B')
        if right != -1:
            bottom[0] = i
            bottom[1] = right
            break

    print(1 + top[0] + (bottom[0] - top[0]) // 2, 1 + top[1] + (bottom[1] - top[1]) // 2)


if __name__ == "__main__":
    main(10)
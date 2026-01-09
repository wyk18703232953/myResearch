def main(n):
    # n will control the size of the matrix: n x n
    # Construct a deterministic matrix of '.' with a centered square of 'B'
    if n <= 0:
        return

    size = n
    matrix = [['.' for _ in range(size)] for _ in range(size)]

    # Define a square of 'B' with side length s, centered as much as possible
    # s must be >=1 and <= n
    s = max(1, min(size, size // 3 if size >= 3 else 1))
    start_row = (size - s) // 2
    start_col = (size - s) // 2

    for i in range(start_row, start_row + s):
        for j in range(start_col, start_col + s):
            matrix[i][j] = 'B'

    matrix_str = [''.join(row) for row in matrix]

    top = [-1, -1]
    bottom = [-1, -1]

    for i in range(size):
        left = matrix_str[i].find('B')
        if left != -1:
            top[0] = i
            top[1] = left
            break

    for i in range(size - 1, -1, -1):
        right = matrix_str[i].rfind('B')
        if right != -1:
            bottom[0] = i
            bottom[1] = right
            break

    row_center = 1 + top[0] + (bottom[0] - top[0]) // 2
    col_center = 1 + top[1] + (bottom[1] - top[1]) // 2
    # print(row_center, col_center)
    pass
if __name__ == "__main__":
    main(10)
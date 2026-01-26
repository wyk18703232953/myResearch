def main(n):
    # n: matrix size n x n, filled deterministically with '.', and a central 'B' block
    # Build deterministic matrix
    mat = []
    for i in range(n):
        row = ['.'] * n
        mat.append(row)

    # Place a deterministic odd-length horizontal block of 'B's centered in the matrix
    # Ensure length is odd and at least 1
    length = 2 * (n // 4) + 1
    if length > n:
        length = n if n % 2 == 1 else n - 1
    if length < 1:
        length = 1

    center_i = n // 2
    center_j = n // 2
    start_j = center_j - length // 2
    if start_j < 0:
        start_j = 0
    if start_j + length > n:
        start_j = n - length

    for j in range(start_j, start_j + length):
        mat[center_i][j] = 'B'

    # Simulate original input-based logic on this generated matrix
    i = j = -1
    row_index = 0
    while j < 0 and row_index < n:
        row_str = ''.join(mat[row_index])
        j = row_str.find('B')
        if j >= 0:
            i += 1
            c = row_str.count('B') // 2 + 1
            # print(i + c, j + c)
            pass
            return
        i += 1
        row_index += 1

    # If no 'B' found, mimic behavior: original code would loop forever;
    # here we choose to print nothing.


if __name__ == "__main__":
    # Example deterministic call
    main(7)
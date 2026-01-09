def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def flip(matrix):
    return matrix[::-1]

def compare_matrices(first, second, n):
    for i in range(n):
        for j in range(n):
            if first[i][j] != second[i][j]:
                return False
    return True

def wrap(first, second, n):
    if compare_matrices(first, second, n):
        return 'Yes'
    hold_first = [row[:] for row in first]
    for _ in range(3):
        first = rotate_90(first)
        if compare_matrices(first, second, n):
            return 'Yes'
    first = hold_first
    first = flip(first)
    if compare_matrices(first, second, n):
        return 'Yes'
    for _ in range(3):
        first = rotate_90(first)
        if compare_matrices(first, second, n):
            return 'Yes'
    return 'No'

def generate_matrices(n):
    first = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(chr(ord('A') + (i + j) % 26))
        first.append(row)
    # Generate second as a rotated/flipped version in a deterministic way
    # For variety: if n is even, rotate 90; if n % 3 == 1, flip; else keep same
    if n % 2 == 0:
        second = rotate_90(first)
    elif n % 3 == 1:
        second = flip(first)

    else:
        second = [row[:] for row in first]
    return first, second

def main(n):
    first, second = generate_matrices(n)
    result = wrap(first, second, n)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)
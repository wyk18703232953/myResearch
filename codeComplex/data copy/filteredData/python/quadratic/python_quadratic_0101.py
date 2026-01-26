def main(n):
    # Generate two n x n matrices of characters deterministically
    # mat1 will be a pattern, mat2 will be another pattern that sometimes matches under rotation
    # Here: mat2 is designed so that when n is even, rotating mat2 once matches mat1; otherwise it doesn't.

    # Build mat1: character at (i, j) is based on (i + j) % 26 mapped to lowercase letters
    mat1 = []
    for i in range(n):
        row = []
        for j in range(n):
            val = (i + j) % 26
            row.append(chr(ord('a') + val))
        mat1.append(tuple(row))

    # Build mat2 initially as a copy of mat1
    mat2 = [tuple(row) for row in mat1]

    # For odd n, modify mat2 so that no rotation will match mat1 (simple deterministic tweak)
    if n % 2 == 1:
        # Flip the first row in a deterministic way
        if n > 0:
            first_row = list(mat2[0])
            first_row = first_row[::-1]
            mat2[0] = tuple(first_row)

    import copy

    mats = []
    mats.append(mat2)
    matu = copy.copy(mat2)
    matv = copy.copy(mat2)
    matv = list(zip(*matv))
    mats.append(matv)

    mattem = copy.copy(matu)
    for _ in range(3):
        mattem = list(zip(*list(reversed(mattem))))
        mats.append(mattem)
    mattem = copy.copy(matv)
    for _ in range(3):
        mattem = list(zip(*list(reversed(mattem))))
        mats.append(mattem)

    flg = 0
    for cmat in mats:
        flg2 = 1
        for ri in range(0, n):
            if cmat[ri] != mat1[ri]:
                flg2 = 0
                break
        if flg2 == 1:
            flg = 1
            break
    if flg == 1:
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    # Example deterministic call for testing / complexity experiments
    main(5)
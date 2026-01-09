def main(n):
    import copy

    # Generate deterministic matrices mat1 and mat2 of size n x n
    # Characters are chosen deterministically from a small alphabet
    alphabet = ('a', 'b', 'c', 'd')
    mat1 = []
    mat2 = []
    for i in range(n):
        row1 = [alphabet[(i * n + j) % len(alphabet)] for j in range(n)]
        row2 = [alphabet[(i * n + j + 1) % len(alphabet)] for j in range(n)]
        mat1.append(tuple(row1))
        mat2.append(tuple(row2))

    flg = 0
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
    main(5)
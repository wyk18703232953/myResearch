def rotate(li, n):
    newli = []
    for x in range(0, n):
        newli.append([])
        newli[x] = li[x].copy()
    for x in range(0, n):
        for y in range(0, n):
            newli[x][y] = li[n - 1 - y][x]
    return newli

def flipV(li, n):
    newli = []
    for x in range(0, n):
        newli.append([])
        newli[x] = li[x].copy()
    newli.reverse()
    return newli

def flipH(li, n):
    newli = []
    for x in range(0, n):
        newli.append([])
        newli[x] = li[x].copy()
    for x in range(0, n):
        newli[x].reverse()
    return newli

def generate_matrix(n):
    # Deterministic n x n matrix of characters
    # pattern: chr(ord('a') + (i + j) % 26)
    return [[chr(ord('a') + (i + j) % 26) for j in range(n)] for i in range(n)]

def transform_for_li2(matrix, n):
    # Deterministic choice of transformation based on n
    # 0: identical
    # 1: flipH
    # 2: flipV
    # 3: rotate 90
    # 4: rotate 180
    # 5: rotate 270
    # 6: flipH then rotate 90
    t = n % 7
    if t == 0:
        return matrix
    elif t == 1:
        return flipH(matrix, n)
    elif t == 2:
        return flipV(matrix, n)
    elif t == 3:
        return rotate(matrix, n)
    elif t == 4:
        return rotate(rotate(matrix, n), n)
    elif t == 5:
        return rotate(rotate(rotate(matrix, n), n), n)
    else:  # t == 6
        tmp = flipH(matrix, n)
        return rotate(tmp, n)

def main(n):
    if n <= 0:
        return
    li1 = generate_matrix(n)
    li2 = transform_for_li2(li1, n)

    # original logic starts here
    templi = []

    # identical
    if li1 == li2:
        print('Yes')
        return

    # flip horizontal
    templi = flipH(li2, n)
    if li1 == templi:
        print('Yes')
        return

    # flip vertical
    templi = flipV(li2, n)
    if li1 == templi:
        print('Yes')
        return

    # rotate1
    templi = rotate(li2, n)
    if li1 == templi:
        print('Yes')
        return

    # rotate2
    templi = rotate(templi, n)
    if li1 == templi:
        print('Yes')
        return

    # rotate3
    templi = rotate(templi, n)
    if li1 == templi:
        print('Yes')
        return

    # flip then rotates
    templi = flipH(li2, n)
    templi = rotate(templi, n)
    if li1 == templi:
        print('Yes')
        return

    templi = rotate(templi, n)
    if li1 == templi:
        print('Yes')
        return

    templi = rotate(templi, n)
    if li1 == templi:
        print('Yes')
        return

    print('No')

if __name__ == "__main__":
    main(5)
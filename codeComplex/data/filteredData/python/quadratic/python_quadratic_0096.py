def main(n):
    # Generate deterministic n x n matrices ns and ns2
    # ns: each cell is a character derived from row and column
    # ns2: apply a fixed transformation (rotate then flip) so some n will yield True, others False
    ns = []
    for i in range(n):
        row = []
        for j in range(n):
            # Map (i, j) to a lowercase letter deterministically
            row.append(chr(ord('a') + (i * n + j) % 26))
        ns.append(''.join(row))

    ns2 = []
    for i in range(n):
        row = []
        for j in range(n):
            # Apply a composed transformation: rotate 90 then flip
            # to original indices to construct ns2 deterministically
            # This mirrors one of the checked transformations
            a = j
            b = n - 1 - i
            a, b = b, a  # flip
            row.append(ns[a][b])
        ns2.append(''.join(row))

    def rotate(i, j):
        return j, n - 1 - i

    def flip(i, j):
        return j, i

    same = True
    for i in range(n):  # 0
        for j in range(n):
            if ns[i][j] != ns2[i][j]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 1
        for j in range(n):
            a, b = rotate(i, j)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 2
        for j in range(n):
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same = True
    for i in range(n):
        for j in range(n):  # 3
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            a, b = rotate(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 0 with flip
        for j in range(n):
            a, b = flip(i, j)
            if ns[a][b] != ns2[i][j]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 1
        for j in range(n):
            a, b = rotate(i, j)
            a, b = flip(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 2
        for j in range(n):
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            a, b = flip(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same = True
    for i in range(n):
        for j in range(n):  # 3
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            a, b = rotate(a, b)
            a, b = flip(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    else:
        return False


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    result = main(5)
    # print("Yes" if result else "No")
    pass
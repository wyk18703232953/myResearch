def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

def main(n):
    # Ensure n >= 1 for meaningful matrix
    if n <= 0:
        return

    # Deterministically construct matrix a and b of size n x n
    # a has a pattern based on (i + j) % 2
    a = [['#' if (i + j) % 2 == 0 else '.' for j in range(n)] for i in range(n)]

    # b is constructed by rotating a 90 degrees clockwise twice (i.e., 180 degrees)
    # to keep relation deterministic but non-trivial
    b = [row[:] for row in a]
    # first 90-degree clockwise rotation
    c = [['' for _ in range(n)] for _ in range(n)]
    for t in range(n):
        for u in range(n):
            c[t][u] = b[n - u - 1][t]
    b = [row[:] for row in c]
    # second 90-degree clockwise rotation (total 180 degrees)
    c = [['' for _ in range(n)] for _ in range(n)]
    for t in range(n):
        for u in range(n):
            c[t][u] = b[n - u - 1][t]
    b = [row[:] for row in c]

    for _ in range(4):
        for _ in range(2):
            if check(a, b):
                # print('Yes')
                pass
                return
            b = b[::-1]
        for _ in range(2):
            if check(a, b):
                # print('Yes')
                pass
                return
            b = [s[::-1] for s in b]
        c = [['' for _ in range(n)] for _ in range(n)]
        for t in range(n):
            for u in range(n):
                c[t][u] = b[u][n - t - 1]
        b = [row[:] for row in c]
        if check(a, b):
            # print('Yes')
            pass
            return
    # print('No')
    pass
if __name__ == "__main__":
    main(5)
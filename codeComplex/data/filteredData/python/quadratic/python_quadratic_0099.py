from itertools import chain, combinations, permutations

def powerset(iterable):
    xs = list(iterable)
    return chain.from_iterable(combinations(xs, k) for k in range(len(xs) + 1))

def make_matrix(n, offset):
    # deterministic n x n matrix with characters derived from indices and offset
    return [[chr(97 + (i * n + j + offset) % 26) for j in range(n)] for i in range(n)]

def copy_matrix(m):
    n = len(m)
    res = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(m[i][j])
        res.append(row)
    return res

def rotate90(m):
    n = len(m)
    res = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(m[n - 1 - j][i])
        res.append(row)
    return res

def vert(m):
    n = len(m)
    res = []
    for i in range(n):
        res.append(m[i][::-1])
    return res

def gor(m):
    n = len(m)
    res = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(m[i][n - 1 - j])
        res.append(row)
    return res

def compute_result(cl1, cl2):
    n = len(cl1)
    def copy(m):
        return copy_matrix(m)

    def pow_m(m):
        return rotate90(m)

    comblist = [[1], []]  # unused but kept to preserve structure
    cm = [pow_m, pow_m, pow_m, vert, gor]
    cm = list(powerset(cm))
    res = False
    if cl1 == cl2:
        res = True
    else:
        for x in cm:
            for y in permutations(x):
                t = copy(cl1)
                for z in y:
                    t = z(t)
                if t == cl2:
                    res = True
                    break
            if res:
                break
    return res

def main(n):
    if n <= 0:
        n = 1
    cl1 = make_matrix(n, 0)
    # for even n, make cl2 reachable by a fixed sequence of transformations;
    # for odd n, use a different deterministic target to get "No"
    if n % 2 == 0:
        cl2 = vert(rotate90(cl1))
    else:
        cl2 = make_matrix(n, n)
    res = compute_result(cl1, cl2)
    if res:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main(4)
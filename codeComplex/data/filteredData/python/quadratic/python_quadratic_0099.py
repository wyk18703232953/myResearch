from itertools import chain, combinations, permutations

def powerset(iterable):
    xs = list(iterable)
    return chain.from_iterable(combinations(xs, k) for k in range(len(xs) + 1))

def main(n):
    cl1 = []
    cl2 = []
    # 生成两个 n x n 字符矩阵，完全确定性
    for i in range(n):
        row = [chr(ord('a') + (i + j) % 26) for j in range(n)]
        cl1.append(row)
    for i in range(n):
        row = [chr(ord('a') + (i * 2 + j * 3) % 26) for j in range(n)]
        cl2.append(row)

    def copy(m):
        res = []
        for i in range(n):
            a = []
            for j in range(n):
                a.append(m[i][j])
            res.append(a)
        return res

    def pow_mat(m):
        res = []
        for i in range(n):
            a = []
            for j in range(n):
                a.append(m[n - 1 - j][i])
            res.append(a)
        return res

    def vert(m):
        res = []
        for i in range(n):
            res.append(m[i][::-1])
        return res

    def gor(m):
        res = []
        for i in range(n):
            a = []
            for j in range(n):
                a.append(m[i][n - 1 - j])
            res.append(a)
        return res

    cm = [pow_mat, pow_mat, pow_mat, vert, gor]
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

    if res:
        # print('Yes')
        pass

    else:
        # print('No')
        pass
if __name__ == "__main__":
    main(5)
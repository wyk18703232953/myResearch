def check(val, A, M):
    s = set()
    for row in A:
        v = 0
        for u in row:
            v <<= 1
            if u >= val:
                v |= 1
        s.add(v)

    x = 1 << M
    for u in s:
        for v in range(x):
            if v in s and (u | v) == x - 1:
                return True
    return False


def getAnswer(val, A, M):
    vi = {}
    for i, row in enumerate(A):
        v = 0
        for u in row:
            v <<= 1
            if u >= val:
                v |= 1
        vi[v] = i

    x = 1 << M
    for u in vi:
        for v in range(x):
            if v in vi and (u | v) == x - 1:
                return vi[u], vi[v]
    return 0, 0


def solve(N, M, A):
    lo, hi = 0, max(max(row) for row in A)
    while lo <= hi:
        m = (lo + hi) // 2
        if check(m, A, M):
            lo = m + 1
        else:
            hi = m - 1
    a, b = getAnswer(hi, A, M)
    print(f"{a + 1} {b + 1}")


def main(n):
    # 映射规模含义：
    # N = n       行数
    # M = 10      列数（固定，保证位运算规模稳定）
    # A[i][j] = (i + 1) * (j + 1) 确定性生成
    if n <= 0:
        return
    N = n
    M = 10
    A = [[(i + 1) * (j + 1) for j in range(M)] for i in range(N)]
    solve(N, M, A)


if __name__ == "__main__":
    main(1000)
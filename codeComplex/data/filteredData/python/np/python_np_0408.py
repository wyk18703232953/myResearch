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
    lo, hi = 0, max([max(row) for row in A])

    while lo <= hi:
        m = (lo + hi) // 2
        if check(m, A, M):
            lo = m + 1
        else:
            hi = m - 1

    a, b = getAnswer(hi, A, M)
    print("{} {}".format(a + 1, b + 1))


def generate_data(n):
    # 解释输入结构：
    # 原程序输入：
    #   N M
    #   N 行，每行 M 个整数
    #
    # 这里将 n 映射为：
    #   N = n
    #   M = max(1, n // 2)
    #
    # 构造 A 为一个 N x M 的矩阵，元素确定性生成：
    #   A[i][j] = (i * 17 + j * 23) % (n + 7)
    # 保证对相同的 n，多次运行生成的数据完全一致。
    if n <= 0:
        N = 1
        M = 1
    else:
        N = n
        M = max(1, n // 2)

    A = []
    base = n + 7
    for i in range(N):
        row = []
        for j in range(M):
            val = (i * 17 + j * 23) % base
            row.append(val)
        A.append(row)
    return N, M, A


def main(n):
    N, M, A = generate_data(n)
    solve(N, M, A)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小进行复杂度实验
    main(10)
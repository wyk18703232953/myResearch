def check(mid, m, a):
    from collections import defaultdict
    d = defaultdict(int)
    for idx, row in enumerate(a):
        string = ''
        for val in row:
            if val >= mid:
                string += '1'
            else:
                string += '0'
        d[int(string, 2)] = idx
    full_mask = (1 << m) - 1
    keys = list(d.keys())
    for i in keys:
        for j in keys:
            if (i | j) == full_mask:
                return [d[i], d[j]]
    return []


def binarySearch(lo, hi, m, a):
    ans = []
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        x = check(mid, m, a)
        if x:
            lo = mid
            ans = [x[0] + 1, x[1] + 1]
        else:
            hi = mid - 1
    return ans


def main(n):
    # 映射含义：
    # n -> 行数 n
    # m  -> 列数 = max(1, n // 2)（可规模化）
    # 矩阵 a[i][j] 为确定性构造：a[i][j] = (i + 1) * (j + 2)
    if n <= 0:
        print()
        return

    m = max(1, n // 2)
    a = [[(i + 1) * (j + 2) for j in range(m)] for i in range(n)]
    res = binarySearch(-1, 10**9 + 1, m, a)
    if res:
        print(*res)
    else:
        print()


if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)
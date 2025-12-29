def solve(n, k):
    if n >= 60:
        return "YES " + str(n - 1)

    mxxx = (4 ** n - 1) // 3

    if k > mxxx:
        return 'NO'

    mn, mx = 0, 0

    for i in range(n):
        mn += 2 ** (i + 1) - 1
        mx += 4 ** i
        if mn <= k and mx >= k:
            return "YES " + str(n - i - 1)

    if 22 <= k <= 25:
        return 'YES ' + str(n - 3)

    if k == 2:
        if n >= 2:
            return 'YES ' + str(n - 1)
        return 'NO'

    if k == 3:
        if n <= 2:
            return 'NO'
        return 'YES ' + str(n - 1)

    if 6 <= k <= 10:
        return 'YES ' + str(n - 2)

    return 'NO'


def main(n):
    # 根据规模 n 生成测试数据：
    # 测试 t 组数据，其中 n 作为规模上界。
    # 生成一些有代表性的 k，包括边界和中间值。
    tests = []

    # 1. 固定 n，遍历一部分典型 k
    k_candidates = set()

    # 小范围特殊值
    k_candidates.update([1, 2, 3, 4, 5, 6, 10, 22, 23, 24, 25])

    # 与 mxxx 相关的边界
    if n < 60:
        mxxx = (4 ** n - 1) // 3
        k_candidates.update([mxxx - 2, mxxx - 1, mxxx, mxxx + 1])

    # 去掉非正和过大的
    k_list = sorted(k for k in k_candidates if 1 <= k <= 10**18)

    for k in k_list:
        tests.append((n, k))

    # 再加上一些随机/规律性生成的 k（这里用线性间隔代替）
    if n < 60:
        mxxx = (4 ** n - 1) // 3
        step = max(1, mxxx // 5)
        for i in range(1, 6):
            k = i * step
            if 1 <= k <= mxxx:
                tests.append((n, k))

    # 去重测试数据
    tests = list(dict.fromkeys(tests))

    # 输出测试结果
    for n_i, k_i in tests:
        print(f"n={n_i}, k={k_i} -> {solve(n_i, k_i)}")


if __name__ == "__main__":
    # 示例：以 n=10 作为规模运行
    main(10)
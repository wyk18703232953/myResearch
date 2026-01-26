def suma(n):
    return n * (n + 1) // 2


def sumaij(i, j):
    if i <= 1:
        return suma(j)
    return suma(j) - suma(i - 1)


def bin_search_solution(n, k):
    st, end = 1, k
    while st < end:
        mid = (st + end) // 2
        s = sumaij(mid, k)
        if s == n:
            return k - mid + 1
        if s > n:
            st = mid + 1

        else:
            end = mid
    return k - st + 2


def solve(n, k):
    if n == 1:
        return 0
    elif k >= n:
        return 1

    else:
        n -= 1
        k -= 1

        if suma(k) < n:
            return -1

        else:
            res = bin_search_solution(n, k)
            return res


def main(n):
    """
    n 为规模参数，用于生成测试数据 (n, k) 并调用原逻辑。
    这里简单生成：
        n_val = n
        k_val = max(1, n // 2)
    返回 solve(n_val, k_val) 的结果。
    """
    n_val = n
    k_val = max(1, n // 2)
    result = solve(n_val, k_val)
    # print(result)
    pass
if __name__ == '__main__':
    # 示例：用规模 n=10 运行
    main(10)
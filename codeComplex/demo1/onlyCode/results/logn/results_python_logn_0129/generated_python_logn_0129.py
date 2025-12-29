def s(n):
    return (n * (n + 1)) // 2


def diff(st, en):
    return s(en) - s(st - 1)


def bs(k, n):
    st = 1
    en = k
    while st < en:
        mid = (st + en) // 2
        sum_val = diff(mid, k)
        if sum_val == n:
            return k - mid + 1
        if sum_val > n:
            st = mid + 1
        else:
            en = mid
    return k - st + 2


def solve_single(n, k):
    if n == 1:
        return 0
    elif n <= k:
        return 1
    else:
        n -= 1
        k -= 1
        if s(k) < n:
            return -1
        else:
            return bs(k, n)


def main(n):
    """
    规模参数 n 用于生成测试数据 (n_i, k_i)。
    这里示例生成方式为：
      n_i = i + 1
      k_i = min(i + 2, 2 * n)
    并对这些测试数据调用原逻辑。
    """
    results = []
    for i in range(1, n + 1):
        n_i = i + 1
        k_i = min(i + 2, 2 * n)
        results.append(solve_single(n_i, k_i))
    # 输出所有结果，每行一个
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 示例：使用规模 n=5 运行
    main(5)
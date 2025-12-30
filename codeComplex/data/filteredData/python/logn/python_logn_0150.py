def normal_sum(N: int) -> int:
    return (N ** 2 + N) // 2


def range_sum(i: int, j: int) -> int:
    # 对应原代码的 sum(i, j)（避免与内置 sum 冲突）
    return normal_sum(j) - 1 - (normal_sum(i - 1) - 1)


def bs_sum(start: int, end: int, k: int, n: int) -> int:
    mid = (start + end) // 2

    if n - range_sum(mid, k) >= mid:
        return bs_sum(start, mid - 1, k, n)
    if n - range_sum(mid, k) < 0:
        return bs_sum(mid + 1, end, k, n)

    return k - mid + 2 if (n - range_sum(mid, k)) != 0 else k - mid + 1


def solve_single_case(n: int, k: int) -> int:
    if n == 1:
        return 0
    elif n <= k:
        return 1
    elif normal_sum(k) - 1 - (k - 2) < n:
        return -1
    else:
        n -= 1
        k -= 1
        return bs_sum(1, k, k, n)


def main(n: int):
    """
    n 为规模参数，用于生成测试数据 (n, k) 并输出答案。
    这里简单生成 k = n，用于规模为 n 的测试。
    可以根据需要修改生成策略。
    """
    k = n  # 根据规模生成测试数据，这里设为 k = n
    ans = solve_single_case(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
def sum_upto(n):
    return (n * (n + 1)) // 2


def range_sum(left, right):
    return sum_upto(right) - sum_upto(left - 1)


def binary_search(k, n):
    low, high = 1, k
    while low <= high:
        mid = (low + high) // 2
        s = range_sum(mid, k)

        if s == n:
            return k - mid + 1
        elif s > n:
            low = mid + 1
        else:
            high = mid - 1

    return k - low + 2


def solve(n, k):
    if n == 1:
        return 0
    if n <= k:
        return 1

    n -= 1
    k -= 1

    if n > sum_upto(k):
        return -1
    return binary_search(k, n)


def main(n):
    """
    n: 规模参数，用于生成一组测试数据 (N, K)
    简单策略：N = n, K = n // 2 + 1（保证一部分情况下有解）
    """
    N = n
    K = max(1, n // 2 + 1)
    ans = solve(N, K)
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)
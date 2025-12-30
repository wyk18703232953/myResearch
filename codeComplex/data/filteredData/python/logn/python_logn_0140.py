def sum_upto(n):
    return (n * (n + 1)) // 2


def range_sum(left, right):
    return sum_upto(right) - sum_upto(left - 1)


def binary_search(k, n):
    low, high, mid = 1, k, 0

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
    elif n <= k:
        return 1
    else:
        n -= 1
        k -= 1

        if n > sum_upto(k):
            return -1
        else:
            return binary_search(k, n)


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里假设测试数据为：
    # n_test = n
    # k_test = n（可根据需要调整生成策略）
    n_test = n
    k_test = n

    ans = solve(n_test, k_test)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
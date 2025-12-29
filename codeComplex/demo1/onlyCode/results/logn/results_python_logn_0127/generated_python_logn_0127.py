def sum_upto(num):
    return (num * (num + 1)) // 2


def sum_from_to(fromm, to):
    if fromm <= 1:
        return sum_upto(to)
    return sum_upto(to) - sum_upto(fromm)


def min_splitters(n, k):
    start = 1
    end = k
    while start < end:
        mid = (start + end) // 2
        mid_val = sum_from_to(mid, k)
        if mid_val == n:
            return k - mid + 1
        elif mid_val > n:
            start = mid + 1
        else:
            end = mid
    return k - start + 1


def main(n):
    """
    n 作为规模，用于生成测试数据：
    - 我们令原题中的 k = n（保证有一定规模关联）
    - 原题输入为 (N, K)，这里构造：
        N = n + 1
        K = n
    你可以根据需要更改生成规则。
    """
    N = n + 1
    K = n

    # 原逻辑从这里开始
    n_val, k_val = N, K

    if n_val == 1:
        result = 0
    elif n_val <= k_val:
        result = 1
    else:
        k_val -= 1
        n_val -= 1
        if sum_upto(k_val) < n_val:
            result = -1
        else:
            result = min_splitters(n_val, k_val)

    print(result)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)
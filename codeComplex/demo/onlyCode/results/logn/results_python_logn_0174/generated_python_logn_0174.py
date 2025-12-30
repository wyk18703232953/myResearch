def bs(n, k, lo, hi):
    while lo <= hi:
        mid = (hi + lo) // 2
        summ = ((k * (k + 1)) // 2 - 1) - (((mid - 1) * mid) // 2 - 1) - (k - 2)

        if summ == n:
            return k - mid + 1
        if summ > n:
            lo = mid + 1
        else:  # summ < n
            hi = mid - 1

    if summ > n:
        mid += 1
    return k - mid + 1


def solve(n, k):
    if n == 1:
        return 0
    elif (k * (k + 1) // 2) - (k - 2) <= n:
        return -1
    elif k >= n:
        return 1
    else:
        return bs(n, k, 2, k)


def main(n):
    """
    按规模 n 生成一组测试数据 (n_val, k) 并返回 solve 的结果。
    这里将测试规模 n 同时用作 n_val 和 k，可按需要修改生成规则。
    """
    n_val = n
    k = n
    return solve(n_val, k)


if __name__ == "__main__":
    # 示例：规模取 10，可按需修改
    print(main(10))
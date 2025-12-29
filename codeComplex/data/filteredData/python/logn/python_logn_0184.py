def func(mid, s):
    p = 0
    q = mid
    while mid > 0:
        p += mid % 10
        mid //= 10
    return (q - p) >= s


def main(n):
    """
    n: 规模参数，用于生成测试数据。
       这里我们按照题意生成一个 s，使得 0 <= s <= 10^18，
       并让 n 本身作为原程序中的 n。
    """
    # 根据 n 生成测试数据，这里简单设定：
    # s = n // 2 （可根据需要更改生成规则）
    s = n // 2

    lo = 1
    hi = 10**18
    ans = n + 1

    while hi >= lo:
        mid = (lo + hi) // 2
        if func(mid, s):
            hi = mid - 1
            ans = mid
        else:
            lo = mid + 1

    if ans > n:
        print(0)
    else:
        print(n - ans + 1)


if __name__ == "__main__":
    # 示例：调用 main(10**6) 作为测试
    main(10**6)
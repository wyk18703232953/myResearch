def getRemain(action, n):
    n -= action
    ans = (n * (n + 1) // 2) - action
    return ans


def main(n):
    # 解释规模映射：
    # 原程序有两个输入 n, k。这里将参数 n 视为原问题规模的 n，
    # 并且构造 k 为关于 n 的确定性函数，以保证可规模化与可重复实验。
    #
    # 为了保证在不同 n 下都有非平凡的二分搜索过程，
    # 构造 k 为某个合法的 remain 值。这里选择 action = n // 3，
    # 因此 k = getRemain(action, n)。
    if n <= 0:
        # print(0)
        pass
        return

    original_n = n
    action = original_n // 3
    if action <= 0:
        action = 1
    if action > original_n:
        action = original_n

    k = getRemain(action, original_n)

    l = 1
    r = original_n
    res = 0
    while l <= r:
        mid = l + (r - l) // 2
        remain = getRemain(mid, original_n)
        if remain == k:
            res = mid
            break
        if remain > k:
            l = mid + 1

        else:
            r = mid - 1
    # print(res)
    pass
if __name__ == "__main__":
    # 示例：以 10 作为规模参数运行一次
    main(10)
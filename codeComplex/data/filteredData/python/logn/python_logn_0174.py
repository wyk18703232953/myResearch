def bs(n, k, lo, hi):
    summ = 0  # to ensure it's defined if while never runs
    mid = lo
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
    根据规模 n 生成测试数据并调用 solve。
    这里约定：k 也与规模相关，示例中取 k = n。
    如需不同测试方式，可在此处修改生成策略。
    """
    k = n  # 简单的测试数据生成策略：让 k 与 n 同阶
    return solve(n, k)


if __name__ == "__main__":
    # 示例：运行 main(10) 进行简单测试
    print(main(10))
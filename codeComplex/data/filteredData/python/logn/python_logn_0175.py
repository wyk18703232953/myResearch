def bs(n, k, lo, hi):
    while lo <= hi:
        mid = (hi + lo) // 2
        summ = ((k * (k + 1)) // 2 - 1) - (((mid - 1) * mid) // 2 - 1) - (k - 2)
        if summ == n:
            return k - mid + 1
        elif summ > n:
            lo = mid + 1
        else:  # summ < n
            hi = mid - 1
    # 循环结束后，summ 和 mid 仍是最后一次计算的值
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
    # 根据规模 n 生成测试数据：
    # 这里设定 k = n，用于构造一组规模和参数都为 n 的测试
    k = n
    return solve(n, k)


if __name__ == "__main__":
    # 示例：运行 main(10)
    print(main(10))
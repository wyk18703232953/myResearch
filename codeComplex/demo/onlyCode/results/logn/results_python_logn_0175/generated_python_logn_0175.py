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
    规模参数 n：用来生成测试数据 (n, k)
    这里简单设定 k = n，保持与原题典型使用场景相近。
    如需其他策略，可按需调整生成方式。
    """
    k = n
    return solve(n, k)


if __name__ == "__main__":
    # 示例：调用 main(10)
    print(main(10))
def main(n):
    # 生成测试数据：给定规模 n，构造一个与原程序等价的 k
    # 这里简单设定 k = 2 * n + 10，保证 k 足够大以体现二分逻辑
    k = 2 * n + 10

    l, r = -1, k + 1
    while l + 1 < r:
        mid = (l + r) >> 1
        val = (k - mid + 1 + k) * mid // 2 - (mid - 1)
        if val < n:
            l = mid
        else:
            r = mid

    result = -1 if r == k + 1 else r
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)
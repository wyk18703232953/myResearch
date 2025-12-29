def main(n):
    # 生成测试数据：根据规模 n 构造一个 k
    # 这里示例设定 k = n，保证规模随 n 线性增长
    k = n

    f = lambda m, k: (k * m - m * (m - 1) // 2 - m + 1)

    def ok(m, k, n):
        return f(m, k) >= n

    # 原逻辑
    if not ok(k, k, n):
        print(-1)
    else:
        l, h = 0, k
        while h > l:
            mid = l + (h - l) // 2
            if ok(mid, k, n):
                h = mid
            else:
                l = mid + 1
        print(h)


if __name__ == "__main__":
    # 示例：调用 main，规模参数可自行调整
    main(10)
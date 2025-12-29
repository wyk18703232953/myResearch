def main(n):
    # 生成测试数据：根据规模 n 构造原程序中的 n, k
    # 原程序第一行是: n, k = map(int, input().split())
    # 这里我们令原始的 n = n，k = n（也可以按需调整生成规则）
    orig_n = n
    orig_k = n

    # 按原始程序逻辑转换
    n, k = orig_n - 1, orig_k - 1
    l = 0
    r = k
    g = k * (k + 1) // 2
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if (g - m * (m + 1) // 2) >= n:
            ans = k - m
            l = m + 1
        else:
            r = m - 1
    print(ans)


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n 的值进行测试
    main(10)
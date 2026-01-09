def main(n):
    # 根据 n 生成测试数据：
    # 这里简单设定：
    #   m = n
    #   对于 i=0..m-1:
    #       x_i = i
    #       d_i = (-1)**i * i
    #
    # 如需不同测试方式，可在此处修改生成规则。
    m = n

    # 原逻辑计算 MAX 和 MIN
    MAX = 0
    MIN = 10**18
    for i in range(n):
        l = i * (i + 1) // 2
        r = (n - 1 - i) * (n - 1 - i + 1) // 2
        v = l + r
        MAX = max(MAX, v)
        MIN = min(MIN, v)

    ans = 0
    for i in range(m):
        x = i
        d = (-1) ** i * i
        ans += n * x
        if d >= 0:
            ans += d * MAX

        else:
            ans += d * MIN

    # print(ans / n)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)
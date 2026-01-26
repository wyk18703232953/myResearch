def main(n):
    # 根据规模 n 生成测试数据，这里设定 k 为一个与 n 相关的值
    # 可根据需要修改生成规则
    k = n  # 示例：令 k = n

    l = 0
    r = n + 1
    while r - l > 1:
        m = (l + r) // 2
        if m * (m + 1) // 2 - (n - m) > k:
            r = m

        else:
            l = m
    # print(n - l)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
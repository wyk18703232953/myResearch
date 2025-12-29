def main(n):
    # 自动生成 s：确保在一般情况下有一定数量的解
    # 这里生成一个中等大小的 s，随 n 线性变化
    s = max(1, n // 3)

    l = 0
    r = n + 1

    while r - l > 1:
        x = (l + r) // 2
        cs = 0
        m = x
        # 计算 x 的各位数字之和
        while m > 0:
            cs += m % 10
            m //= 10
        if x - cs >= s:
            r = x
        else:
            l = x

    # 输出与原逻辑一致：满足条件的 x 的个数
    print(n - l)


if __name__ == "__main__":
    # 示例：可修改此处测试不同规模 n
    main(10**6)
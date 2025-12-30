def main(n):
    # 根据 n 生成测试数据，这里按照题意构造一个合理的 s
    # 原题逻辑是统计满足 x - sum_digits(x) >= s 的 x 的个数
    # 这里我们将 s 设置为 n 的一半，当然可以根据需要调整生成规则
    s = n // 2

    l = 0
    r = n + 1

    while r - l > 1:
        x = (l + r) // 2
        cs = 0
        m = x
        while m > 0:
            cs += m % 10
            m //= 10
        if x - cs >= s:
            r = x
        else:
            l = x

    print(n - l)


if __name__ == "__main__":
    # 示例：调用 main，n 可以按需求调整
    main(10**6)
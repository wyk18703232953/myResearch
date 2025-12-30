def main(n):
    # 生成测试数据：1 到 n 的所有整数作为待判断的 n
    # 对原程序来说，这些是 t 个测试用例
    for x in range(1, n + 1):
        val = x

        if val % 2 == 1:
            print('NO')
            continue

        val //= 2

        # 检查 val 是否是某个整数的平方
        l, r = 0, val + 2
        while r - l > 1:
            m = (l + r) // 2
            if m * m <= val:
                l = m
            else:
                r = m
        if l * l == val:
            print('YES')
            continue

        # 检查 val 是否是 2 * (某个整数的平方)
        l, r = 0, val + 2
        while r - l > 1:
            m = (l + r) // 2
            if m * m * 2 <= val:
                l = m
            else:
                r = m
        if l * l * 2 == val:
            print('YES')
            continue

        print('NO')


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)
def main(n):
    # n 表示数组长度
    if n <= 0:
        print()
        return

    # 确定性生成长度为 n 的整数数组
    # 既有正数也有负数，便于保留原算法行为特征
    l1 = [i * (-1 if i % 3 == 0 else 1) for i in range(n)]

    if n % 2 == 0:
        for i in range(n):
            if l1[i] >= 0:
                l1[i] = -1 * l1[i] - 1
    else:
        for i in range(n):
            if l1[i] >= 0:
                l1[i] = -1 * l1[i] - 1
        idx = l1.index(min(l1))
        l1[idx] = l1[idx] * -1 - 1

    print(' '.join(str(x) for x in l1))


if __name__ == "__main__":
    # 示例：使用规模 n = 10 运行
    main(10)
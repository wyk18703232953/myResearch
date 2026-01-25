def main(n):
    # n 表示列表长度
    a = n
    # 构造一个长度为 n 的列表，其中恰好有一个数与其他数的奇偶性不同
    # 前 n-1 个元素为偶数，最后一个元素为奇数（当 n > 1）
    if n <= 0:
        return
    if n == 1:
        b = [2]  # 单元素，偶数
    else:
        b = [2 * i for i in range(1, n)] + [2 * n + 1]
    c = [int(i % 2 == 0) for i in b]
    if c.count(1) == 1:
        print(c.index(1) + 1)
    else:
        print(c.index(0) + 1)


if __name__ == "__main__":
    main(10)
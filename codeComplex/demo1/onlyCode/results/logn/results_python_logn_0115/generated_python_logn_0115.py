def main(n):
    # 生成测试数据：根据规模 n 构造一组 (l, r)
    # 这里示例为：
    #   l = n
    #   r = 2*n + 1  （保证通常 l != r 且 r > l）
    l = n
    r = 2 * n + 1

    if l == r:
        print(0)
    else:
        x = l ^ r
        c = 0
        while x > 0:
            x = x // 2
            c = c + 1
        print(2 ** c - 1)


if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 测试不同规模
    main(10)
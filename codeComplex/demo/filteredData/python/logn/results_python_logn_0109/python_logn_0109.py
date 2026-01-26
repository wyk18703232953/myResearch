def main(n):
    # 根据规模 n 生成测试数据，这里假设：
    # l1 为 [1, n] 内的数，r 为 [l1, n] 内的数
    # 可根据需要修改测试数据生成策略
    if n < 1:
        return

    # 简单示例：取 l1 = 1, r = n
    l1 = 1
    r = max(l1, n)

    if l1 == r:
        result = 0

    else:
        if (r & (r - 1)) == 0:
            result = r ^ (r - 1)

        else:
            x = l1 ^ r
            p1 = 1
            while p1 <= x:
                p1 *= 2
            result = p1 - 1

    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：n 可根据需要修改
    main(10)
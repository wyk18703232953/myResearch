def main(n):
    """
    n: 测试规模，用作 q 的大小。
    自动生成 q 组测试数据 (n, m, k)，并执行原逻辑。
    """
    # 这里用 n 作为 q，即生成 q = n 组测试
    q = n

    # 简单构造一组多样化的 (n, m, k) 测试数据
    # 规则示例（可根据需要调整）：
    #   a: 在 1..2n 范围变化
    #   b: 在 1..2n 范围变化
    #   k: 在 max(a, b)..max(a, b)+3 范围变化
    for i in range(1, q + 1):
        a = i
        b = (2 * i) % (2 * n + 1)
        if b == 0:
            b = 1
        k = max(a, b) + (i % 4)

        # 以下是原逻辑
        if a > k or b > k:
            # print(-1)
            pass
        elif (a - b) % 2:
            # print(k - 1)
            pass
        elif (a - k) % 2:
            # print(k - 2)
            pass

        else:
            # print(k)
            pass
if __name__ == '__main__':
    # 示例：以 n=10 作为规模运行
    main(10)
def main(n):
    """
    根据规模 n 生成测试数据 (a, b, c, n)，并输出结果。
    原逻辑：
        a, b, c, n = map(int, input().split())
        if a + b - c > n - 1 or min(a, b) < c:
            print(-1)
        else:
            print(n - (a + b - c))
    这里我们用给定的 n 生成 a, b, c。
    """

    # 生成测试数据：
    # 尝试生成一个满足条件的用例：
    # 令 c = n // 3，a = c + 1, b = c + 2，保证 min(a,b) >= c
    # 然后根据是否越界再做简单调整。
    if n <= 2:
        # 对很小的 n 做特殊处理，构造一个小用例
        a, b, c = 1, 1, 0
    else:
        c = n // 3
        a = c + 1
        b = c + 2
        # 如果 a + b - c 过大，则压缩一下
        if a + b - c > n - 1:
            # 简单缩小 a,b
            a = max(1, n // 4)
            b = max(1, n // 4 + 1)
            c = min(a, b)

    # 应用原始逻辑
    if a + b - c > n - 1 or min(a, b) < c:
        print(-1)
    else:
        print(n - (a + b - c))


if __name__ == "__main__":
    # 示例：调用 main，规模自选
    main(10)
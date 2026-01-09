def main(n):
    # 可以根据需要调整测试数据生成规则
    # 这里设定 k 与 n 同阶，例如 k = n
    k = n

    if n == 1:
        # print(0)
        pass
        return

    if (k * k - k) // 2 + 1 < n:
        # print(-1)
        pass
        return

    g, b = 0, k // 2
    while b != 0:
        while (
            g + b <= k
            and (k * k - k) // 2 + 1 - ((g + b) ** 2 - (g + b)) // 2 >= n
        ):
            g += b
        b //= 2

    # print(k - g)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
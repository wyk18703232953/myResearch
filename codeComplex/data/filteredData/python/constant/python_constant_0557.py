def main(n):
    """
    n: 规模参数，用于生成测试数据。
    这里约定：
    - n 为原代码中的 n
    - m, k, l 由 n 派生生成测试数据
    """
    # 根据 n 生成测试数据（示例策略，可根据需要调整）
    # 确保 m > 0，且不会为零
    m = max(1, n // 3)
    k = n * 2
    l = n

    c = (k + l) // m
    if (k + l) % m != 0:
        c += 1

    if n >= m * c:
        print(c)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main，使用某个规模 n
    main(10)
def main(n: int):
    """
    n 作为规模参数，这里用来生成测试数据：
    - k: 固定为 3
    - s: 固定为 5
    - p: 固定为 2
    并将原逻辑封装在 main 中。
    你可以根据需要自行修改 k, s, p 的生成方式。
    """
    # 根据规模 n 生成一组测试数据（可按需修改生成策略）
    k = 3
    s = 5
    p = 2

    # 原始逻辑
    result = int((int((n + s - 1) / s) * k + p - 1) / p)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，传入规模 n
    main(10)
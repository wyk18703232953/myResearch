def main(n: int):
    """
    根据规模 n 生成测试数据 a, b，然后执行原逻辑并打印结果。
    这里示例性地生成：
    a = n
    b = max(1, n // 2)
    可按需要自行调整生成方式。
    """
    a = n
    b = max(1, n // 2)

    c = 2 * (a - 1) - b * (b - 1)
    if c > 0:
        print(-1)
    else:
        d = int((1 + (1 - 4 * c) ** 0.5) / 2)
        if d * (d - 1) + c > 0:
            d -= 1
        print(b - d)


if __name__ == "__main__":
    # 示例：以 n=10 运行
    main(10)
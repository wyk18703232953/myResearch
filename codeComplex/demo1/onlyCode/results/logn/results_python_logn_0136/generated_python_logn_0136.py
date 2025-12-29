def main(n):
    # 这里假设 k 与 n 有关，用于生成测试数据
    # 可按需要调整策略，例如：k = n // 2，或 k = n，或其他关系
    k = max(1, n // 2)

    m = 2 * (n - 1) - k * (k - 1)

    if m > 0:
        print(-1)
    else:
        x = int((1 + (1 - 4 * m) ** 0.5) / 2)
        if x * (x - 1) + m > 0:
            x -= 1
        print(k - x)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
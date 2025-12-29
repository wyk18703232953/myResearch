def main(n):
    # 根据规模 n 生成测试数据：
    # 这里生成 k，使得 1 <= k <= n，示例选择 k = n // 2 + 1
    k = n // 2 + 1
    if k > n:
        k = n

    m = 2 * (n - 1) - k * (k - 1)

    if m > 0:
        print(-1)
    else:
        x = int((1 + (1 - 4 * m) ** 0.5) / 2)
        if x * (x - 1) + m > 0:
            x -= 1
        print(k - x)


# 示例调用
if __name__ == "__main__":
    main(10)
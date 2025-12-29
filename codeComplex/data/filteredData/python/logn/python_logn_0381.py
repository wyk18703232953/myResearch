def main(n):
    M = 1000000007

    # 根据 n 生成测试数据：
    # 原程序需要 n, k，这里固定用一个相对简单的 k 生成方式，
    # 例如令 k = n，保持规模随 n 变化。
    k = n

    if n == 0:
        print(0)
        return

    ans = 2 * n - 1
    x = pow(2, k, M)
    print((((ans * x) % M) + 1) % M)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
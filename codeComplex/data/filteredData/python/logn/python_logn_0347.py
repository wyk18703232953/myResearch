def main(n):
    """
    n 为规模参数，这里用来生成测试数据：
    比如：
      x = n
      k = n 的二进制位数（或简单取 k=n，这里给出一种可随 n 变化的方案）
    """
    md = 1000000007

    # 生成测试数据（示例方案，可根据需要调整）
    x = n
    # 使 k 随 n 增长，这里简单取 k = n
    k = n

    if x > 0:
        ans = (pow(2, k + 1, md) * x - pow(2, k, md) + 1) % md
    else:
        ans = 0

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
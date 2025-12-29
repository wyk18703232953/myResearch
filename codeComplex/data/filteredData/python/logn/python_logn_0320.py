def main(n):
    # 生成测试数据：n 为给定规模，k 这里示例设为 n 的平方
    k = n * n

    m = 1000000007
    z = pow(2, k, m)

    ans = (((2 * z) * (n % m)) % m - (z - 1)) % m
    if n == 0:
        print(0)
    else:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
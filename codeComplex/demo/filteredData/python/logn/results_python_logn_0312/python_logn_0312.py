mod = 10 ** 9 + 7

def pow1(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n

    else:
        if k % 2 == 0:
            a = pow1(n, k // 2) % mod
            return a * a % mod

        else:
            return pow1(n, k - 1) % mod * n % mod

def main(n):
    # 根据规模 n 生成测试数据：
    # 原代码中有 n, k 两个参数，这里用 n 作为原 n，
    # 并生成一个与 n 同规模的 k（例如 k = n）。
    k = n

    if n == 0:
        result = 0

    else:
        x = pow1(2, k + 1) % mod
        result = ((n * x - pow1(2, k) + 1)) % mod

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
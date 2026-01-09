def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res


def main(n):
    """
    n: 用作规模参数，这里用来生成测试数据 x[0], x[1]
       例如：x[0] = n, x[1] = n + 1
    """
    p = 1000000007

    # 根据 n 生成测试数据，这里示例为：
    # x[0] = n, x[1] = n + 1
    x0 = n
    x1 = n + 1
    x = [x0, x1]

    y = power(2, x[1], p)

    if x[0] > 0:
        ans = (2 * y * x[0]) % p - (y - 1) % p

    else:
        ans = 0

    ans %= p
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)
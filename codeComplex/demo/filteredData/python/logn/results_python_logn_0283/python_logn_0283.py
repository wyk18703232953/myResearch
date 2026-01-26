def bin_pow(num, _pow, module):
    if _pow == 0:
        return 1
    if _pow == 1:
        return num % module
    if _pow % 2 == 1:
        return num * bin_pow(num, _pow - 1, module) % module
    res = bin_pow(num, _pow // 2, module)
    return (res * res) % module


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单取 x = n, k = n，可根据需要自行调整生成策略
    x = n
    k = n

    if x == 0:
        return 0

    mod = 10**9 + 7
    __power = bin_pow(2, k, mod)
    return (x * __power * 2 + 1 - __power) % mod


if __name__ == "__main__":
    # 示例：调用 main(10)
    result = main(10)
    # print(result)
    pass
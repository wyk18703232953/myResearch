mod = 1000000007

def main(n):
    """
    n 作为规模参数，用来生成测试数据 (x, k)：
    这里示例：x = n，k = n // 2
    可根据需要修改生成规则。
    """
    x = n
    k = n // 2

    if x == 0:
        return 0
    else:
        return (x * pow(2, k + 1, mod) - pow(2, k, mod) + 1) % mod


if __name__ == "__main__":
    # 示例：调用 main(10)
    print(main(10))
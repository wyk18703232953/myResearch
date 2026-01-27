from math import sqrt


def main(n):
    # 根据 n 生成测试数据，这里示例为：令 k = n
    k = n

    t = int(sqrt(8 * n + 8 * k + 9) + 0.0001)
    m = (t - 3) // 2
    result = n - m
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
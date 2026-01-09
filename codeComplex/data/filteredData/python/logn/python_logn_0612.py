def main(n):
    from math import sqrt
    # 映射含义：
    # 使用 n 作为原程序中的 n
    # 使用 k = n^2 作为规模相关的第二个参数
    orig_n = n
    k = n * n

    a = 1
    b = -1 * (2 * orig_n + 3)
    c = orig_n * (orig_n + 1) - 2 * k

    res = (-1 * b) - sqrt((b * b) - 4 * a * c)
    res = res / 2
    res = int(res)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)
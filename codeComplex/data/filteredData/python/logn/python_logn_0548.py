def main(n: int):
    """
    原程序功能：给定整数 k，输出“无限拼接的正整数序列 123456789101112...”
    中的第 k 个字符（1-based）。

    这里用 n 作为规模参数，我们令 k = n。
    """
    k = n

    d = [0]
    for i in range(1, 12):
        d.append((10 ** i - 10 ** (i - 1)) * i + d[i - 1])

    for i in range(1, len(d)):
        if k <= d[i]:
            f = d[i - 1]
            f1 = 10 ** (i - 1)
            # 找到第 k 个字符对应的数字，并取出其中相应的位
            # print(str(((k - f - 1) // i) + f1)[(k - f - 1) % i])
            pass
            return


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的值进行测试
    main(1000)
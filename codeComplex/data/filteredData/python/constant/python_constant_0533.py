def main(n):
    # 解释：原程序读取两个整数 n, m，并输出 ceil(m / n)
    # 在这里我们将输入规模参数命名为 size，用于生成确定性的 n, m
    size = max(1, n)

    # 生成确定性输入：
    # 让原程序的 n = size
    # 让原程序的 m = size^2 + size
    div = size
    m = size * size + size

    if m % div != 0:
        result = m // div + 1

    else:
        result = m // div

    return result


if __name__ == "__main__":
    # print(main(10))
    pass
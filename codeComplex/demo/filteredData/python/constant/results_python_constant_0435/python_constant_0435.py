def main(n):
    # 原程序的输入结构为两个整数 n, k
    # 这里将 n 视为问题规模，并构造确定性的 k
    # 例如令 k = n // 2 + 1，避免为 0
    input_n = n
    k = n // 2 + 1

    if k % 2 == 1:
        mink = (k + 1) // 2

    else:
        mink = k // 2 + 1
    result = max(0, min(k - 1, input_n) - mink + 1)
    return result


if __name__ == "__main__":
    # 示例调用
    for size in [1, 2, 5, 10, 100]:
        # print(size, main(size))
        pass
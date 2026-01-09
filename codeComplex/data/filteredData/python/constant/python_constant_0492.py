def main(n):
    # 根据 n 构造确定性输入规模
    # 映射为 a, b 两个整数
    # 确保 a > 0
    a = max(1, n)
    b = n * n + 3 * n + 1

    result = (b + a - 1) // a
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
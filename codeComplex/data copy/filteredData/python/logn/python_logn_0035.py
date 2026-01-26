def main(n):
    # 将 n 映射为两个整数 a, b，用于保持可扩展的输入规模
    # 这里选择构造方式完全确定性且随 n 增大而增大
    a = n
    b = (n * 2) + 1

    s = a ^ b
    cnt = 0
    while s != 0:
        s = int(s / 2)
        cnt = cnt + 1
    result = (2 ** cnt) - 1
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
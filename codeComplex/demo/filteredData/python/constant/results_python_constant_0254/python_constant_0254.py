def main(n):
    import math

    # 在原程序中有两行输入：n 和 m
    # 这里将 n 映射为原程序的第一个整数 n0，第二个整数 m0 为一个随 n 规模增长的确定性值
    n0 = n
    m0 = n * n + 1  # 确定性构造，使输入规模随 n 增长

    if n0 <= math.log2(m0):
        result = m0 % (2 ** n0)

    else:
        result = m0

    # print(result)
    pass
if __name__ == "__main__":
    main(10)
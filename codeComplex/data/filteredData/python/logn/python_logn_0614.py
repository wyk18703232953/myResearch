def main(n):
    import math

    # 映射：原程序中有两个输入 n, k
    # 这里设：
    #   原_n = n
    #   原_k = n // 2  （确定性构造，保证规模随 n 增长）
    orig_n = n
    k = n // 2

    temp = 2 * (k + orig_n)
    m = (-3 + math.sqrt(9 + 4 * temp)) / 2
    result = int(orig_n - m)

    # 保持原程序的输出行为：打印一个整数
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 以进行规模化实验
    main(10)
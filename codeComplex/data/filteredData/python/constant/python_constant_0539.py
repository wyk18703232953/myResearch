def main(n):
    # 在原程序中，n 是输入的第一个参数，S 是第二个参数
    # 这里将实验规模参数 n 作为原始 n 的值
    original_n = n
    # 确定性生成 S，与 n 相关联
    S = n * (n + 1)
    result = (S + original_n - 1) // original_n
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
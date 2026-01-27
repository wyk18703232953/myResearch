def main(n):
    # 在原程序中：
    # 第一行输入为 n
    # 第二行输入为 m
    # 这里将实验规模参数 n 映射为原程序的 n
    original_n = n
    # 为保证可扩展性且与 n 有关，构造一个确定性的 m
    # 例如：m = n 的平方加上一些线性项
    m = n * n + 3 * n + 7

    if original_n <= 26:
        result = m % (2 ** original_n)

    else:
        result = m
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值做实验
    main(10)
def main(n):
    # 映射：原程序中第一个输入为 n，这里保持为参数 n
    # 原程序中第二个输入 k 由 n 确定性生成
    # 例如设定 k = n^2 + n
    k = n * n + n
    result = (k + n - 1) // n
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
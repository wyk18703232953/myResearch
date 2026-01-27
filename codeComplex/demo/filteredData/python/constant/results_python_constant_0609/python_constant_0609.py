def main(n):
    # 将 n 作为原程序中的第一个输入，将 k 设为与 n 相关的确定性值
    # 这里选择 k = n + 1，确保 k > 0 且规模与 n 同阶
    k = n + 1
    result = (-(-n * 2 // k)) + (-(-n * 5 // k)) + (-(-n * 8 // k))
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，按需修改 n 进行规模实验
    main(10)
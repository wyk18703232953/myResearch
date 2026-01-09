def main(n):
    # 映射：原程序中有两个输入 n 和 s
    # 重构后：
    #   - 使用参数 n 作为原程序的第一个输入
    #   - 生成一个确定性的 s，规模同 n，设为 s = n * (n + 1)
    original_n = n
    s = n * (n + 1)
    result = (s + original_n - 1) // original_n
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
def main(n: int):
    # 根据规模 n 生成类似结构的测试：前两行长度随 n 变化
    # 第一行：n 个 5
    for _ in range(n):
        # print(5, end="")
        pass
    # print()
    pass
    # 第二行：n-1 个 4，最后一个是 5；当 n<=0 时不输出第二行
    if n > 0:
        for _ in range(n - 1):
            # print(4, end="")
            pass
        # print(5)
        pass
if __name__ == "__main__":
    # 示例：将原来固定规模 1000 映射为 n=1000
    main(1000)
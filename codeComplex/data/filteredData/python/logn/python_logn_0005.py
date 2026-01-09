def main(n):
    # 根据 n 生成确定性输入规模
    # 映射为两个整数 a, b
    a = n
    b = (n * 2 + 3)

    # 原始逻辑
    if a == b:
        # print(0)
        pass

    else:
        x = a ^ b
        c = 1
        while x:
            x >>= 1
            c <<= 1
        # print(c - 1)
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 的值进行规模化实验
    main(10)
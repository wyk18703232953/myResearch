def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里示例：令 A, B 为与 n 相关的两个整数
    # 你可以按需求修改数据生成逻辑
    A = n
    B = n // 2

    # 原逻辑：输出 (1 << (A ^ B).bit_length()) - 1
    result = (1 << (A ^ B).bit_length()) - 1
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
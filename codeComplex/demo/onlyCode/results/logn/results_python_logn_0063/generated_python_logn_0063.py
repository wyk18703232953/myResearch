def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里简单设定 A = n, B = 2*n 作为示例数据
    A = n
    B = 2 * n

    # 原逻辑：输出 (1 << (A ^ B).bit_length()) - 1
    result = (1 << (A ^ B).bit_length()) - 1
    print(result)


if __name__ == "__main__":
    # 示例：可自行修改测试规模
    main(10)
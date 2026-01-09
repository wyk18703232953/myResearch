def main(n: int):
    # 根据规模 n 生成测试数据，这里示例为：
    # l 从 0 到 n，r 为 n，这样规模随 n 增长
    l, r = n // 2, n

    result = 2 ** ((l ^ r).bit_length()) - 1
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，实际评测时可由外部指定 n
    main(10)
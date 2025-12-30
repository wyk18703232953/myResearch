def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里简单设定 l = 0, r = n，作为一组随规模变化的测试数据
    l = 0
    r = n

    # 原始逻辑
    res = 2 ** ((l ^ r).bit_length()) - 1
    print(res)


if __name__ == "__main__":
    # 示例：可修改为任意规模 n
    main(10)
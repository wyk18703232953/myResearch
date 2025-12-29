def main(n: int):
    # 原逻辑：输出 (n * 3) // 2
    print((n * 3) // 2)


if __name__ == "__main__":
    # 根据规模 n 生成测试数据，这里直接使用 n 本身作为测试数据
    # 示例：测试从 1 到 5 的若干规模
    for n in range(1, 6):
        main(n)
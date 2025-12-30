def main(n: int):
    wyn = 1
    x = 4
    for _ in range(n - 1):
        wyn += x
        x += 4
    print(wyn)


if __name__ == "__main__":
    # 根据规模 n 生成测试数据，这里直接以 n 作为规模参数
    # 可按需修改为多组测试，例如 for n in range(1, 11): main(n)
    test_n = 10  # 示例规模
    main(test_n)
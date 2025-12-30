def main(n: int) -> None:
    # 根据 n 生成测试数据，这里简单使用 n 本身作为测试值
    x = n
    print(["YES", "NO"][all(x % i for i in [4, 7, 47, 744, 477])])


if __name__ == "__main__":
    # 示例：可自行修改 n 测试不同规模
    main(100)
def main(n: int):
    # 根据 n 生成测试数据（仅示例：这里不做复杂生成，直接使用 n）
    # 如果需要更复杂的测试数据，可在此处生成并使用
    for i in range(n // 3):
        # print(2 * i, 0)
        pass
        # print(2 * i + 1, 0)
        pass
        # print(2 * i + 1, 3)
        pass
    for i in range(n % 3):
        # print(2 * (n // 3) + i, 0)
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的测试规模
    main(10)
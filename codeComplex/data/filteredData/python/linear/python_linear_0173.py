def main(n: int):
    # 根据 n 生成测试数据（示例：这里只是展示生成，真实逻辑视需求调整）
    # 例如：生成一个长度为 n 的数组 [1, 2, ..., n]
    test_data = list(range(1, n + 1))

    # 原逻辑开始
    if n >= 6:
        for i in range(2, n - 1):
            print(1, i)
        for i in range(n - 1, n + 1):
            print(2, i)
    else:
        print(-1)
    for i in range(2, n + 1):
        print(1, i)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行测试
    main(10)
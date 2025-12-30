def main(n: int):
    # 这里根据 n 生成测试数据，如果需要可以调整为固定或随机生成方式
    # 当前逻辑是直接使用传入的 n 作为规模

    if n <= 5:
        print(-1)
        for i in range(2, n + 1):
            print(1, i)
        return

    print(1, 2)
    print(2, 3)
    print(2, 4)
    for i in range(5, n + 1):
        print(3, i)

    for i in range(2, n + 1):
        print(1, i)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)
def main(n):
    if n < 6:
        print(-1)
    else:
        # 固定的前几条边
        print(1, 2)
        print(1, 3)
        print(1, 4)
        # 从 5 到 n 连到 2
        for i in range(5, n + 1):
            print(2, i)
    # 线性链 1-2-3-...-n
    for i in range(1, n):
        print(i, i + 1)


if __name__ == "__main__":
    # 示例：生成规模为 10 的测试数据
    main(10)
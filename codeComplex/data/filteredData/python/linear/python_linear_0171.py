def main(n: int):
    # 这里根据规模 n 生成测试数据，本题只需要 n 本身即可
    # 如需扩展，可在此处生成更多与 n 相关的测试数据

    if n == 2 or n == 3 or n == 4 or n == 5:
        print(-1)
    else:
        print(1, 2)
        print(2, 3)
        print(2, 4)
        for i in range(5, n + 1):
            print(4, i)

    for i in range(2, n + 1):
        print(1, i)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可修改为任意正整数 n
    main(10)
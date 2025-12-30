def main(n):
    # 根据规模 n 生成测试数据，这里直接使用 n 作为原始输入
    x = n

    # 原逻辑：读入 n 后先加 1
    x += 1

    # 输出逻辑
    if x % 2 == 0 or x == 1:
        print(x // 2)
    else:
        print(x)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改或在外部调用 main(n)
    main(10)
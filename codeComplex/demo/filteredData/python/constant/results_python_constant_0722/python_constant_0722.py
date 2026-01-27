def main(n: int):
    # 根据规模 n 生成测试数据：这里直接使用 n 作为原程序中的 n
    # 若需要批量测试，可在此根据 n 构造多个测试值。
    i = 0
    x = n  # 使用 x 作为工作变量，模拟原代码中的 n

    while True:
        delta = 9 * (10 ** i) * (i + 1)
        if x - delta <= 0:
            break
        x -= delta
        i += 1

    a = x // (i + 1)
    b = x % (i + 1)

    if b != 0:
        # print(str(10 ** i + a)[b - 1])
        pass

    else:
        # print(str(10 ** i + a - 1)[-1])
        pass
if __name__ == "__main__":
    # 示例：调用 main(1000)，可按需修改测试规模
    main(1000)
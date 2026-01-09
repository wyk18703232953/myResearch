def main(n: int):
    total = 0
    # 原程序逻辑：对给定 n 进行计算
    for i in range(2, n + 1):
        j = 2
        while j * i <= n:
            total += i
            j += 1
    # print(4 * total)
    pass
if __name__ == "__main__":
    # 根据 n 生成测试数据：这里直接给定一个示例规模 n
    # 如果需要多组测试，可在此处循环调用 main 不同的 n
    example_n = 10
    main(example_n)
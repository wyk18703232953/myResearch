def main(n: int):
    # 根据规模 n 生成测试数据，这里简单地直接使用 n 作为测试值
    # 如果需要批量测试，可以自行在外部循环调用 main 不同的 n
    x = n

    # 原逻辑：输出 n//2 + 1
    result = x // 2 + 1
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
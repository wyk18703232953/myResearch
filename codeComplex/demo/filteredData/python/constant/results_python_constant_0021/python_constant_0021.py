def main(n: int):
    # 根据规模 n 生成测试数据，这里直接将 n 作为测试数据
    # 若需批量测试，可自行在外部循环调用 main 不同的 n
    result = 3 * (n // 2)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：使用规模 n=10 进行一次测试
    main(10)
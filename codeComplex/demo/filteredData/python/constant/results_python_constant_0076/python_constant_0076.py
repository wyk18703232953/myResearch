def main(n: int):
    # 这里根据 n 生成一个测试数据，本题逻辑只依赖单个整数
    # 若你希望一次性测试多个规模，可自行在外部循环调用 main
    test_n = n

    res = test_n if test_n < 3 else (
        (test_n - 1) * (
            test_n * (test_n - 2)
            if test_n & 1
            else (test_n - 3) * (test_n if test_n % 3 else test_n - 2)
        )
    )
    # print(res)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)
def main(n: int):
    # 这里根据规模 n 生成测试数据，本题只有一个整数输入，直接用 n 即可
    x = n

    # 原始逻辑
    if x == 0:
        result = 0

    else:
        result = x // 2 + 1 if x % 2 != 0 else x + 1

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：可以在这里调用 main 进行简单测试
    # 例如规模为 10：
    main(10)
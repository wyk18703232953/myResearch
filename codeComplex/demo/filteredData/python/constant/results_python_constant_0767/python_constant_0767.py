def main(n):
    # 依据规模 n 生成测试数据，这里示例为：
    # 令 k = n，可以按需修改生成规则
    k = n

    b = (9 + 8 * (n + k)) ** 0.5
    a = int(b)
    result = n - (a - 3) // 2
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
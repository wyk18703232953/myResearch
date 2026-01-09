def main(n: int):
    # 生成测试数据：原程序中 n 来自输入，这里直接使用参数 n
    answer = 0
    for i in range(1, 2 * n - 2, 2):
        answer += i
    result = answer * 2 + 2 * n - 1
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：可在此处修改 n 测试不同规模
    main(10)
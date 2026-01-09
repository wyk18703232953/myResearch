def main(n: int):
    # 原逻辑：对于给定的 n，计算表达式并输出
    x = 2 * n - 1
    ans = x
    x -= 2
    curr = 0
    while x > 0:
        curr += x
        x -= 2
    # print(ans + 2 * curr)
    pass
if __name__ == "__main__":
    # 根据 n 生成测试数据，这里简单地固定一个规模示例
    test_n = 5
    main(test_n)
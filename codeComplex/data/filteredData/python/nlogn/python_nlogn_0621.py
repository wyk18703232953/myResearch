def main(n: int):
    ans = 0
    # 原逻辑部分
    for i in range(2, n + 1):
        for j in range(2 * i, n + 1, i):
            ans += 4 * (j // i)
    # print(ans)
    pass
if __name__ == "__main__":
    # 根据规模 n 生成测试数据：这里直接使用 n 作为规模参数
    # 可根据需要修改测试用的 n 值
    test_n = 100  # 示例：测试规模为 100
    main(test_n)
def main(n: int):
    ans = []
    m = int(n ** 0.5)
    x = n
    while x - m > 0:
        for i in range(1, m + 1):
            ans.append(x - m + i)
        x -= m
    for i in range(1, x + 1):
        ans.append(i)
    print(*ans)


if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据并运行
    test_n = 100  # 可以在这里修改测试规模
    main(test_n)
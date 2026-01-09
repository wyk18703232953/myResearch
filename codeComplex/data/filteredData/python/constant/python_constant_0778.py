def main(n):
    # 预计算所有可能的 2*i^2 和 4*i^2
    ok = set()
    for i in range(114514):
        x = i * i
        ok.add(2 * x)
        ok.add(4 * x)

    # 根据规模 n 生成测试数据：
    # 前一半生成一定在集合中的数，后一半生成一定不在集合中的数
    tests = []
    half = n // 2

    # 生成在 ok 中的数
    i = 0
    while len(tests) < half and i < 114514:
        x = i * i
        tests.append(2 * x)
        if len(tests) < half:
            tests.append(4 * x)
        i += 1
    tests = tests[:half]

    # 生成不在 ok 中的数：从 1 开始依次找非 ok 整数
    x = 1
    while len(tests) < n:
        if x not in ok:
            tests.append(x)
        x += 1

    # 模拟原程序输出
    for val in tests:
        ans = "YES" if val in ok else "NO"
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)
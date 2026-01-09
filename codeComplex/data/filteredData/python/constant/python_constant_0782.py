def main(n):
    # 预处理平方和 2*平方
    hashi = {}
    limit = 10**5
    for i in range(1, limit):
        hashi[i * i] = 1
        hashi[2 * i * i] = 1

    # 生成测试数据：
    # 使用 n 作为要测试的数值本身（可以根据需要自行调整生成规则）
    t = 1          # 测试组数
    test_values = [n]

    # 模拟原逻辑
    results = []
    for value in test_values:
        if value % 2:
            results.append("NO")
            continue
        z = value // 2
        if z in hashi:
            results.append("YES")

        else:
            results.append("NO")

    # 输出结果
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    # 示例：调用 main( n )，可按需修改 n
    main(10)
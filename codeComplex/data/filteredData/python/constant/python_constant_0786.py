def main(n):
    # 生成测试数据：这里将 n 作为单个测试用例的值
    t = 1
    results = []
    for _ in range(t):
        a = round((n / 2) ** 0.5)
        b = round((n / 4) ** 0.5)
        if 2 * a * a == n or 4 * b * b == n:
            results.append("YES")
        else:
            results.append("NO")
    # 输出结果
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例：调用 main(8)
    main(8)
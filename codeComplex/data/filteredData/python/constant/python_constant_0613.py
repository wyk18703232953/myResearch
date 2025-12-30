def f(n: int) -> int:
    t = (n + 1) // 2
    return t if n % 2 == 0 else -t


def main(n: int):
    # 生成测试数据：
    # 这里生成 n 组 [le, rg] 区间，示例策略：
    # le = 1, 2, ..., n
    # rg = le + n - 1
    # 可根据需要调整测试数据生成策略。
    results = []
    for i in range(1, n + 1):
        le = i
        rg = i + n - 1
        res = f(rg) - f(le - 1)
        results.append(res)

    # 输出结果
    for val in results:
        print(val)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
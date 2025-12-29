import random

def main(n: int):
    """
    n: 测试数据组数
    根据 n 随机生成 n 组 (a, b)，并对每组执行原逻辑，返回结果列表。
    """
    results = []

    # 生成 n 组测试数据并执行逻辑
    for _ in range(n):
        # 可根据需要调整数据规模，这里给出一个示例范围
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)

        x, y = a, b
        ans = 0
        while x and y:
            x, y = min(x, y), max(x, y)
            ans, y = ans + y // x, y % x

        results.append((a, b, ans))

    # 输出结果：每行 "a b ans"
    for a, b, ans in results:
        print(a, b, ans)


if __name__ == "__main__":
    # 示例：运行 5 组随机测试
    main(5)
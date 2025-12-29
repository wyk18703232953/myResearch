import random

def main(n):
    """
    n: 生成 n 组 (a, b) 测试数据并分别计算结果
    输出每组的 count 值（对应原程序中每次循环的输出）
    """
    results = []
    for _ in range(n):
        # 生成测试数据：两个正整数 a, b
        # 可根据需要调整数据规模
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)

        # 对应原代码中：n, m = sorted(map(int, input().split()))
        x, y = sorted((a, b))
        count = 0
        while x > 0:
            count += y // x
            y = y % x
            x, y = sorted((x, y))
        results.append(count)

    # 按原程序风格逐行输出
    for val in results:
        print(val)


if __name__ == "__main__":
    # 示例：生成 5 组测试数据并运行
    main(5)
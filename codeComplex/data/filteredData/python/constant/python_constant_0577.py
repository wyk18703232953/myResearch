import random

def solve(x, y, n):
    return "White" if (x - 1 + y - 1) <= (n - x + n - y) else "Black"


def main(n):
    # 根据规模 n 生成测试数据
    # 生成一个位于 [1, n] 范围内的随机坐标 (x, y)
    x = random.randint(1, n)
    y = random.randint(1, n)

    result = solve(x, y, n)
    print(f"n={n}, x={x}, y={y}, result={result}")


if __name__ == "__main__":
    # 示例：可以在此处指定想要测试的 n
    main(8)
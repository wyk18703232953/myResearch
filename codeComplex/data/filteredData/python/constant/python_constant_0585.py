import random

def main(n: int):
    # 生成测试数据：x, y 在 [1, n] 范围内
    x = random.randint(1, n)
    y = random.randint(1, n)

    def d(a, b):
        return a + b

    if d(x - 1, y - 1) <= d(n - x, n - y):
        print("White")
    else:
        print("Black")


if __name__ == "__main__":
    # 示例：可修改 n 测试不同规模
    main(10)
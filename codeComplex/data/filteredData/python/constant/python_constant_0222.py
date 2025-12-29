import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设 n 控制数据的大致上界
    if n <= 0:
        n = 1

    # 生成 h, b
    h = random.randint(0, n)
    b = random.randint(0, n)

    # 生成 x, y, z
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)

    # 原逻辑
    result = max(0, 2 * x + y - h) + max(0, 3 * z + y - b)
    print(result)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
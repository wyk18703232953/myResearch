import random

def main(n: int):
    # 生成测试数据：
    # A, B, x, y, z 的取值范围可以根据需要调整，这里示例使用 [-n, n]
    A = random.randint(-n, n)
    B = random.randint(-n, n)
    x = random.randint(-n, n)
    y = random.randint(-n, n)
    z = random.randint(-n, n)

    A1 = 2 * x + y - A
    B1 = 3 * z + y - B
    final = 0
    if A1 > 0:
        final += A1
    if B1 > 0:
        final += B1

    print(final)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
import random

def main(n):
    # 1. 生成测试数据
    # 这里将 n 用作数值规模上界，用于随机生成 A, B, x, y, z
    # 可根据需要调整数据生成规则
    max_val = max(1, n)

    A = random.randint(0, max_val)
    B = random.randint(0, max_val)
    x = random.randint(0, max_val)
    y = random.randint(0, max_val)
    z = random.randint(0, max_val)

    # 2. 原始逻辑
    y1 = (x * 2) + y
    b1 = y + (3 * z)

    summ = 0
    if y1 > A:
        summ += y1 - A
    if b1 > B:
        summ += b1 - B

    print(summ)


if __name__ == "__main__":
    # 默认给一个规模，例如 10
    main(10)
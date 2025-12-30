import random

def main(n: int):
    # n 用作生成数据的规模参数，这里不直接影响变量数量，仅用于控制随机数范围
    # 根据 n 生成测试数据：
    # x, y, z 在 [1, n] 范围内
    # t1, t2, t3 在 [1, n] 范围内
    if n <= 0:
        raise ValueError("n 必须为正整数")

    x = random.randint(1, n)
    y = random.randint(1, n)
    z = random.randint(1, n)
    t1 = random.randint(1, n)
    t2 = random.randint(1, n)
    t3 = random.randint(1, n)

    tp = abs(x - y) * t1
    pt = (abs(x - y) + abs(x - z)) * t2 + t3 + t3 + t3

    if tp >= pt:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：规模 n = 100
    main(100)
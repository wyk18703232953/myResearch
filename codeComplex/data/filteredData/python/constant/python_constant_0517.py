import random

def main(n):
    # n 作为规模参数，这里我们用它来控制随机数范围
    # 例如：坐标范围在 [-n, n]，时间系数范围在 [1, n]
    x = random.randint(-n, n)
    y = random.randint(-n, n)
    z = random.randint(-n, n)
    t1 = random.randint(1, n)
    t2 = random.randint(1, n)
    t3 = random.randint(1, n)

    stair = t1 * abs(x - y)
    lift = t2 * (abs(z - x) + abs(x - y)) + t3 * 3
    print("YES" if lift <= stair else "NO")


if __name__ == "__main__":
    # 示例：用 n = 10 运行一组测试
    main(10)
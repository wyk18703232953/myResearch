import random

def main(n: int):
    # 生成测试数据：
    # n 用作生成数值的范围上界（至少为 1）
    if n <= 0:
        n = 1

    # 位置坐标 x, y, z ∈ [0, n]
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)

    # 时间参数 t1, t2, t3 ∈ [1, n+1]，避免为 0
    t1 = random.randint(1, n + 1)
    t2 = random.randint(1, n + 1)
    t3 = random.randint(1, n + 1)

    elevator = t2 * (abs(x - y) + abs(z - x)) + 3 * t3
    stairs = t1 * abs(x - y)

    if elevator > stairs:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    # 示例：规模 n = 10，可根据需要修改或在外部调用 main(n)
    main(10)
def main(n):
    # 生成测试数据
    # n: 房屋数量
    # 生成 N 和 T
    N = n
    T = 5  # 可以根据需要调整，或设计成与 n 相关

    import random

    # 随机生成 N 个房屋 (位置, 宽度)
    # 位置在 [0, 10*n] 范围内，宽度在 [1, 10] 范围内
    houses = []
    for _ in range(N):
        a = random.randint(0, 10 * n)
        x = random.randint(1, 10)
        houses.append((a, x))

    # 按原逻辑处理
    houses.sort()

    count = 2  # borders left and right

    for (a, x), (b, y) in zip(houses, houses[1:]):
        gap = b - a - (x / 2 + y / 2)
        if gap > T:
            count += 2
        elif gap == T:
            count += 1

    print(count)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)
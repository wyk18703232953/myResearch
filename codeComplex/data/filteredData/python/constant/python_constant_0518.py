import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里假设：坐标和时间系数在一定范围内随机生成
    # n 不直接参与逻辑，只用于控制数据“规模”或范围
    # 可根据需要自行调整生成规则
    max_coord = max(10, n * 10)
    max_time  = max(10, n * 2)

    x = random.randint(-max_coord, max_coord)
    y = random.randint(-max_coord, max_coord)
    z = random.randint(-max_coord, max_coord)
    t1 = random.randint(1, max_time)
    t2 = random.randint(1, max_time)
    t3 = random.randint(1, max_time)

    if abs(z - x) * t2 + 3 * t3 + abs(x - y) * t2 <= abs(x - y) * t1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：以 n=10 运行
    main(10)
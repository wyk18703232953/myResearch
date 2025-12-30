import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # 这里 n 不直接参与逻辑运算，仅用于控制随机数范围
    limit = max(1, n)

    # 随机生成三点坐标 (x1, y1), (x2, y2), (x3, y3)
    x1, y1 = random.randint(-limit, limit), random.randint(-limit, limit)
    x2, y2 = random.randint(-limit, limit), random.randint(-limit, limit)
    x3, y3 = random.randint(-limit, limit), random.randint(-limit, limit)

    # 原始逻辑
    if (y2 - y1) * (y3 - y1) > 0 and (x2 - x1) * (x3 - x1) > 0 and x1 + y1 != x3 + y3:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：可修改为任意规模 n
    main(10)
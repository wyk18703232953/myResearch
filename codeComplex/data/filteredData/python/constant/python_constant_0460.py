import random
import math


def main(n: int):
    # 生成测试数据：
    # n: 任意规模参数，这里仅用于控制生成坐标的范围
    # 生成 (x, y), (bx, by), (cx, cy)
    limit = max(1, n)
    x = random.randint(-limit, limit)
    y = random.randint(-limit, limit)
    bx = random.randint(-limit, limit)
    by = random.randint(-limit, limit)
    cx = random.randint(-limit, limit)
    cy = random.randint(-limit, limit)

    # 原始逻辑
    x1, y1 = x - bx, y - by
    x2, y2 = x - cx, y - cy

    if abs(x2) == abs(y2):
        print('NO')
        return
    if math.copysign(x2, x1) != x2:
        print('NO')
        return
    if math.copysign(y2, y1) != y2:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)
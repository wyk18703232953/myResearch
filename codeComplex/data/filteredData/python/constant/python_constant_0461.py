import random

def main(n):
    # 生成测试数据：n 组 (ax, ay, bx, by, cx, cy)
    # 这里假设坐标范围在 [-10^9, 10^9] 之间，可按需要调整
    COORD_MIN, COORD_MAX = -10**9, 10**9

    random.seed(0)  # 固定种子，保证复现性
    for _ in range(n):
        ax = random.randint(COORD_MIN, COORD_MAX)
        ay = random.randint(COORD_MIN, COORD_MAX)
        bx = random.randint(COORD_MIN, COORD_MAX)
        by = random.randint(COORD_MIN, COORD_MAX)
        cx = random.randint(COORD_MIN, COORD_MAX)
        cy = random.randint(COORD_MIN, COORD_MAX)

        if (ax - bx) * (ax - cx) > 0 and (ay - by) * (ay - cy) > 0:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    # 示例：运行 5 组测试
    main(5)
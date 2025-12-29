import math
import random

def main(n):
    # 生成测试数据：半径 r 和 n 个圆心 x 坐标
    # 这里假设 r 为一个适中整数，x 坐标为递增随机数，便于可视化
    r = 10
    x_cord = []
    cur = 0
    for _ in range(n):
        # 相邻两个圆心的水平距离在 [0, 2r] 和 [2r, 4r] 范围内随机选择，
        # 既能产生重叠也能产生不重叠的情况
        step = random.randint(0, 4 * r)
        cur += step
        x_cord.append(cur)

    # 以下为原始逻辑，只是将 input() 替换为使用生成的测试数据
    y_cord = []
    for i, x in enumerate(x_cord):
        if len(y_cord) == 0:
            y_cord.append(r)
        else:
            y_cord.append(r)
            for j in range(i):
                diff = abs(x_cord[i] - x_cord[j])
                if diff <= 2 * r:
                    y_cord[i] = max(
                        y_cord[i],
                        math.sqrt(4 * r * r - diff ** 2) + y_cord[j]
                    )

    # 输出结果
    for y in y_cord:
        print(y, end=" ")

if __name__ == '__main__':
    # 示例：规模为 5
    main(5)
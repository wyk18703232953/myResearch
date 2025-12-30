import math
import random


def main(n):
    # 生成测试数据：固定半径 r，随机生成 n 个圆心横坐标
    r = 1
    # 为避免数值太大，横坐标在 [0, 10 * n] 内随机生成
    x = [random.randint(0, 10 * n) for _ in range(n)]

    y = [r]
    for i in range(1, n):
        _y = r
        for j in range(i):
            dx = x[i] - x[j]
            if 4 * r * r >= dx * dx:
                _y = max(_y, y[j] + math.sqrt(4 * r * r - dx * dx))
        y.append(round(_y, 6))

    print(' '.join(map(str, y)))


if __name__ == "__main__":
    # 示例：调用 main(5) 生成规模为 5 的测试数据并运行
    main(5)
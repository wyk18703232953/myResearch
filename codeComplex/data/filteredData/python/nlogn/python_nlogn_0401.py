from math import hypot
import random


def main(n: int):
    # 生成规模为 n 的测试数据：n 行 (x, y) 浮点数
    # 可根据需要修改数据分布
    data = []
    for _ in range(n):
        # 生成 [-1000, 1000] 范围内的随机浮点数
        x = random.uniform(-1000, 1000)
        y = random.uniform(-1000, 1000)
        data.append([x, y])

    # 在原程序中，读入后会在每行末尾附加其原始索引
    for i, s in enumerate(data):
        data[i] = [s[0], s[1], i]

    # 按照 |x| 排序
    data.sort(key=lambda xyi: abs(xyi[0]))

    res = ['1'] * len(data)
    x, y, _ = data.pop()
    while data:
        dx, dy, i = data.pop()
        a, b, u, v = x + dx, y + dy, x - dx, y - dy
        if hypot(a, b) < hypot(u, v):
            x, y = a, b
        else:
            x, y, res[i] = u, v, '-1'

    print(' '.join(res))


if __name__ == '__main__':
    # 示例：调用 main(10)
    main(10)
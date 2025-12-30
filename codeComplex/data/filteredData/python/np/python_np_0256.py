from itertools import permutations
import random


def main(n):
    # 生成测试数据：x1, y1, x2, y2, x3, y3 在 1..n 范围内随机取值
    # n 表示坐标的最大值规模
    if n < 1:
        n = 1
    x1, y1 = random.randint(1, n), random.randint(1, n)
    x2, y2 = random.randint(1, n), random.randint(1, n)
    x3, y3 = random.randint(1, n), random.randint(1, n)

    # 原始逻辑开始
    for x in [[x1, y1], [y1, x1]]:
        for y in [[x2, y2], [y2, x2]]:
            for z in [[x3, y3], [y3, x3]]:
                if x[1] == y[1] == z[1] and x[0] + y[0] + z[0] == x[1]:
                    print(x[1])
                    print('\n'.join(
                        ['A' * x[1] for _ in range(x[0])]
                        + ['B' * x[1] for _ in range(y[0])]
                        + ['C' * z[1] for _ in range(z[0])]
                    ))
                    return

    for per in permutations(
        [
            [[x1, y1], [y1, x1], 'A'],
            [[x2, y2], [y2, x2], 'B'],
            [[x3, y3], [y3, x3], 'C'],
        ],
        3
    ):
        for x in per[0][:-1]:
            for y in per[1][:-1]:
                for z in per[2][:-1]:
                    if x[1] == (y[1] + z[1]) and y[0] == z[0] and x[1] == x[0] + y[0]:
                        print(x[1])
                        print('\n'.join(
                            [per[0][-1] * x[1] for _ in range(x[0])]
                            + [
                                per[1][-1] * y[1] + per[2][-1] * z[1]
                                for _ in range(y[0])
                            ]
                        ))
                        return

    print(-1)


if __name__ == "__main__":
    # 示例调用：n 为规模参数
    main(10)
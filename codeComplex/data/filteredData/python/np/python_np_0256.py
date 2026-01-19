def main(n):
    # 解释输入结构：原程序需要 6 个整数 x1, y1, x2, y2, x3, y3
    # 这里用 n 生成它们，使得同一个 n 的输入数据是确定性的
    # 生成方式可以自由调整，但必须是确定性的且与 n 相关
    x1 = n
    y1 = n + 1
    x2 = n + 2
    y2 = n + 3
    x3 = n + 4
    y3 = n + 5

    # 以下是原逻辑（移除了所有输入依赖）
    from itertools import permutations

    for x in [[x1, y1], [y1, x1]]:
        for y in [[x2, y2], [y2, x2]]:
            for z in [[x3, y3], [y3, x3]]:
                if x[1] == y[1] == z[1] and x[0] + y[0] + z[0] == x[1]:
                    print(x[1])
                    print('\n'.join(
                        ['A' * x[1] for _ in range(x[0])] +
                        ['B' * x[1] for _ in range(y[0])] +
                        ['C' * z[1] for _ in range(z[0])]
                    ))
                    return

    for per in permutations(
        [
            [[x1, y1], [y1, x1], 'A'],
            [[x2, y2], [y2, x2], 'B'],
            [[x3, y3], [y3, x3], 'C']
        ],
        3
    ):
        for x in per[0][:-1]:
            for y in per[1][:-1]:
                for z in per[2][:-1]:
                    if x[1] == (y[1] + z[1]) and y[0] == z[0] and x[1] == x[0] + y[0]:
                        print(x[1])
                        print('\n'.join(
                            [per[0][-1] * x[1] for _ in range(x[0])] +
                            [per[1][-1] * y[1] + per[2][-1] * z[1] for _ in range(y[0])]
                        ))
                        return

    print(-1)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行规模化实验
    main(10)
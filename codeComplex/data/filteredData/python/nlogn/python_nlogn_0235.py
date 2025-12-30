import random
import sys


def main(n):
    # 生成测试数据：n 个点的坐标
    # 这里简单生成 [-10^9, 10^9] 范围内的随机整数坐标
    # 可按需要调整生成策略
    X = [random.randint(-10**9, 10**9) for _ in range(n)]
    Y = [random.randint(-10**9, 10**9) for _ in range(n)]

    if n <= 3:
        print('YES')
        return

    for _ in range(13):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 2)

        if a == b:
            b += 1

        x0, y0 = X[a], Y[a]
        x1, y1 = X[b], Y[b]

        dx = x1 - x0
        dy = y1 - y0
        not_on_line = []
        for c in range(n):
            if c == a or c == b:
                continue
            x2, y2 = X[c], Y[c]
            Dx = x2 - x0
            Dy = y2 - y0
            if dx * Dy - dy * Dx != 0:
                not_on_line.append(c)

        if len(not_on_line) <= 1:
            print('YES')
            return

        a = not_on_line[0]
        b = not_on_line[1]
        x0, y0 = X[a], Y[a]
        x1, y1 = X[b], Y[b]

        dx = x1 - x0
        dy = y1 - y0
        can = True
        for c in not_on_line:
            if c == a or c == b:
                continue
            x2, y2 = X[c], Y[c]
            Dx = x2 - x0
            Dy = y2 - y0
            if dx * Dy - dy * Dx != 0:
                can = False
                break
        if can:
            print('YES')
            return

    print('NO')


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)
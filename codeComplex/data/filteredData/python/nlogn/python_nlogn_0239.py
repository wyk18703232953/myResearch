import random


def main(n):
    # 生成规模为 n 的测试数据：n 个随机点，坐标范围可自行调整
    # 为了可重复性，可以固定随机种子（需要时可修改或去掉）
    random.seed(0)
    points = []
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        points.append([x, y])

    if n < 5:
        print('YES')
        return

    st = [False] * n

    def run(first, second):
        dx = first[0] - second[0]
        dy = first[1] - second[1]

        for i, p in enumerate(points):
            if st[i]:
                continue
            if dx == 0:
                if p[0] == first[0]:
                    st[i] = True
            elif dy == 0:
                if p[1] == first[1]:
                    st[i] = True
            else:
                if ((p[0] - first[0]) * dy) == (p[1] - first[1]) * dx:
                    st[i] = True

    def check(fi, si):
        for i in range(n):
            st[i] = (i == fi or i == si)

        run(points[fi], points[si])

        fi2 = None
        si2 = None
        for i in range(n - 1):
            if not st[i]:
                fi2 = i
                for j in range(i + 1, n):
                    if not st[j]:
                        si2 = j
                        break
                break
        if fi2 is None or si2 is None:
            return True

        st[fi2] = True
        st[si2] = True
        run(points[fi2], points[si2])
        return not (False in st)

    if check(0, 1) or check(0, 2) or check(1, 2):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
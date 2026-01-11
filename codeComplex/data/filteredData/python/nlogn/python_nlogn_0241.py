def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def f(v, i1, i2):
    d = [v[i2][i] - v[i1][i] for i in range(len(v[i1]))]

    res = []
    for x in v:
        d2 = [x[i] - v[i1][i] for i in range(len(v[i1]))]
        if cross(d, d2) != 0:
            res.append(x)

    return res


def main(n):
    if n <= 0:
        return "YES"

    # 生成确定性的二维点集，规模为 n
    # 点构造方式：第 i 个点为 [i, (i * 2) % max(1, n//2 + 1)]
    # 保证维度为 2，与原算法一致
    v = [[i, (i * 2) % (max(1, n // 2 + 1))] for i in range(n)]

    if n <= 4:
        return "YES"

    ok = False
    for first in range(3):
        if ok:
            break

        for second in range(first + 1, 3):
            other = f(v, first, second)

            if len(other) <= 2:
                ok = True
                break

            remainder = f(other, 0, 1)

            if not remainder:
                ok = True

    return "YES" if ok else "NO"


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 规模进行时间复杂度实验
    # print(main(10))
    pass
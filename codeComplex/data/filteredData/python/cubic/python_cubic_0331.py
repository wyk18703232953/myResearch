import random

def f(l, r, g, b, op):
    if (r == 0 and g == 0) or (r == 0 and b == 0) or (b == 0 and g == 0):
        return 0
    else:
        if op[r][g][b] != -1:
            return op[r][g][b]
        if r == 0:
            op[r][g][b] = l[1][g - 1] * l[2][b - 1] + f(l, r, g - 1, b - 1, op)
            return op[r][g][b]
        if g == 0:
            op[r][g][b] = l[0][r - 1] * l[2][b - 1] + f(l, r - 1, g, b - 1, op)
            return op[r][g][b]
        if b == 0:
            op[r][g][b] = l[0][r - 1] * l[1][g - 1] + f(l, r - 1, g - 1, b, op)
            return op[r][g][b]
        op[r][g][b] = max(
            l[1][g - 1] * l[2][b - 1] + f(l, r, g - 1, b - 1, op),
            l[0][r - 1] * l[2][b - 1] + f(l, r - 1, g, b - 1, op),
            l[0][r - 1] * l[1][g - 1] + f(l, r - 1, g - 1, b, op),
        )
        return op[r][g][b]


def main(n: int):
    """
    n 为规模参数，用来生成 r, g, b 以及三个序列的长度。
    这里简单设定 r = g = b = n。
    数据范围和分布可按需要调整。
    """
    r = g = b = n

    # 生成测试数据：三个长度分别为 r, g, b 的数组
    # 数值范围可根据需要调整，这里用 1~100 的随机整数
    l = []
    arr_r = sorted(random.randint(1, 100) for _ in range(r))
    arr_g = sorted(random.randint(1, 100) for _ in range(g))
    arr_b = sorted(random.randint(1, 100) for _ in range(b))
    l.append(arr_r)
    l.append(arr_g)
    l.append(arr_b)

    op = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    ans = f(l, r, g, b, op)
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：调用 main(3) 进行测试
    main(3)
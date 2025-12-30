import random
import sys


def solve_one_case(a):
    # 原逻辑：给定数组 a，输出四个数
    if len(set(a)) == 1:
        x = a[0]
        return [x, x, x, x]

    a.sort()
    g1 = False
    d = {}
    mx = 10001
    for v in a:
        if v not in d:
            d[v] = 1
        else:
            d[v] += 1
        if d[v] == 4:
            g1 = True
            if v < mx:
                mx = v

    if g1:
        return [mx, mx, mx, mx]
    else:
        res = []
        for k in d.keys():
            if d[k] >= 2:
                res.append(k)
        m = len(res)
        minj = 0
        # 按题解原意选择最优一对
        for j in range(m - 1):
            if (
                res[j] * res[j + 1] * (res[minj] ** 2 + res[minj + 1] ** 2)
                > res[minj] * res[minj + 1] * (res[j] ** 2 + res[j + 1] ** 2)
            ):
                minj = j
        return [res[minj], res[minj], res[minj + 1], res[minj + 1]]


def main(n):
    """
    n: 规模参数，用来生成测试数据。
       这里设定为：
       - 测试用例数量 t = max(1, min(n, 10))
       - 每个用例长度 len(a) = max(4, n)
       - 数值范围 [-n, n]，不为 0 时保证有解的概率较高（可重复值）
    """
    out = sys.stdout

    # 生成 t 个测试用例
    t = max(1, min(n, 10))
    out.write(str(t) + "\n")

    for _ in range(t):
        length = max(4, n)

        # 生成一个随机数组，保证有重复值概率较高
        # 将值限制在较小范围内，以促进重复出现
        value_range = max(2, min(n, 1000))
        a = [random.randint(1, value_range) for _ in range(length)]

        # 输出该用例的 n 和数组内容
        out.write(str(length) + "\n")
        out.write(" ".join(map(str, a)) + "\n")

        # 调用原逻辑得到答案并输出
        ans = solve_one_case(a)
        out.write(" ".join(map(str, ans)) + "\n")


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n
    main(10)
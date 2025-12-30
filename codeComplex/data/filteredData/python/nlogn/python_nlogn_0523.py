import random


def solve_one_case(a):
    if len(set(a)) == 1:
        x = a[0]
        return x, x, x, x

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
        return mx, mx, mx, mx
    else:
        res = []
        for k in d:
            if d[k] >= 2:
                res.append(k)
        m = len(res)
        minj = 0
        for j in range(m - 1):
            if res[j] * res[j + 1] * (res[minj] ** 2 + res[minj + 1] ** 2) > \
               res[minj] * res[minj + 1] * (res[j] ** 2 + res[j + 1] ** 2):
                minj = j
        return res[minj], res[minj], res[minj + 1], res[minj + 1]


def main(n):
    """
    n: 规模，用于生成测试数据的元素个数。
    生成一个长度为 n 的数组，元素为 [1, 10000] 的随机整数，
    然后调用原逻辑并打印结果。
    """
    # 生成单个测试用例
    a = [random.randint(1, 10000) for _ in range(n)]
    x1, x2, x3, x4 = solve_one_case(a)
    print(x1, x2, x3, x4)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
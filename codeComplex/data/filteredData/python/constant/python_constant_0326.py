def score(l):
    return sum(x * (x % 2 == 0) for x in l)


def main(n):
    # n 控制 ns 的规模与数值大小
    # 构造长度固定为 14 的列表，元素与 n 相关且确定
    ns = [(i * n + i * i) % (2 * n + 1) for i in range(14)]

    res = 0
    for i in range(14):
        l = list(ns)
        for j in range(13):
            l[(i + 1 + j) % 14] += l[i] // 14 + (1 if (j + 1) <= l[i] % 14 else 0)
        l[i] = l[i] // 14
        res = max(res, score(l))

    # print(res)
    pass
if __name__ == "__main__":
    main(10)
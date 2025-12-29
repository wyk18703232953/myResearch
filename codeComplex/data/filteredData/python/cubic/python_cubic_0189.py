import random

def main(n: int):
    # 1. 生成测试数据 b，长度为 n，元素在 [0, 2047] 内
    # 可根据需要自定义生成规则，这里用随机数
    random.seed(0)
    b = [random.randint(0, 2047) for _ in range(n)]

    # 原始逻辑开始
    e = [[-1] * (n + 1) for _ in range(2048)]

    d = [[] for _ in range(n)]
    for i, v in enumerate(b):
        if 0 <= v < 2048:
            e[v][i] = i
        d[i].append(i)

    for v in range(1, 2048):
        for i in range(n):
            j = e[v][i]
            if j != -1:
                h = e[v][j + 1]
            else:
                h = -1
            if j != -1 and h != -1:
                e[v + 1][i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for ee in d[s]:
            if s > 0:
                temp = a[s - 1] + 1
            else:
                temp = 1
            a[ee] = min(a[ee], temp)

    print(a[n - 1])


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
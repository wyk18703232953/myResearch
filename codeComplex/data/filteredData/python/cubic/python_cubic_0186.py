import random

def main(n: int):
    # 生成测试数据：b 为长度为 n 的数组，值域 [0, 2023]
    # 可按需修改数据生成方式
    b = [random.randint(0, 2023) for _ in range(n)]

    e = [[-1] * (n + 1) for _ in range(2024)]
    d = [[] for _ in range(n)]

    for j, v in enumerate(b):
        e[v][j] = j
        d[j].append(j)

    for v in range(1, 2024):
        for i in range(n):
            j = e[v][i]
            h = e[v][j + 1] if j != -1 and j + 1 <= n else -1
            if j != -1 and h != -1:
                e[v + 1][i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for pos in d[s]:
            a[pos] = min(a[pos], a[s - 1] + 1 if s > 0 else 1)

    print(a[n - 1])


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)
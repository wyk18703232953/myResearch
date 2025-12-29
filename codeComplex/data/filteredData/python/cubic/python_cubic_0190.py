import random

def main(n: int):
    # 生成测试数据：b 为长度为 n 的数组，元素在 [1, 10] 范围内
    # 数值上限不超过 2023 即可，原代码中使用到的最大值为 2023
    max_val = 10
    b = [random.randint(1, max_val) for _ in range(n)]

    # 以下是原始逻辑的改写，无 input()
    e = [[-1] * (n + 1) for _ in range(2024)]

    d = [[] for _ in range(n)]
    for i, v in enumerate(b):
        e[v][i] = i
        d[i].append(i)
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
            if s > 0:
                a[pos] = min(a[pos], a[s - 1] + 1)
            else:
                a[pos] = min(a[pos], 1)

    print(a[n - 1])


if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)
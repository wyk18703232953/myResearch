import random

def main(n: int):
    # 1. 生成测试数据 b（长度为 n，元素在 [0, 2023] 范围内）
    #    可根据需要修改生成策略
    random.seed(0)
    b = [random.randint(0, 2023) for _ in range(n)]

    # 2. 原始逻辑开始
    e = [[-1] * (n + 1) for _ in range(2024)]

    d = [[] for _ in range(n)]
    for i, v in enumerate(b):
        if 0 <= v <= 2023:  # 保证索引合法
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
        for epos in d[s]:
            a[epos] = min(a[epos], a[s - 1] + 1 if s > 0 else 1)

    # 输出结果
    print(a[n - 1])


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)
import random

def main(n: int) -> int:
    # 1. 生成规模为 n 的测试数据 b
    # 取值范围依原代码中 e 的大小设计（1..2001）
    b = [random.randint(1, 2001) for _ in range(n)]

    # 2. 原始逻辑开始
    e = [[-1] * (n + 1) for _ in range(2002)]
    d = [[] for _ in range(n)]

    for i, v in enumerate(b):
        e[v][i] = i
        d[i].append(i)

    for v in range(1, 2002):
        for i in range(n):
            j = e[v][i]
            h = e[v][j + 1] if j != -1 else -1
            if j != -1 and h != -1:
                e[v + 1][i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for pos in d[s]:
            a[pos] = min(a[pos], a[s - 1] + 1 if s > 0 else 1)

    # 返回原本会打印的结果
    return a[n - 1]


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需修改 n
    result = main(10)
    print(result)
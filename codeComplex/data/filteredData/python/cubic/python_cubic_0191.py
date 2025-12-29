import random

def main(n: int) -> int:
    # 生成测试数据：b 为长度为 n、元素在 1..3023 之间的随机序列
    max_v = 3023
    b = [random.randint(1, max_v) for _ in range(n)]

    e = [[-1] * (n + 1) for _ in range(3024)]
    d = [[] for _ in range(n)]
    for i, v in enumerate(b):
        e[v][i] = i
        d[i].append(i)

    for v in range(1, 3024):
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

    # 原程序打印 a[n-1]，这里返回方便调用
    return a[n - 1]


if __name__ == "__main__":
    # 示例：规模为 10
    result = main(10)
    print(result)
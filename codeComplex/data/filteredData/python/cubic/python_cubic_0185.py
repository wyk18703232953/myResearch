import random

def main(n: int) -> int:
    # 生成测试数据：b 为 0..n-1 范围内的整数
    # 这里简单生成随机数据；可按需改为其他分布
    random.seed(0)
    b = [random.randint(0, n - 1) for _ in range(n)]

    # 原逻辑开始
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
        for e_idx in d[s]:
            a[e_idx] = min(a[e_idx], a[s - 1] + 1 if s > 0 else 1)

    # 返回原程序最终输出
    return a[n - 1]


if __name__ == "__main__":
    # 示例：运行规模 n=10
    result = main(10)
    print(result)
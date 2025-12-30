import random

def main(n: int) -> int:
    # 1. 生成测试数据：长度为 n，元素取值范围 [1, 2023]
    # 确保不会越界使用 tracker 的第一维（大小为 2024）
    arr = [random.randint(1, 2023) for _ in range(n)]

    # 原始逻辑开始
    tracker = [[-1] * (n + 1) for _ in range(2024)]

    d = [[] for _ in range(n)]
    for j, v in enumerate(arr):
        tracker[v][j] = j
        d[j].append(j)

    for v in range(1, 2024):
        for i in range(n):
            j = tracker[v][i]
            h = tracker[v][j + 1] if j != -1 and j + 1 <= n else -1
            if j != -1 and h != -1:
                tracker[v + 1][i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for pos in d[s]:
            a[pos] = min(a[pos], a[s - 1] + 1 if s > 0 else 1)

    # 保留原程序输出行为：返回 a[n-1]
    return a[n - 1]


# 示例调用（按需使用）
if __name__ == "__main__":
    # 例如 n = 10
    result = main(10)
    print(result)
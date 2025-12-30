import random

def main(n):
    # 1. 生成测试数据
    # 生成一个随机的 n 个点的置换 a（0-based）
    a = list(range(n))
    random.shuffle(a)
    # 生成每个点的随机费用 c
    # 这里费用取 1~10^9 的随机整数
    c = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 原逻辑
    visited = [-1] * n
    res = 0

    for i in range(n):
        trace = []

        t = i
        mn = 10**18
        while visited[t] == -1:
            visited[t] = i
            trace.append(t)
            t = a[t]

        if visited[t] != i:
            continue

        while trace:
            v = trace.pop()
            mn = min(mn, c[v])
            if t == v:
                break

        res += mn

    print(res)


if __name__ == "__main__":
    # 可以修改这里的 n 以改变规模
    main(10)
import random

def main(n: int):
    # 生成测试数据：
    # cost[1..n]: 1 到 10^9 之间的随机权值
    # arr[1..n]: 随机生成的置换（每个点出度为 1，且为一个排列）
    #
    # 原程序结构：
    # n
    # cost[1..n]
    # arr[1..n]
    #
    # 这里直接在内存中构造 cost 和 arr 数组

    # 1. 生成 cost 数组（下标从 1 开始）
    cost = [0] + [random.randint(1, 10**9) for _ in range(n)]

    # 2. 生成 arr 作为一个随机排列（1..n 的排列）
    arr = [0] + random.sample(range(1, n + 1), n)

    # 3. 逻辑与原 main() 一致
    nv = [-1] * (n + 1)
    colors = []
    c = 0
    for i in range(1, n + 1):
        if nv[i] != -1:
            continue
        nv[i] = c
        dest = arr[i]
        while nv[dest] == -1:
            nv[dest] = c
            dest = arr[dest]
        if nv[dest] == c:
            colors.append(dest)
        c += 1

    s = 0
    for i in colors:
        mi = cost[i]
        nxt = arr[i]
        while nxt != i:
            mi = min(mi, cost[nxt])
            nxt = arr[nxt]
        s += mi

    # 输出与原程序相同的结果：所有环上的最小 cost 之和
    print(s)


if __name__ == "__main__":
    # 示例：调用 main，规模可按需调整
    main(10)
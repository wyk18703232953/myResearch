import random

def main(n):
    # 1. 生成测试数据：构造一个 1..n 的随机排列作为 arr
    #    每个点必须有且只有一个出边，原程序正是基于这种结构（排列上的若干环）。
    perm = list(range(1, n + 1))
    random.shuffle(perm)

    # cost: 1..n 的随机正整数权值，这里取 1..10^9 之间
    cost = [0] + [random.randint(1, 10**9) for _ in range(n)]
    arr = [0] + perm  # arr[i] 表示 i 指向的节点

    # 以下为原 main 逻辑的无 input() 改写
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

    print(s)


if __name__ == "__main__":
    # 示例：n = 10，可按需修改或在外部调用 main(n)
    main(10)
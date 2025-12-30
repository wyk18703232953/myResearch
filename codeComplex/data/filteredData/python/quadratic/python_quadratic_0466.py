from queue import Queue
import random

def main(n: int):
    # 生成一棵 n 个节点的随机树（节点编号 1..n）
    g = [set() for _ in range(n + 1)]
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)  # 随机选择一个前面的节点作为父节点
        g[u].add(v)
        g[v].add(u)

    # 生成一个从 1 开始的随机遍历序列 a（打乱 2..n 的顺序）
    rest = list(range(2, n + 1))
    random.shuffle(rest)
    a = [1] + rest

    # 下面是原逻辑（移除所有 input()，使用生成的 g 和 a）
    if a[0] != 1:
        print("No")
        return

    ptr = 0
    i = 1

    # 为了不破坏生成的树结构，拷贝一份 g
    g_work = [set(nei) for nei in g]

    while i < n:
        par = a[ptr]
        while len(g_work[par]) != 0:
            if i >= n:  # 防止越界
                print("No")
                return
            if a[i] not in g_work[par]:
                print("No")
                return
            else:
                g_work[par].remove(a[i])
                g_work[a[i]].remove(par)
            i += 1
        ptr += 1
        if ptr >= n:  # 防止越界
            break
    print("Yes")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
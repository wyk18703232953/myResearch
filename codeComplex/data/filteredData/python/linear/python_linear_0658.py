import random

def main(n):
    # 生成测试数据：随机生成一棵 n 个节点的树和一个整数 s
    # 节点编号为 1..n
    if n < 2:
        return

    # 随机生成 s（可按需要调整范围）
    s = random.randint(1, 10**6)

    # 生成一棵随机树：对于每个节点 i(2..n)，随机连到一个之前的节点 1..i-1
    edges = []
    for i in range(2, n + 1):
        p = random.randint(1, i - 1)
        edges.append((p, i))

    # 以下为原逻辑的改写（无 input）
    a = [0] * (n + 1)

    if n == 2:
        print(s)
        return

    for u, v in edges:
        a[u] += 1
        a[v] += 1

    leaf_count = a.count(1)
    if leaf_count == 0:
        # 理论上树至少有 2 个叶子，这里仅作健壮性处理
        print(0.0)
    else:
        print(2.0 * s / leaf_count)


if __name__ == "__main__":
    # 示例：调用 main(10)，可以按需要修改 n
    main(10)
import random

def main(n):
    # 生成测试数据：n, k 和 P
    # 这里假设原题中 P 中的数在 [0, 255] 范围内
    # k：容量上限，随 n 调整，可按需修改策略
    k = max(1, n // 2)
    P = [random.randint(0, 255) for _ in range(n)]

    parent = list(range(256))
    sz = [1] * 256

    def rt(x):
        if x != parent[x]:
            parent[x] = rt(parent[x])
        return parent[x]

    def u(rx, ry):
        parent[ry] = rx
        sz[rx] += sz[ry]

    ans = [0] * n
    for i, p in enumerate(P):
        rx = rt(p)
        while rx > 0 and sz[rx] + sz[rt(rx - 1)] <= k:
            u(rt(rx - 1), rx)
            rx = rt(p)
        ans[i] = rt(p)

    # 按原程序风格输出
    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    # 示例：规模为 10，可按需修改或在外部调用 main
    main(10)
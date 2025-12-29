import random

def main(n: int):
    # 生成测试数据：
    # c: 长度为 n 的随机正整数数组
    # a: 长度为 n 的随机排列，表示 1..n 的置换（每个点出度为 1，保证是若干个环 + 链的结构）
    random.seed(0)
    c = [random.randint(1, 10**9) for _ in range(n)]
    p = list(range(1, n + 1))
    random.shuffle(p)
    a = p[:]  # a[i] 取值在 1..n 之间

    u = [0] * n
    ans = 0

    for i in range(n):
        if u[i] != 0:
            continue
        idx = i
        # 第一轮：走链直到遇到已访问的点
        while u[idx] == 0:
            u[idx] = 1
            idx = a[idx] - 1

        # 如果遇到的是已经确认过的点（u == 2），说明这条路径不包含新的环
        if u[idx] == 2:
            idx = i
            while u[idx] == 1:
                u[idx] = 2
                idx = a[idx] - 1
            continue

        # 此时 idx 落在一个新环上，求该环上的最小 c 值
        start = idx
        mn = c[idx]
        u[idx] = 2
        while a[idx] - 1 != start:
            idx = a[idx] - 1
            mn = min(mn, c[idx])
            u[idx] = 2

        # 把从 i 出发到环的路径上的点也标记为 2
        idx = i
        while u[idx] == 1:
            u[idx] = 2
            idx = a[idx] - 1

        ans += mn

    print(ans)


if __name__ == "__main__":
    # 示例：n 可自由修改
    main(10)
import random

def main(n):
    # 生成规模为 n 的测试数据
    # m 取一个不大于 n 的正整数
    if n <= 0:
        return

    m = max(1, n // 2)  # 示例：m 为 n 的一半，至少为 1

    # xs: n 个整数，取值范围示例 [-10^9, 10^9]
    xs = [random.randint(-10**9, 10**9) for _ in range(n)]

    # ts: n 个 0/1，保证至少有一个 1，否则原逻辑依赖 ds 会出问题
    ts = [random.randint(0, 1) for _ in range(n)]
    if all(t == 0 for t in ts):
        ts[random.randrange(n)] = 1

    # 逻辑开始（移植自原程序，并参数化 m, xs, ts）
    ps = [x for x, t in zip(xs, ts) if t == 0]
    ds = [x for x, t in zip(xs, ts) if t == 1]

    # 若 ds 为空，原代码会在 abs(ds[di] - p) 时报错，这里做个保护
    if not ds:
        # 如果没有 t == 1，则 ans 全为 0
        ans = [0] * m
        print(' '.join(map(str, ans)))
        return

    # 如果 ds 的数量与 m 不一致，原题一般是 m == len(ds)
    # 这里将 m 截断或扩展为 len(ds)，以保持逻辑一致性
    if len(ds) != m:
        m = len(ds)

    ans = [0] * m

    di = 0
    for pi, p in enumerate(ps):
        while di < m - 1 and abs(ds[di] - p) > abs(ds[di + 1] - p):
            di += 1

        if di >= m:
            ans[m - 1] += len(ps) - pi
            break

        ans[di] += 1

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    # 示例调用：n 可根据需要调整
    main(10)
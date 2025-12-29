import random

def main(n):
    # 生成数据规模：n 行，m 列（可根据需要调整 m）
    m = max(1, min(10, n))  # 简单设为不超过 10 的 n
    # 生成测试数据：a[i][j] 为 0~1e9 的随机整数
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    def get_ans(x):
        lim = 1 << m
        match = lim - 1
        track = [-1 for _ in range(lim)]

        for i in range(n):
            mask = 0
            for j in range(m):
                if a[i][j] >= x:
                    mask |= 1 << j
            track[mask] = i

        for i in range(lim):
            if track[i] == -1:
                continue
            for j in range(lim):
                if track[j] == -1:
                    continue
                if (i | j) == match:
                    return track[i], track[j]

        return -1, -1

    lo = 0
    hi = 10**9
    while lo < hi - 1:
        mid = (lo + hi) // 2
        i, j = get_ans(mid)
        if i == -1:
            hi = mid - 1
        else:
            lo = mid

    i, j = get_ans(hi)
    if i != -1:
        print(f"{i+1} {j+1}")
    else:
        i, j = get_ans(lo)
        print(f"{i+1} {j+1}")


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(5)
import random

def main(n):
    # 生成测试数据：原点坐标 x0, y0 以及 n 个点的坐标
    # 这里使用随机整数坐标，范围可按需调整
    random.seed(0)
    x0, y0 = 0, 0
    arr = [[x0, y0]]
    for _ in range(n):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        arr.append([x, y])

    # 预计算所有点对间的平方距离
    dist = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            dist[i][j] = (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2

    def dfs(status, memo, pp):
        if memo[status] is not None:
            return memo[status]
        if status < 0:
            return 1e8
        res = 1e8
        prev = []
        for i in range(1, n + 1):
            if (status & (1 << (i - 1))) == 0:
                continue
            t1 = status ^ (1 << (i - 1))
            temp = dfs(t1, memo, pp) + dist[0][i] * 2
            if temp < res:
                res = temp
                prev = [i, 0]
            for j in range(i + 1, n + 1):
                if (t1 & (1 << (j - 1))) == 0:
                    continue
                nxt = t1 ^ (1 << (j - 1))
                temp = dfs(nxt, memo, pp) + dist[0][j] + dist[j][i] + dist[i][0]
                if temp < res:
                    res = temp
                    prev = [i, j, 0]
            break
        memo[status] = res
        pp[status] = prev
        return res

    memo = [None for _ in range(1 << n)]
    pp = [None for _ in range(1 << n)]
    memo[0] = 0
    pp[0] = []

    end = (1 << n) - 1
    res = dfs(end, memo, pp)

    path = [0]
    cur = end
    while cur > 0:
        prev = pp[cur]
        path.extend(prev)
        for i in range(len(prev) - 1):
            cur -= (1 << (prev[i] - 1))

    print(res)
    print(' '.join(map(str, path)))


if __name__ == "__main__":
    # 示例：n = 4
    main(4)
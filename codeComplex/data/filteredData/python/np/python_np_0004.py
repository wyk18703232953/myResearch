import random
import math

def main(n):
    # 1. 生成测试数据：手提包坐标 (xs, ys) 与 n 个物品坐标
    random.seed(0)
    xs, ys = random.uniform(-10, 10), random.uniform(-10, 10)
    objects = []
    for _ in range(n):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        objects.append([x, y])

    # 2. 将手提包作为第 n 个点加入
    objects.append([xs, ys])  # objects[n] is handbag

    # 3. 预计算距离平方
    dist = [[0.0] * (n + 1) for _ in range(n + 1)]
    dist2 = [[0.0] * n for _ in range(n)]

    for i in range(n + 1):
        xi, yi = objects[i]
        for j in range(n + 1):
            xj, yj = objects[j]
            dx = xi - xj
            dy = yi - yj
            dist[i][j] = dx * dx + dy * dy

    for i in range(n):
        for j in range(n):
            dist2[i][j] = dist[n][i] + dist[i][j] + dist[j][n]

    # 4. 动态规划
    INF = 1e18
    dp = [INF] * (1 << n)
    vis = set([0])
    dp[0] = 0.0

    for mask in range((1 << n) - 1):
        if mask in vis:
            for j in range(n):
                if mask & (1 << j) == 0:
                    new_mask = mask | (1 << j)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + 2.0 * dist[n][j])
                    vis.add(new_mask)

                    for k in range(j + 1, n):
                        if mask & (1 << k) == 0:
                            new_mask2 = new_mask | (1 << k)
                            dp[new_mask2] = min(dp[new_mask2], dp[mask] + dist2[j][k])
                            vis.add(new_mask2)

                    break

    # 5. 回溯路径
    curr = (1 << n) - 1
    path = [0]
    while curr:
        for i in range(n):
            if curr & (1 << i):
                if dp[curr] == dp[curr ^ (1 << i)] + 2.0 * dist[n][i]:
                    path.extend([i + 1, 0])
                    curr ^= (1 << i)
                    break
                for j in range(i + 1, n):
                    if curr & (1 << j):
                        prev_mask = curr ^ (1 << i) ^ (1 << j)
                        if dp[curr] == dp[prev_mask] + dist2[i][j]:
                            path.extend([j + 1, i + 1, 0])
                            curr = prev_mask
                            break
                else:
                    continue
                break

    # 6. 输出结果
    print(int(dp[(1 << n) - 1]))
    print(*path[::-1])


if __name__ == "__main__":
    # 示例：n = 4
    main(4)
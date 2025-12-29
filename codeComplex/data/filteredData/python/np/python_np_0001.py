def main(n: int):
    # 1. 生成测试数据
    # 随机生成坐标点：n 个物品 + 1 个手提包位置
    # 为了结果可复现，这里不用随机数，直接按规律生成
    xs, ys = 0.0, 0.0  # 手提包位置
    objects = []
    for i in range(n):
        # 简单构造：物品分布在一条折线上
        x = float(i)
        y = float(i * i % (2 * n + 1))
        objects.append([x, y])
    objects.append([xs, ys])  # objects[n] 是手提包

    # 2. 原逻辑：预计算距离
    dist = [[0.0] * (n + 1) for _ in range(n + 1)]
    dist2 = [[0.0] * n for _ in range(n)]

    for i in range(n + 1):
        for j in range(n + 1):
            dx = objects[i][0] - objects[j][0]
            dy = objects[i][1] - objects[j][1]
            dist[i][j] = dx * dx + dy * dy

    for i in range(n):
        for j in range(n):
            dist2[i][j] = dist[n][i] + dist[i][j] + dist[j][n]

    # 3. DP 求最优值
    INF = 1e18
    dp = [INF] * (1 << n)
    vis = {0}
    dp[0] = 0.0

    for mask in range((1 << n) - 1):
        if mask in vis:
            for j in range(n):
                if mask & (1 << j) == 0:
                    new_mask = mask | (1 << j)
                    cost1 = dp[mask] + 2.0 * dist[n][j]
                    if cost1 < dp[new_mask]:
                        dp[new_mask] = cost1
                    vis.add(new_mask)

                    for k in range(j + 1, n):
                        if mask & (1 << k) == 0:
                            new_mask2 = new_mask | (1 << k)
                            cost2 = dp[mask] + dist2[j][k]
                            if cost2 < dp[new_mask2]:
                                dp[new_mask2] = cost2
                            vis.add(new_mask2)
                    break

    # 4. 还原路径
    curr = (1 << n) - 1
    path = [0]
    while curr:
        updated = False
        for i in range(n):
            if curr & (1 << i):
                prev_mask = curr ^ (1 << i)
                if dp[curr] == dp[prev_mask] + 2.0 * dist[n][i]:
                    path.extend([i + 1, 0])
                    curr = prev_mask
                    updated = True
                    break

                for j in range(i + 1, n):
                    if curr & (1 << j):
                        prev_mask2 = curr ^ (1 << i) ^ (1 << j)
                        if dp[curr] == dp[prev_mask2] + dist2[i][j]:
                            path.extend([j + 1, i + 1, 0])
                            curr = prev_mask2
                            updated = True
                            break
                if updated:
                    break
        if not updated:
            # 理论上不会发生，仅防止死循环
            break

    print(int(dp[(1 << n) - 1]))
    print(*path[::-1])


# 示例调用
if __name__ == "__main__":
    main(4)
def main(n):
    # Generate deterministic coordinates based on n
    # things[0] is the starting point (xs, ys, 0)
    # Next n points have coordinates derived from their index
    xs = 0
    ys = 0
    things = [[xs, ys, 0]]
    for i in range(1, n + 1):
        x = i
        y = i * 2
        things.append([x, y, i])

    distance = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(i, n + 1):
            dx = things[i][0] - things[j][0]
            dy = things[i][1] - things[j][1]
            d = dx * dx + dy * dy
            distance[i][j] = d
            distance[j][i] = d

    INF = float('inf')
    DP = [INF for _ in range((1 << n) + 10)]
    Path = [None for _ in range((1 << n) + 10)]
    DP[0] = 0

    for cur in range(1 << n):
        if DP[cur] == INF:
            continue
        for nxt1 in range(n):
            if cur & (1 << nxt1) != 0:
                continue

            if DP[cur | (1 << nxt1)] > DP[cur] + distance[0][nxt1 + 1] + distance[nxt1 + 1][0]:
                DP[cur | (1 << nxt1)] = DP[cur] + distance[0][nxt1 + 1] + distance[nxt1 + 1][0]
                Path[cur | (1 << nxt1)] = cur

            for nxt2 in range(n):
                if (cur | (1 << nxt1)) & (1 << nxt2) != 0:
                    continue
                new_mask = cur | (1 << nxt1) | (1 << nxt2)
                new_cost = DP[cur] + distance[0][nxt1 + 1] + distance[nxt1 + 1][nxt2 + 1] + distance[nxt2 + 1][0]
                if DP[new_mask] > new_cost:
                    DP[new_mask] = new_cost
                    Path[new_mask] = cur
            break

    result_cost = DP[(1 << n) - 1]

    path = []
    cur = (1 << n) - 1
    while cur != 0:
        path.append(0)
        father = Path[cur]
        diff = cur ^ father
        d1 = len(bin(diff)[2:])
        path.append(d1)
        diff ^= (1 << (d1 - 1))
        if diff != 0:
            d2 = len(bin(diff)[2:])
            path.append(d2)
        cur = father
    path.append(0)
    path = list(reversed(path))

    print(result_cost)
    print(' '.join(map(str, path)))


if __name__ == "__main__":
    main(4)
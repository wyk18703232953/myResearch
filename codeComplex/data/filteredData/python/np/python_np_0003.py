import random
import math

def main(n: int):
    # 1. 生成测试数据：
    #    点 0 为起点 (xs, ys)，后面 n 个点为 things 1..n
    #    这里生成整数坐标，可根据需要调整范围
    random.seed(0)
    xs = random.randint(0, 100)
    ys = random.randint(0, 100)
    things = [[xs, ys, 0]]
    for i in range(n):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        things.append([x, y, i + 1])

    # 2. 预计算距离（平方距离）
    distance = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(i, n + 1):
            d = (things[i][0] - things[j][0]) ** 2 + (things[i][1] - things[j][1]) ** 2
            distance[i][j] = distance[j][i] = d

    INF = float('inf')
    DP = [INF for _ in range((1 << n) + 10)]
    Path = [None for _ in range((1 << n) + 10)]
    DP[0] = 0

    # 3. 按原逻辑做 DP
    for cur in range(1 << n):
        if DP[cur] == INF:
            continue
        for nxt1 in range(n):
            if cur & (1 << nxt1) != 0:
                continue

            # 只带一个物品（nxt1）往返
            if DP[cur | (1 << nxt1)] > DP[cur] + distance[0][nxt1 + 1] + distance[nxt1 + 1][0]:
                DP[cur | (1 << nxt1)] = DP[cur] + distance[0][nxt1 + 1] + distance[nxt1 + 1][0]
                Path[cur | (1 << nxt1)] = cur

            # 一次带两个物品（nxt1, nxt2）
            for nxt2 in range(n):
                if (cur | (1 << nxt1)) & (1 << nxt2) != 0:
                    continue
                new_state = cur | (1 << nxt1) | (1 << nxt2)
                cost = (DP[cur] +
                        distance[0][nxt1 + 1] +
                        distance[nxt1 + 1][nxt2 + 1] +
                        distance[nxt2 + 1][0])
                if DP[new_state] > cost:
                    DP[new_state] = cost
                    Path[new_state] = cur
            break

    # 4. 输出最优代价
    print(DP[(1 << n) - 1])

    # 5. 还原路径并输出，与原程序保持一致的输出格式
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
    print(' '.join(map(str, path)))


if __name__ == "__main__":
    # 示例：调用 main(4)
    main(4)
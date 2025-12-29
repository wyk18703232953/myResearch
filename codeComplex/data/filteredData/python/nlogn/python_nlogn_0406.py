import random

def main(n):
    # 1. 生成测试数据：n 个区间 [a, b]，保证 a <= b
    # 你可以根据需要调整生成策略
    intervals = []
    for _ in range(n):
        a = random.randint(0, 2 * n)
        b = random.randint(0, 2 * n)
        if a > b:
            a, b = b, a
        intervals.append((a, b))

    # 2. 以下为原 solve() 的逻辑，改为使用生成的数据 intervals

    points = []
    for a, b in intervals:
        points.append(a)
        points.append(b)
    points.sort()

    k = 0
    coord_index = {}
    coord_list = []
    for x in points:
        if x not in coord_index:
            coord_index[x] = k
            coord_list.append(x)
            k += 1

    n1 = len(coord_index)
    dp = [[0, 0] for _ in range(n1)]
    for a, b in intervals:
        dp[coord_index[a]][0] += 1
        dp[coord_index[b]][1] -= 1

    ans = {}
    last = dp[0][0]
    ans[last] = 1
    last += dp[0][1]

    for i in range(1, n1):
        cnts = coord_list[i] - coord_list[i - 1] - 1
        if last in ans:
            ans[last] += cnts
        else:
            ans[last] = cnts

        last += dp[i][0]
        if last in ans:
            ans[last] += 1
        else:
            ans[last] = 1
        last += dp[i][1]

    if last in ans:
        ans[last] += 1
    else:
        ans[last] = 1

    # 输出与原程序一致：从 1 到 n 的答案
    res = []
    for i in range(1, n + 1):
        res.append(str(ans.get(i, 0)))
    print(" ".join(res))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
from heapq import heappush, heappop
import random


def main(n: int):
    # 生成测试数据：长度为 n 的数组 aa，元素为 1~5 的随机整数
    random.seed(0)
    aa = [random.randint(1, 5) for _ in range(n)]

    # 原逻辑开始
    inf = 10 ** 9
    dp1 = [[-1] * (n + 1) for _ in range(n)]
    to = [[i + 1] for i in range(n)]
    for i in range(n):
        dp1[i][i + 1] = aa[i]

    for w in range(2, n + 1):
        for l in range(n - w + 1):
            r = l + w
            for m in range(l + 1, r):
                if dp1[l][m] != -1 and dp1[l][m] == dp1[m][r]:
                    dp1[l][r] = dp1[l][m] + 1
                    to[l].append(r)

    hp = []
    heappush(hp, (0, 0))
    dist = [-1] * (n + 1)
    ans = None
    while hp:
        d, i = heappop(hp)
        if i == n:
            ans = d
            break
        if dist[i] != -1:
            continue
        dist[i] = d
        for j in to[i]:
            if dist[j] != -1:
                continue
            heappush(hp, (d + 1, j))

    # 输出结果（不输出测试数据，只输出答案）
    print(ans)


# 示例调用
if __name__ == "__main__":
    main(10)
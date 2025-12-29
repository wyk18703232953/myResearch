import random

def main(n: int):
    # 生成测试数据：
    # n: 骑士/金币数量
    # k: 从 0 到 n-1 的某个值
    k = random.randint(0, max(0, n - 1))
    # 为保证逻辑可见，生成较小的金币值
    knight = [random.randint(1, 100) for _ in range(n)]
    coins = [random.randint(1, 100) for _ in range(n)]

    # 原逻辑开始
    d = {}
    ans = [0] * n
    for i in range(n):
        knight[i] = [knight[i], i]
    for i in coins:
        d[i] = d.get(i, 0) + 1
    c = coins[:]
    knight = sorted(knight, key=lambda x: x[0])
    ans2 = []
    ans = coins[:]
    if k == 0:
        print(*ans)
    else:
        for i in range(n):
            ans1 = 0
            if len(ans2) < k:
                ans1 = sum(ans2)
            else:
                ans2 = sorted(ans2)[-k:]
                ans1 += sum(ans2)
            ans[knight[i][1]] += ans1
            ans2.append(coins[knight[i][1]])
        print(*ans)


if __name__ == "__main__":
    # 示例调用：可自行修改 n 的大小
    main(5)
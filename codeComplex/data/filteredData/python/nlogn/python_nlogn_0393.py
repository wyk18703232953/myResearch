import random

def main(n):
    # 生成测试数据
    # n: 人数规模
    # 随机生成 k，1 <= k <= n
    k = random.randint(1, n)
    # 随机生成 power 和 coins，范围可按需调整
    power = [random.randint(1, 10**6) for _ in range(n)]
    coins = [random.randint(1, 10**6) for _ in range(n)]

    dp = [0 for _ in range(n)]

    def takeSecond(elem):
        return elem[1]

    def takeFirst(elem):
        return elem[0]

    people = [(power[i], coins[i], i) for i in range(n)]
    people.sort(key=takeFirst)

    dp[0] = []

    for i, p in enumerate(people):
        if i == 0:
            continue
        kills = [v for v in dp[i - 1]]
        kills.append(people[i - 1][1])

        if len(kills) > k:
            # 移除最小的金币
            kills.remove(min(kills))

        dp[i] = kills

    x = [(people[i][2], str(sum(dp[i]) + people[i][1])) for i in range(n)]
    x.sort(key=takeFirst)

    print(" ".join(z[1] for z in x))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
def main(n):
    # n 表示数组长度
    if n <= 0:
        return

    # 确定性生成 k、knight 和 coins
    # 让 k 与 n 相关，但不超过 n
    k = n // 3

    # 生成 knight：一个长度为 n 的整数数组
    # 示例：knight[i] = (i * 7 + 3) % (2*n + 1)
    knight = [(i * 7 + 3) % (2 * n + 1) for i in range(n)]

    # 生成 coins：一个长度为 n 的整数数组
    # 示例：coins[i] = (i * i + 5) % (3*n + 1)
    coins = [(i * i + 5) % (3 * n + 1) for i in range(n)]

    # 保持原算法逻辑
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
        # print(*ans)
        pass

    else:
        for i in range(n):
            if len(ans2) < k:
                ans1 = sum(ans2)

            else:
                ans2 = sorted(ans2)[-k:]
                ans1 = sum(ans2)
            ans[knight[i][1]] += ans1
            ans2.append(coins[knight[i][1]])
        # print(*ans)
        pass
if __name__ == "__main__":
    main(10)
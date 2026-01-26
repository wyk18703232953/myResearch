def main(n):
    # n 表示硬币数量
    coins = []
    coinsValueTotal = 0

    # 确定性生成硬币面值：例如 coins[i] = (i % 10) + 1
    for i in range(n):
        coin = (i % 10) + 1
        coins.append(coin)
        coinsValueTotal += coin

    coins.sort(reverse=True)
    minCoins = 0
    halfCoinsValueTotal = coinsValueTotal / 2
    for i in range(len(coins)):
        minCoins += coins[i]
        if minCoins > halfCoinsValueTotal:
            # print(i + 1)
            pass
            break


if __name__ == "__main__":
    main(10)
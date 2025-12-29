import random

def main(n):
    # 1. 生成规模为 n 的测试数据：n 枚硬币，面值为 1~100 的随机整数
    coins = [random.randint(1, 100) for _ in range(n)]

    # 2. 原始逻辑
    coinsValueTotal = sum(coins)
    coins.sort(reverse=True)

    minCoins = 0
    halfCoinsValueTotal = coinsValueTotal / 2

    for i in range(len(coins)):
        minCoins += coins[i]
        if minCoins > halfCoinsValueTotal:
            print(i + 1)
            break

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
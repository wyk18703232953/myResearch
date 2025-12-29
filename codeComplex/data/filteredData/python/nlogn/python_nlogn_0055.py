import random

def main(n: int):
    # 生成测试数据：n 个硬币，每个面值在 1~100 之间
    coins = [random.randint(1, 100) for _ in range(n)]
    coins.sort(reverse=True)

    target = (sum(coins) + 2) // 2

    count = 1
    total = coins[count - 1]
    while total < target and count < n:
        count += 1
        total += coins[count - 1]

    print(count)


if __name__ == "__main__":
    # 示例：n=10，可按需修改
    main(10)
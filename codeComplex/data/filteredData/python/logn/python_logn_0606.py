import math
import random

def minPut(n):
    return math.ceil((-1 + math.sqrt(1 - 4 * (-n * 2))) / 2)

def nCandies(n):
    return int(n * (n + 1) / 2)

def solve(actions, candies):
    put = minPut(candies)
    putCandies = nCandies(put)

    eat = putCandies - candies

    while put + eat < actions:
        eat += put + 1
        put += 1

    return eat

def main(n):
    """
    n 为规模参数，用于生成测试数据。
    这里简单约定：
      actions 在 [1, 10*n]
      candies 在 [1, 10*n]
    并保证 actions >= candies 以避免无意义数据。
    """
    random.seed(0)
    actions = random.randint(1, 10 * n)
    candies = random.randint(1, 10 * n)
    if actions < candies:
        actions, candies = candies, actions

    result = solve(actions, candies)
    print(result)

if __name__ == "__main__":
    # 示例：使用规模 10 运行
    main(10)
import random

def main(n):
    # 随机生成规模
    games = n
    bills = n

    # 生成测试数据：
    # g: 随机游戏价格（1~100）
    # b: 随机账单额度（1~100），排序后更符合匹配逻辑的一般用法
    g = [random.randint(1, 100) for _ in range(games)]
    b = [random.randint(1, 100) for _ in range(bills)]
    g.sort()
    b.sort()

    total = 0
    i = 0
    j = 0

    while i < games and j < bills:
        if g[i] <= b[j]:
            total += 1
            i += 1
            j += 1
        else:  # g[i] > b[j]
            i += 1

    print(total)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
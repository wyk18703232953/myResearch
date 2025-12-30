import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里将 n 作为 groupSize，其他三个值在合理范围内随机生成
    groupSize = n
    # 假定每个门店单独通过的人数不超过 groupSize
    mecces = random.randint(0, groupSize)
    burgerKing = random.randint(0, groupSize)
    both = random.randint(0, min(mecces, burgerKing, groupSize))

    # 原逻辑
    mecces_adj = mecces - both
    burgerKing_adj = burgerKing - both
    notPassed = groupSize - sum((mecces_adj, burgerKing_adj, both))

    if notPassed > 0 and burgerKing_adj >= 0 and mecces_adj >= 0:
        print(notPassed)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)
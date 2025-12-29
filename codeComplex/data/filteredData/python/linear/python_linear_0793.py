import random

def main(n):
    """
    n: 牌张数，随机生成 n 张 [1-9][smp] 形式的手牌，
       然后执行原程序逻辑并打印结果。
    """
    # 生成测试数据：随机 n 张牌
    # 花色: s,m,p; 点数: 1-9
    suits = ['s', 'm', 'p']
    tiles = []
    for _ in range(n):
        rank = random.randint(1, 9)
        suit = random.choice(suits)
        tiles.append(f"{rank}{suit}")
    input_str = " ".join(tiles)

    # 原始逻辑开始
    m = {"s": [0] * 9, "m": [0] * 9, "p": [0] * 9}
    for e in input_str.split():
        m[e[1]][int(e[0]) - 1] += 1
    ret = 2
    for t in "smp":
        l = m[t]
        if max(l) >= 2:
            ret = min(ret, 3 - max(l))
        else:
            for i in range(7):
                seq = sum(l[i:i + 3])
                ret = min(ret, 3 - seq)
    print(ret)


if __name__ == "__main__":
    # 示例：规模 n = 13
    main(13)
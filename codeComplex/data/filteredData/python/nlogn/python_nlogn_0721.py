def main(n):
    # 生成规模为 n 的测试数据：n 张牌，每张牌为 1-9 + m/p/s 之一
    import random
    random.seed(0)
    suits = 'mps'
    cards = []
    for _ in range(n):
        a = random.randint(1, 9)
        b = random.choice(suits)
        cards.append(f"{a}{b}")

    # 原逻辑开始
    f = lambda c: 'mps'.index(c)
    l = [[], [], []]
    for c in cards:
        a, b = c
        l[f(b)].append(int(a))
    for i in range(3):
        l[i].sort()

    res = 3
    for x in l:
        if len(x) == 0:
            continue
        elif len(x) == 1:
            res = min(res, 2)
        elif len(x) == 3:
            if len(set(x)) == 1:
                res = min(res, 0)
                break
            if x[0] == x[1] - 1 and x[1] == x[2] - 1:
                res = min(res, 0)
                break
        res = min(res, 2)
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                if abs(x[i] - x[j]) <= 2:
                    res = min(res, 1)
    print(res)


if __name__ == "__main__":
    main(3)
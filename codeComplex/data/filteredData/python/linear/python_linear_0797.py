import random

def main(n):
    # n 为手牌数量规模，这里生成 n 张牌，牌种类限制在 m/p/s 三种花色、1~9 牌面
    suits = ['m', 'p', 's']
    hand = []
    for _ in range(n):
        num = random.randint(1, 9)
        suit = random.choice(suits)
        hand.append(f"{num}{suit}")

    t = [[0] * 9 for _ in range(3)]

    for x in hand:
        if x[1] == 'm':
            idx = 0
        elif x[1] == 'p':
            idx = 1
        elif x[1] == 's':
            idx = 2
        else:
            continue
        t[idx][int(x[0]) - 1] += 1

    max_cons = 0
    max_mult = 0
    for i in range(3):
        cons = [0, 0, 0]
        for j in range(9):
            cons[0] = cons[1]
            cons[1] = cons[2]
            cons[2] = 1 if t[i][j] > 0 else 0
            max_cons = max(sum(cons), max_cons)
            max_mult = max(max_mult, t[i][j])

    print(3 - max(max_cons, max_mult))


if __name__ == '__main__':
    main(14)  # 示例：规模为 14（类似麻将一手牌的张数）
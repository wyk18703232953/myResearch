def main(n):
    # 构造确定性的手牌列表 hand，长度与 n 相关
    # 花色循环：m, p, s
    suits = ['m', 'p', 's']
    hand = []
    for i in range(n):
        rank = i % 9 + 1          # 1~9 循环
        suit = suits[(i // 9) % 3]
        hand.append(str(rank) + suit)

    buflist = hand
    hand = buflist
    t = []
    for i in range(3):
        t.append([])
        for j in range(9):
            t[i].append(0)
    for x in hand:
        idx = 0
        if x[1] == 'm':
            idx = 0
        elif x[1] == 'p':
            idx = 1
        elif x[1] == 's':
            idx = 2
        t[idx][int(x[0]) - 1] += 1
    max_cons = 0
    max_mult = 0
    for i in range(3):
        cons = [0, 0, 0]
        for j in range(9):
            cons[0] = cons[1]
            cons[1] = cons[2]
            if t[i][j] > 0:
                cons[2] = 1
            else:
                cons[2] = 0
            max_cons = max(sum(cons), max_cons)
            max_mult = max(max_mult, t[i][j])
    print(3 - max(max_cons, max_mult))


if __name__ == "__main__":
    main(20)
def main(n):
    # n 表示手牌规模（张数），原算法假设输入为若干麻将牌如 "1m 2m 3p ..."
    # 我们生成一个确定性的长度为 n 的手牌序列
    suits = ['m', 'p', 's']  # 三种花色
    hand = []
    for i in range(n):
        num = (i % 9) + 1          # 牌面 1~9
        suit = suits[(i // 9) % 3] # 花色按组循环
        hand.append(f"{num}{suit}")

    # 以下保留原程序的核心算法逻辑
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
    # print(3 - max(max_cons, max_mult))
    pass
if __name__ == "__main__":
    # 示例：以 n=14（常见麻将手牌规模）运行一次
    main(14)
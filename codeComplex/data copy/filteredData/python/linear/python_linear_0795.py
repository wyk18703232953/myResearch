def main(n):
    # n 控制牌的数量，输入结构为一行若干形如 "1p 9m 3s" 的牌
    # 花色按顺序循环：p, m, s
    suits = ['p', 'm', 's']
    D = []
    for i in range(n):
        num = (i % 9) + 1  # 1~9
        suit = suits[(i // 9) % 3]
        D.append(str(num) + suit)

    s = [0] * 10
    m = [0] * 10
    p = [0] * 10

    for i in D:
        if i[1] == 'p':
            p[int(i[0])] += 1
        elif i[1] == 'm':
            m[int(i[0])] += 1

        else:
            s[int(i[0])] += 1

    need = 3
    for i in range(1, 10):
        need = min(3 - p[i], need)
        need = min(3 - s[i], need)
        need = min(3 - m[i], need)
        if i <= 7:
            tmp = 0
            tmp += min(1, p[i])
            tmp += min(1, p[i + 1])
            tmp += min(1, p[i + 2])
            need = min(3 - tmp, need)
            tmp = 0
            tmp += min(1, m[i])
            tmp += min(1, m[i + 1])
            tmp += min(1, m[i + 2])
            need = min(3 - tmp, need)
            tmp = 0
            tmp += min(1, s[i])
            tmp += min(1, s[i + 1])
            tmp += min(1, s[i + 2])
            need = min(3 - tmp, need)

    # print(need)
    pass
if __name__ == "__main__":
    main(20)
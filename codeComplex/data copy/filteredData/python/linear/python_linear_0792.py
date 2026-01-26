def main(n):
    # Generate deterministic test data based on n
    # We will create 3*n cards cycling through 1-9 and suits m, p, s
    suits = ['m', 'p', 's']
    cards = []
    total_cards = max(1, n * 3)
    for i in range(total_cards):
        rank = (i % 9) + 1
        suit = suits[(i // 9) % 3]
        cards.append(str(rank) + suit)

    lm = [0] * 9
    lp = [0] * 9
    ls = [0] * 9

    for item in cards:
        if item[1] == 'm':
            lm[int(item[0]) - 1] += 1
        elif item[1] == 'p':
            lp[int(item[0]) - 1] += 1

        else:
            ls[int(item[0]) - 1] += 1

    if max(lm) == 3 or max(lp) == 3 or max(ls) == 3:
        # print(0)
        pass
        return

    def seq_checker(li):
        flag = 0
        for i in range(9):
            if flag == 0:
                if li[i] == 1:
                    flag = 1

            else:
                if li[i] == 1:
                    flag += 1

                else:
                    break
        return flag

    if seq_checker(lm) == 3 or seq_checker(lp) == 3 or seq_checker(ls) == 3:
        # print(0)
        pass
    elif max(lm) == 2 or max(lp) == 2 or max(ls) == 2:
        # print(1)
        pass

    else:
        m = 0
        for i in range(0, 7):
            m = max(sum(lm[i:i + 3]), sum(lp[i:i + 3]), sum(ls[i:i + 3]), m)
        # print(3 - m)
        pass
if __name__ == "__main__":
    main(5)
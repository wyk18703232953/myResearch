import random

def main(n: int):
    # 生成规模为 n 的测试数据：n 组麻将牌，每组 3 张
    # 每张牌格式为 "<数字><花色>"，数字 1-9，花色 s/p/m
    suits = ['s', 'p', 'm']
    results = []

    for _ in range(n):
        tiles = []
        for _ in range(3):
            num = random.randint(1, 9)
            suit = random.choice(suits)
            tiles.append(f"{num}{suit}")
        s = ' '.join(tiles)

        # 原逻辑开始
        parts = s.split(' ')

        M = [0] * 9
        P = [0] * 9
        S = [0] * 9

        for pile in parts:
            num = int(pile[0])
            tile = pile[1]

            if tile == 's':
                S[num - 1] += 1
            elif tile == 'p':
                P[num - 1] += 1
            elif tile == 'm':
                M[num - 1] += 1

        # 和牌：刻子（三张一样）或顺子（三张连续） => 输出 0
        for i in range(9):
            if M[i] == 3 or P[i] == 3 or S[i] == 3:
                results.append(0)
                break
        else:
            for i in range(7):
                if ((M[i] == 1 and M[i + 1] == 1 and M[i + 2] == 1) or
                    (P[i] == 1 and P[i + 1] == 1 and P[i + 2] == 1) or
                    (S[i] == 1 and S[i + 1] == 1 and S[i + 2] == 1)):
                    results.append(0)
                    break
            else:
                # 一步听牌：对子或两张相邻/隔一张同花色 => 输出 1
                done = False
                for i in range(9):
                    if M[i] == 2 or P[i] == 2 or S[i] == 2:
                        results.append(1)
                        done = True
                        break

                if not done:
                    for i in range(8):
                        if ((M[i] == 1 and M[i + 1] == 1) or
                            (P[i] == 1 and P[i + 1] == 1) or
                            (S[i] == 1 and S[i + 1] == 1)):
                            results.append(1)
                            done = True
                            break

                if not done:
                    for i in range(7):
                        if ((M[i] == 1 and M[i + 2] == 1) or
                            (P[i] == 1 and P[i + 2] == 1) or
                            (S[i] == 1 and S[i + 2] == 1)):
                            results.append(1)
                            done = True
                            break

                # 否则两步听牌 => 输出 2
                if not done:
                    results.append(2)

    # 输出每组数据对应的结果
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 示例：生成并判断 5 组随机测试数据
    main(5)
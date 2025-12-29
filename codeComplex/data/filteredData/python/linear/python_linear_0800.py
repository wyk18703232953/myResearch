import random

def main(n: int):
    """
    n: 测试规模，这里理解为生成 n 组 3 张牌进行测试。
       每组 3 张牌按原逻辑各自独立处理。
    """
    # 花色列表：m=万, p=饼, s=索（原代码中“else”分支用作第三种花色）
    suits = ['m', 'p', 's']

    for _ in range(n):
        # 生成一组测试数据：3 张麻将牌
        # 牌的格式与原程序一致，例如 "3m", "7p", "9s"
        m = []
        for _ in range(3):
            num = random.randint(1, 9)
            suit = random.choice(suits)
            m.append(f"{num}{suit}")

        # 以下为原逻辑改写（无 input，直接用 m 列表）
        tiles = [[0 for _ in range(9)] for _ in range(3)]
        for i in range(len(m)):
            g = int(m[i][0]) - 1  # 牌面 1-9 转为索引 0-8
            h = m[i][1]           # 花色
            if h == "m":
                tiles[0][g] += 1
            elif h == "p":
                tiles[1][g] += 1
            else:
                tiles[2][g] += 1

        # 输出生成的测试数据（若只想要结果，可注释下一行）
        # print("Input:", *m)

        if m[0] == m[1] and m[1] == m[2]:
            print(0)
        elif m[0] == m[1]:
            print(1)
        elif m[0] == m[2]:
            print(1)
        elif m[1] == m[2]:
            print(1)
        else:
            flag = False
            for i in range(3):
                for j in range(9):
                    if tiles[i][j] != 0:
                        if j != 8 and tiles[i][j + 1] != 0:
                            if j != 7 and tiles[i][j + 2] != 0:
                                print(0)
                                flag = True
                                break
                            else:
                                print(1)
                                flag = True
                                break
                        elif j != 7 and j != 8 and tiles[i][j + 2] != 0:
                            print(1)
                            flag = True
                            break
                if flag:
                    break
            if not flag:
                print(2)


if __name__ == "__main__":
    # 示例：运行 5 组测试
    main(5)
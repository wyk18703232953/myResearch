from math import *
import random

def main(n):
    # n 为生成牌的数量，原逻辑要求至少 3 张
    if n < 3:
        n = 3

    # 牌的花色：万(m)、索(s)、筒(p)
    suits = ['m', 's', 'p']
    # 数字范围 1~9
    numbers = list(range(1, 10))

    # 根据规模 n 生成测试数据：n 张随机牌
    tiles = []
    for _ in range(n):
        num = random.choice(numbers)
        suit = random.choice(suits)
        tiles.append(f"{num}{suit}")

    # 构造原程序的牌桶
    d = {'m': [], 's': [], 'p': []}
    for t in tiles:
        d[t[1]].append(int(t[0]))

    # 为了与原逻辑结果可见，这里先打印生成的测试数据
    print("Tiles:", " ".join(tiles))

    # 按原代码逻辑进行判断
    for k, v in d.items():
        v.sort()
        if len(v) == 3 and len(set(v)) == 1:
            print(0)
            break
        if len(v) == 3 and v[0] + 1 == v[1] and v[1] + 1 == v[2]:
            print(0)
            break
    else:
        for k, v in d.items():
            v.sort()
            if len(v) == 2 and len(set(v)) == 1:
                print(1)
                break
            if len(v) == 2 and v[1] - v[0] <= 2:
                print(1)
                break
            if len(v) == 3 and (v[0] == v[1] or v[1] == v[2]):
                print(1)
                break
            if len(v) == 3 and (v[1] - v[0] <= 2 or v[2] - v[1] <= 2):
                print(1)
                break
        else:
            print(2)


if __name__ == "__main__":
    # 示例运行
    main(3)
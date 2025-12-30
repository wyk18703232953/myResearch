import random

def ism(a, b, c):
    return a == b and b == c

def isk(a, b, c):
    x = [a, b, c]
    x.sort()
    if x[0][1] == x[1][1] and x[1][1] == x[2][1]:
        if int(x[0][0]) + 1 == int(x[1][0]) and int(x[1][0]) + 1 == int(x[2][0]):
            return 1
    return 0

def main(n):
    # 根据 n 生成测试数据：随机生成 3 张牌
    # n 仅用作控制随机性规模（这里简单作为随机种子的一部分）
    random.seed(n)
    suits = ['m', 's', 'p']
    tiles = []
    for _ in range(3):
        val = random.randint(1, 9)
        suit = random.choice(suits)
        tiles.append(f"{val}{suit}")
    a, b, c = tiles
    x = [a, b, c]

    typem = []
    types = []
    typep = []
    m, s, p = 0, 0, 0

    for i in x:
        if i[1] == 'm':
            m += 1
            typem.append(i)
        elif i[1] == 's':
            s += 1
            types.append(i)
        elif i[1] == 'p':
            p += 1
            typep.append(i)

    ans = 0
    done = 0

    if isk(a, b, c) or ism(a, b, c):
        ans = 0
        done = 1

    if done == 0 and a == b and b == c:
        ans = 0
        done = 1

    elif done == 0 and a == b:
        ans = 1
        done = 1

    elif done == 0 and b == c:
        ans = 1
        done = 1
    elif done == 0 and a == c:
        ans = 1
        done = 1

    # Shuntsu
    if done == 0 and m >= 2:
        typem.sort()
        for i in range(len(typem) - 1):
            if abs(int(typem[i][0]) - int(typem[i + 1][0])) <= 2 and \
               abs(int(typem[i][0]) - int(typem[i + 1][0])) > 0:
                ans = 1
                done = 1

    if done == 0 and s >= 2:
        types.sort()
        for i in range(len(types) - 1):
            if abs(int(types[i][0]) - int(types[i + 1][0])) <= 2 and \
               abs(int(types[i][0]) - int(types[i + 1][0])) > 0:
                ans = 1
                done = 1

    if done == 0 and p >= 2:
        typep.sort()
        for i in range(len(typep) - 1):
            if abs(int(typep[i][0]) - int(typep[i + 1][0])) <= 2 and \
               abs(int(typep[i][0]) - int(typep[i + 1][0])) > 0:
                ans = 1
                done = 1

    if done == 0:
        ans = 2
        done = 1

    print(ans)

if __name__ == "__main__":
    main(10)
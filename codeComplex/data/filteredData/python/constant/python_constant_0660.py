import random

def main(n):
    # 生成 3 个点，坐标范围根据 n 缩放（0 ~ n 之间）
    l = []
    for _ in range(3):
        a = random.randint(0, n)
        b = random.randint(0, n)
        l.append((a, b))

    # 原逻辑开始
    l.sort()
    path = []
    path.append(l[0])
    x = l[0][0]
    while x < l[1][0]:
        path.append((x, l[0][1]))
        x = x + 1

    up = False
    if l[0][1] < l[1][1]:
        up = True
    if up:
        y = l[0][1]
        while y <= l[1][1]:
            path.append((l[1][0], y))
            y = y + 1
    else:
        y = l[0][1]
        while y >= l[1][1]:
            path.append((l[1][0], y))
            y = y - 1

    up = False
    if l[1][1] < l[2][1]:
        up = True
    if up:
        y = l[1][1]
        while y <= l[2][1]:
            path.append((l[1][0], y))
            y = y + 1
    else:
        y = l[1][1]
        while y >= l[2][1]:
            path.append((l[1][0], y))
            y = y - 1

    x = l[1][0]
    while x < l[2][0]:
        path.append((x, l[2][1]))
        x = x + 1

    path.append(l[2])
    path = list(set(path))

    print(len(path))
    for i in range(len(path)):
        print(str(path[i][0]) + " " + str(path[i][1]))


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)
import random

def main(n):
    # 随机生成一个 n x n 的字符矩阵，其中有一个或多个连续的 'B' 区域
    m = n
    li = [['W' for _ in range(m)] for _ in range(n)]

    # 随机生成一个矩形区域填充 'B'
    top = random.randint(0, n - 1)
    bottom = random.randint(top, n - 1)
    left = random.randint(0, m - 1)
    right = random.randint(left, m - 1)

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            li[i][j] = 'B'

    # 以下为原逻辑（寻找 'B' 区域的中心位置）
    for j in range(m):
        flag = False
        for i in range(n):
            if li[i][j] == "B":
                flag = True
                position1 = i
                break
        if flag:
            break

    for j in range(m - 1, -1, -1):
        flag = False
        for i in range(n - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position2 = i
                break
        if flag:
            break

    for i in range(n):
        flag = False
        for j in range(m):
            if li[i][j] == "B":
                flag = True
                position3 = j
                break
        if flag:
            break

    for i in range(n - 1, -1, -1):
        flag = False
        for j in range(m - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position4 = j
                break
        if flag:
            break

    avg1 = (position1 + position2) // 2 + 1
    avg2 = (position3 + position4) // 2 + 1
    print(avg1, avg2)

if __name__ == "__main__":
    # 示例调用：可根据需要改动 n
    main(5)
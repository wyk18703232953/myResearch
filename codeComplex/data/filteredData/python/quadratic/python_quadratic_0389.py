import random

def main(n):
    # 随机生成一个 n x n 的矩阵，里面有一个或多个连续的 'B' 组成的矩形
    m = n
    # 初始化为全 'W'
    li = [['W' for _ in range(m)] for _ in range(n)]

    # 随机生成一个非空的矩形区域 [top, bottom] x [left, right] 填充 'B'
    top = random.randint(0, n - 1)
    bottom = random.randint(top, n - 1)
    left = random.randint(0, m - 1)
    right = random.randint(left, m - 1)

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            li[i][j] = 'B'

    # 以下逻辑与原程序一致，只是去掉了 input()
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
    # 示例：以 n=5 运行
    main(5)
import random

def main(n: int):
    # 生成一个 n 行、m 列的随机棋盘，其中包含一段连续的 'B'
    # 为保持逻辑，令 m 与 n 相同，也可根据需要调整
    m = n

    # 初始化全为 '.'
    a = [['.' for _ in range(m)] for _ in range(n)]

    # 随机选择某一行和一段连续的 B
    row = random.randint(0, n - 1)
    if m == 1:
        start_col = 0
        length = 1
    else:
        start_col = random.randint(0, m - 1)
        length = random.randint(1, m - start_col)
    for c in range(start_col, start_col + length):
        a[row][c] = 'B'

    # 以下逻辑为原程序的主体，无 input()，直接使用生成的 a, n, m
    temp = 0
    pos1 = 0
    pos2 = 0

    for i in range(n):
        ok = False
        for j in range(m):
            if a[i][j] == "B":
                pos1 = i
                pos2 = j
                temp += 1
                temp2 = j
                if j != m - 1:
                    ok = True
                    while True:
                        ok2 = False
                        if temp2 == m - 1:
                            ok2 = True
                            break
                        if a[i][temp2 + 1] != "B":
                            ok2 = True
                            break
                        temp += 1
                        temp2 += 1
                elif j == m - 1:
                    temp = 1
                    ok = True
                    break
                if ok2:
                    break
        if ok:
            break

    # 输出结果
    print(temp // 2 + pos1 + 1, temp // 2 + pos2 + 1)


# 简单示例：当以脚本运行时，给一个默认的 n
if __name__ == "__main__":
    main(5)
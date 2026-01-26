from math import inf

def main(n):
    # n 作为矩阵规模，生成 n x n 的矩阵
    # 构造一个确定性的 'B' 区域：从 (n//4, n//4) 到 (3n//4, 3n//4)
    m = n
    li = []
    for i in range(n):
        row = []
        for j in range(m):
            if n == 0:
                ch = 'W'

            else:
                if n // 4 <= i <= 3 * n // 4 and n // 4 <= j <= 3 * n // 4:
                    ch = 'B'

                else:
                    ch = 'W'
            row.append(ch)
        li.append(row)

    min1 = inf
    min2 = inf
    max1 = -inf
    max2 = -inf
    for i in range(n):
        for j in range(m):
            if li[i][j] == "B":
                min1 = min(min1, i)
                min2 = min(min2, j)
                max1 = max(max1, i)
                max2 = max(max2, j)
    if min1 is inf:
        # 若没有 'B'，保持行为确定，这里输出 (1, 1)
        x, y = 1, 1

    else:
        x = (min1 + max1) // 2 + 1
        y = (min2 + max2) // 2 + 1
    # print(x, y)
    pass
if __name__ == "__main__":
    main(10)
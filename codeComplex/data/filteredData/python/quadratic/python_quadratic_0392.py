from math import inf

def main(n):
    # 设定矩阵为 n 行 n 列
    rows = n
    cols = n
    li = []
    # 构造一个确定性的包含若干 'B' 的矩阵
    for i in range(rows):
        row = []
        for j in range(cols):
            # 在一个中心十字区域放置 'B'，其余为 '.'
            if rows > 0 and cols > 0 and (i == rows // 2 or j == cols // 2):
                row.append('B')

            else:
                row.append('.')
        li.append(row)

    min1 = inf
    min2 = inf
    max1 = -inf
    max2 = -inf

    for i in range(rows):
        for j in range(cols):
            if li[i][j] == "B":
                if i < min1:
                    min1 = i
                if j < min2:
                    min2 = j
                if i > max1:
                    max1 = i
                if j > max2:
                    max2 = j

    # 若没有 'B'，为保持行为确定，输出 (1, 1)
    if min1 == inf:
        # print(1, 1)
        pass

    else:
        # print((min1 + max1) // 2 + 1, (min2 + max2) // 2 + 1)
        pass
if __name__ == "__main__":
    main(5)
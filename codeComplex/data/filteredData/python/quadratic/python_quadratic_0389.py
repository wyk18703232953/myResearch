def main(n):
    # 映射规模：n -> n x n 的矩阵
    # 构造一个确定性的 n x n 矩阵，包含一段连续的 'B' 区域
    m = n
    li = []
    for i in range(n):
        row = []
        for j in range(m):
            # 简单确定性规则：在中间的一个子矩形中放 'B'，其他为 'W'
            # 子矩形大小与 n 线性相关
            top = n // 4
            bottom = n - 1 - n // 4
            left = m // 4
            right = m - 1 - m // 4
            if top <= i <= bottom and left <= j <= right:
                row.append('B')

            else:
                row.append('W')
        li.append(row)

    # 以下为原始算法逻辑（不依赖输入）
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
    # print(avg1, avg2)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)
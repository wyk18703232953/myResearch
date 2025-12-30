import random

def main(n):
    # 这里约定生成一个 n 行 n 列 的网格
    m = n

    # 根据 n 生成测试数据：随机由 '.' 和 '#' 构成的网格
    arr = []
    for _ in range(n):
        row = ''.join(random.choice(['.', '#']) for _ in range(m))
        arr.append(row)

    # arr1 用于标记由特定“十字形”模式覆盖到的 '#'
    arr1 = [[0] * m for _ in range(n)]

    # 检测模式：
    # ###
    # #.#
    # ###
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#' and i < n - 2 and j < m - 2:
                if (arr[i][j + 1] == '#' and
                    arr[i][j + 2] == '#' and
                    arr[i + 1][j] == '#' and
                    arr[i + 2][j] == '#' and
                    arr[i + 2][j + 1] == '#' and
                    arr[i + 2][j + 2] == '#' and
                    arr[i + 1][j + 2] == '#'):
                    arr1[i][j] = 1
                    arr1[i + 1][j] = 1
                    arr1[i + 2][j] = 1
                    arr1[i + 2][j + 1] = 1
                    arr1[i + 2][j + 2] = 1
                    arr1[i + 1][j + 2] = 1
                    arr1[i][j + 1] = 1
                    arr1[i][j + 2] = 1

    flag = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "#" and arr1[i][j] == 0:
                flag = 1
                break
        if flag == 1:
            break

    # 输出原始随机网格，方便查看测试数据
    for row in arr:
        print(row)

    # 输出结果
    if flag == 1:
        print("NO")
    else:
        print("YES")
import random

def fun(grid, counter, n, m):
    for i in range(n):
        possible = True
        for j in range(m):
            if grid[i][j] == '1' and counter[j] == 1:
                possible = False
                break
        if possible:
            return True
    return False

def main(n):
    # 生成规模为 n 的测试数据
    # 这里令列数 m 与 n 相同，也可以根据需要修改为其他函数关系
    m = n

    grid = []
    counter = [0] * m

    # 随机生成由 '0' 和 '1' 组成的 n 行 m 列矩阵
    for _ in range(n):
        row = ''.join(random.choice('01') for _ in range(m))
        grid.append(row)
        for i in range(m):
            if row[i] == '1':
                counter[i] += 1

    if fun(grid, counter, n, m):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)
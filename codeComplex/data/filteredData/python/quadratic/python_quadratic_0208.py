import random

def main(n: int):
    # 生成一个 n 行 m 列的随机 01 矩阵，m 可根据需要设定
    m = max(1, n)  # 简单设置：列数等于行数，且至少为 1
    grid = []
    for _ in range(n):
        row = ''.join(random.choice('01') for _ in range(m))
        grid.append(row)

    cnts = [0 for _ in range(m)]
    for i in range(n):
        for j in range(m):
            cnts[j] += 0 if grid[i][j] == '0' else 1

    for i in range(n):
        flag = True
        for j in range(m):
            if grid[i][j] == '1' and cnts[j] == 1:
                flag = False
                break
        if flag:
            print('YES')
            return
    print('NO')


if __name__ == "__main__":
    # 示例：调用 main(5) 进行一次运行
    main(5)
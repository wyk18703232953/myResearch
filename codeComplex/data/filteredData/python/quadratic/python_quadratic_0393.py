import random

def main(n: int):
    # 生成一个 n x n 的网格，随机选择一段连续的 'B'
    m = n  # 这里假设为正方形网格，原代码未使用 m

    grid = []
    chosen_row = random.randint(0, n - 1)
    length = random.randint(1, m)          # 'B' 段长度
    start_col = random.randint(0, m - length)

    for i in range(n):
        if i == chosen_row:
            row = ['.'] * m
            for j in range(start_col, start_col + length):
                row[j] = 'B'
            grid.append(''.join(row))
        else:
            grid.append('.' * m)

    # 以下为原逻辑的封装，不使用 input()
    lock = 0
    Ccen = 0
    Rcen = 0
    for i in range(n):
        s = grid[i]
        if ('B' in s) and (lock == 0):
            Rstart = s.index('B')
            cnt = s.count('B')
            Rcen = Rstart + (cnt // 2)
            Cstart = i
            Ccen = Cstart + (cnt // 2)
            lock = 1

    print(Ccen + 1, Rcen + 1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
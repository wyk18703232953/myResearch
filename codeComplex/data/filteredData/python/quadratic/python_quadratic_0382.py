import random
import string

def main(n):
    # 随机生成一个 n 行 m 列的字符网格，并在其中放置一段连续的 'B'
    # 保证至少有一行包含 'B'
    m = max(1, n)  # 简单设定 m 与 n 同阶，也可按需调整
    grid = []

    # 随机选择一行放置 B 段
    b_row = random.randint(0, n - 1)
    # 随机决定该行 B 段长度（至少 1，且不超过 m）
    b_len = random.randint(1, m)
    # 随机决定 B 段起始位置
    b_start = random.randint(0, m - b_len)

    for i in range(n):
        if i == b_row:
            row = ['.'] * m
            for j in range(b_start, b_start + b_len):
                row[j] = 'B'
            grid.append(''.join(row))
        else:
            # 其他行随机生成不含 B 的字符
            row = [random.choice(string.ascii_uppercase.replace('B', '')) for _ in range(m)]
            grid.append(''.join(row))

    # 以下为原逻辑的封装，使用生成的 grid 代替输入
    r = 0
    c = 0
    f = 1
    for i in range(n):
        s = grid[i]
        if f and "B" in s:
            f = 0
            ci = s.index('B')
            cc = s.count("B")
            r = i + 1 + cc // 2
            c = ci + cc // 2 + 1

    print(r, c)
    return r, c, grid  # 若只需输出，可去掉 return
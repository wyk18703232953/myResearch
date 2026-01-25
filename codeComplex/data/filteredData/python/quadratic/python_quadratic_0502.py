def isValid(field, y, x):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            if field[y + i][x + j] == '.':
                return False
    return True

def fill(field, y, x, cur):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            cur[y + i][x + j] = '#'

def main(n):
    # 解释规模含义：
    # 将输入规模 n 映射为一个近似为正方形的网格大小 n = rows * cols
    # rows = n // 2, cols = n - rows，保证 rows, cols >= 1
    if n <= 0:
        return
    rows = max(1, n // 2)
    cols = max(1, n - rows)

    # 构造一个确定性的 sig 矩阵，元素为 '.' 或 '#'
    # 规则：若 (i + j) % 3 == 0 则为 '#', 否则 '.'
    sig = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i + j) % 3 == 0:
                row.append('#')
            else:
                row.append('.')
        sig.append(row)

    # 初始 cur 为全 '.' 的矩阵
    cur = [["."] * cols for _ in range(rows)]

    # 在 sig 上应用原算法逻辑
    if rows >= 3 and cols >= 3:
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isValid(sig, i, j):
                    fill(sig, i, j, cur)

    if sig == cur:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main(10)
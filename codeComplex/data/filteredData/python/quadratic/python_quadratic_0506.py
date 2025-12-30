import random

def main(n):
    # 为了保持原逻辑，构造一个 n 行 m 列的字符网格，元素为 '#' 或 '.'
    # 这里令 m = n，生成一个 n x n 的随机网格
    m = n
    u = []
    u1 = []
    for _ in range(n):
        row = [random.choice(['#', '.']) for _ in range(m)]
        u.append(row)
        u1.append(['.'] * m)

    # 原有逻辑：在 u 中寻找特定形状的 '#' 图案，并在 u1 中“画”出该图案
    for i in range(n - 2):
        for j in range(m - 2):
            ok = True
            for k in range(3):
                if u[i][j + k] != '#' or u[i + k][j] != '#':
                    ok = False
                    break
            if ok:
                if (u[i + 2][j + 1] != '#' or
                    u[i + 2][j + 2] != '#' or
                    u[i + 1][j + 2] != '#'):
                    ok = False
                else:
                    for k in range(3):
                        u1[i][j + k] = '#'
                        u1[i + k][j] = '#'
                    u1[i + 2][j + 1] = '#'
                    u1[i + 2][j + 2] = '#'
                    u1[i + 1][j + 2] = '#'

    # 比较 u 与 u1 是否完全一致
    ok = True
    for i in range(n):
        for j in range(m):
            if u[i][j] != u1[i][j]:
                ok = False
                break
        if not ok:
            break

    if ok:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)
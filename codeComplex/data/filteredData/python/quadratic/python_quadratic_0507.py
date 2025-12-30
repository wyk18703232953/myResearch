import random

def main(n):
    # 生成一个 n 行 n 列的随机网格，包含 '#' 和 '.'
    m = n
    s = []
    st = set()
    cst = set()

    # 简单生成测试数据：每个位置以 50% 概率为 '#'
    for i in range(n):
        row = ''.join(random.choice(['#', '.']) for _ in range(m))
        s.append(row)
        for j, ch in enumerate(row):
            if ch == '#':
                st.add((i, j))

    # 按原逻辑检查由 3x3 全 '#' 组成的“星型”能覆盖的点
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if s[i - 1][j - 1] != '#':
                continue
            if s[i - 1][j] != '#':
                continue
            if s[i - 1][j + 1] != '#':
                continue
            if s[i][j - 1] != '#':
                continue
            if s[i][j + 1] != '#':
                continue
            if s[i + 1][j - 1] != '#':
                continue
            if s[i + 1][j] != '#':
                continue
            if s[i + 1][j + 1] != '#':
                continue
            cst.add((i - 1, j))
            cst.add((i - 1, j - 1))
            cst.add((i - 1, j + 1))
            cst.add((i + 1, j))
            cst.add((i + 1, j - 1))
            cst.add((i + 1, j + 1))
            cst.add((i, j + 1))
            cst.add((i, j - 1))

    # 输出生成的测试数据（方便调试，可按需删除）
    for row in s:
        print(row)

    # 输出判断结果
    if len(cst) == len(st):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)
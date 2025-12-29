import random

mod = 10 ** 9 + 7
INF = float('inf')


def main(n: int):
    # 生成测试数据：n 行，m 列（这里令 m = n，必要可自行调整）
    m = n

    # 生成一个 n x m 的 0/1 矩阵（字符）
    # 保证至少有一行不是“必需行”（否则结果必然为 NO，测试不全面）
    s = []
    for _ in range(n):
        row = [random.choice(['0', '1']) for _ in range(m)]
        # 避免全 0 行导致所有灯计数为 0 时测试无意义，可适当强制至少一个 1
        if all(c == '0' for c in row):
            row[random.randrange(m)] = '1'
        s.append(row)

    # 统计每列的 ‘1’ 数量
    lampcnt = [0] * m
    for i in range(n):
        for j in range(m):
            if s[i][j] == '1':
                lampcnt[j] += 1

    # 判定是否存在一行 i，使得对所有灯 j，
    # 若该灯只被这一行点亮（lampcnt[j] == 1），则该行在该灯上是“唯一”的；
    # 原代码含义：是否存在一行不是对某个灯“唯一负责”的（即删去该行后仍有解）
    res = False
    for i in range(n):
        only = False
        for j in range(m):
            if s[i][j] == '1' and lampcnt[j] == 1:
                only = True
        if not only:
            res = True

    # 输出与原程序一致
    print('YES' if res else 'NO')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
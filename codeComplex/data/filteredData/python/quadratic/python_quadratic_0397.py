import random

def main(n):
    # 生成一个 n x n 的矩阵，随机放置若干个 'B'，保证至少有一个 'B'
    m = n  # 原题中 n, m 可不同，这里用方阵；如需长方形可自行修改
    M = [['0' for _ in range(m)] for _ in range(n)]

    # 随机生成若干个 'B' 的位置
    k = random.randint(1, max(1, n * m // 4))  # 随机放 1 到 n*m//4 个 B
    positions = set()
    while len(positions) < k:
        a = random.randrange(n)
        b = random.randrange(m)
        positions.add((a, b))
    for a, b in positions:
        M[a][b] = 'B'

    # 以下为原逻辑（去掉 input），在矩阵 M 上操作
    start = []
    end = []
    for a in range(n):
        for b in range(m):
            if M[a][b] == 'B':
                if not start:
                    start.append(a + 1)
                    start.append(b + 1)
                else:
                    end.clear()
                    end.append(a + 1)
                    end.append(b + 1)

    if not start or not end:
        print(start[0], start[1])
    else:
        mid1 = int((end[0] + start[0]) / 2)
        mid2 = int((end[1] + start[1]) / 2)
        print(mid1, mid2)
import random

def main(n):
    # 随机生成一个 n x n 的棋盘，'*' 和 '.' 混合
    m = n
    # 控制密度，可根据需要调整，比如 0.3 星号密度
    density = 0.3
    board = [
        ''.join('*' if random.random() < density else '.' for _ in range(m))
        for _ in range(n)
    ]

    # 原逻辑开始：把 board 当作输入读入
    w = [c == '*' for i in range(n) for c in board[i]]
    nm = n * m
    q = [
        *[range(i, i + m) for i in range(0, nm, m)],  # 每一行
        *[range(i, nm, m) for i in range(m)]          # 每一列
    ]
    e = [1000] * nm

    # 第一轮扫描
    for f in (True, False):
        for r in q:
            v = 0
            for i in r:
                if w[i]:
                    v += 1
                    if e[i] > v:
                        e[i] = v
                else:
                    v = e[i] = 0
        if f:
            w.reverse()
            e.reverse()

    e = [c if c != 1 else 0 for c in e]

    # 第二轮扫描
    for f in (True, False):
        for r in q:
            v = 0
            for i in r:
                if v > e[i]:
                    v -= 1
                else:
                    v = e[i]
                if v:
                    w[i] = False
        if f:
            w.reverse()
            e.reverse()

    # 输出结果
    if any(w):
        print(-1)
    else:
        r = []
        for i, c in enumerate(e):
            if c:
                r.append(f'{i // m + 1} {i % m + 1} {c - 1}')
        print(len(r), '\n'.join(r), sep='\n')


# 示例：运行规模为 5 的测试
if __name__ == "__main__":
    main(5)
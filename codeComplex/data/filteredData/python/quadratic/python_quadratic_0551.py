def main(n):
    # 根据规模 n 构造一个 n 行 (1..n) 的棋盘，列数 m = n
    # 原逻辑：在 n*m 的网格上交替从左上到右下、右下到左上输出所有格子一次
    m = n
    ans = []
    moves = n * m
    c1 = [1, 1]
    c2 = [n, m]
    p = 0
    while moves > 0:
        if p % 2 == 0:
            ans.append(tuple(c1))
            c1[1] += 1
            if c1[1] > m:
                c1[0] += 1
                c1[1] = 1
        else:
            ans.append(tuple(c2))
            c2[1] -= 1
            if c2[1] < 1:
                c2[0] -= 1
                c2[1] = m
        moves -= 1
        p += 1
    for i in ans:
        print(*i)


if __name__ == "__main__":
    # 简单测试：使用 n = 3 作为示例规模
    main(3)
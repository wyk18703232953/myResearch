import random

def main(n: int):
    # n 作为规模参数，用来生成 t（测试组数）和棋盘大小、矩形范围等
    # 这里示例：t = n，棋盘大小和矩形坐标按 n 相关规则随机生成
    t = n

    for _ in range(t):
        # 生成棋盘大小 n * m，限定在 [1, 2n] 范围，可以按需调整
        N = random.randint(1, max(1, 2 * n))
        M = random.randint(1, max(1, 2 * n))

        # 生成第一个矩形 (x1, y1, x2, y2)
        x1 = random.randint(1, N)
        x2 = random.randint(x1, N)
        y1 = random.randint(1, M)
        y2 = random.randint(y1, M)

        # 生成第二个矩形 (x3, y3, x4, y4)
        x3 = random.randint(1, N)
        x4 = random.randint(x3, N)
        y3 = random.randint(1, M)
        y4 = random.randint(y3, M)

        # 原始逻辑开始
        count_w = N * M // 2 + N * M % 2
        count_g = N * M // 2

        area1 = (x2 - x1 + 1) * (y2 - y1 + 1)
        area2 = (x4 - x3 + 1) * (y4 - y3 + 1)

        if (x1 + y1) % 2 == 0:
            count_g -= area1 // 2
            count_w += area1 // 2
        else:
            count_g -= area1 // 2 + area1 % 2
            count_w += area1 // 2 + area1 % 2

        x5 = max(x1, x3)
        x6 = min(x4, x2)
        y5 = max(y1, y3)
        y6 = min(y4, y2)

        if (x3 + y3) % 2 == 1:
            count_g += area2 // 2
            count_w -= area2 // 2
        else:
            count_g += area2 // 2 + area2 % 2
            count_w -= area2 // 2 + area2 % 2

        if x5 <= x6 and y5 <= y6:
            area3 = (x6 - x5 + 1) * (y6 - y5 + 1)
            if (x5 + y5) % 2 == 0:
                count_g += area3 // 2
                count_w -= area3 // 2
            else:
                count_g += area3 // 2 + area3 % 2
                count_w -= area3 // 2 + area3 % 2

        print(count_w, count_g)


if __name__ == "__main__":
    # 示例运行：规模 n = 5
    main(5)
import random

def main(n):
    # 生成测试数据：n 行、m 列的 0/1 矩阵
    # 这里设定 m = n（可按需要修改生成策略）
    m = n
    a = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]

    ignorable = [True] * n

    for i in range(m):
        cnt = 0
        for j in range(n):
            cnt += a[j][i]
        if cnt == 1:
            for j in range(n):
                if a[j][i]:
                    ignorable[j] = False

    if any(ignorable):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改 n
    main(5)
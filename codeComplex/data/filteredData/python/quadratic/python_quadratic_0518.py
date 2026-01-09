def main(n):
    # 根据规模 n 生成一个 n x n 的随机测试棋盘
    # 使用简单确定性模式而非真正随机，保证复现性
    m = n
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    dp2 = [[-1 for _ in range(m)] for _ in range(n)]

    # 生成测试数据：
    # 对每个 3x3 子块，其中心是 '.'，周围是 '#'
    # 这样能触发算法标记 dp2 的逻辑
    for i in range(n):
        for j in range(m):
            # 判断是否为某个 3x3 块的中心
            if 1 <= i < n - 1 and 1 <= j < m - 1 and (i % 3 == 1) and (j % 3 == 1):
                dp[i][j] = '.'  # 中心空

            else:
                dp[i][j] = '#'  # 其余填 '#'

    # 模拟原程序从输入读入棋盘后的处理
    # dp 已经是字符矩阵形式，无需再转换 -1，这里按原逻辑走即可

    for i in range(0, n - 2):
        for j in range(0, m - 2):
            p = 0
            c = 0
            for k in range(i, i + 3):
                for h in range(j, j + 3):
                    p += 1
                    if p != 5:
                        if dp[k][h] == '#':
                            c += 1

            if c == 8:
                p = 0
                for k in range(i, i + 3):
                    for h in range(j, j + 3):
                        p += 1
                        if p != 5:
                            dp2[k][h] = '#'

    if dp == dp2:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # 示例：调用 main(9) 进行测试
    main(9)
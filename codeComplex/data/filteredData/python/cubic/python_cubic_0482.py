def main(n):
    # 映射 n 为网格大小与步数：n 越大，网格越大、K 越大
    # 这里选择一个简单且确定性的规则：
    # 行列规模随 n 增长，K 为偶数以避免全部输出 -1
    rows = max(1, n // 3)
    cols = max(1, n // 4)
    # 保证 K 为偶数且至少为 2
    K = max(2, (n // 2) * 2)

    # 构造 wh 与 wv，使用简单算术保证确定性
    wh = [[0] * cols for _ in range(rows)]
    wv = [[0] * cols for _ in range(rows)]

    # 模拟原输入结构：
    # 第一部分：n 行，每行 m-1 个整数 -> wh 的前 m-1 列
    for i in range(rows):
        # 构造长度 m-1 的行，值依赖 i、j、n 确定
        t = [(i * 7 + j * 5 + n) % 9 + 1 for j in range(cols - 1)] if cols > 1 else []
        for j in range(cols - 1):
            wh[i][j] = t[j]

    # 第二部分：n-1 行，每行 m 个整数 -> wv 的前 n-1 行
    for i in range(rows - 1):
        t = [(i * 11 + j * 3 + n) % 9 + 1 for j in range(cols)]
        for j in range(cols):
            wv[i][j] = t[j]

    INF = int(1e8)
    # 原代码中 f 第三维固定为 11，保持不变
    f = [[[INF] * 11 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            f[i][j][0] = 0

    halfK = K // 2
    for k in range(1, halfK + 1):
        for i in range(rows):
            for j in range(cols):
                if i > 0:
                    f[i][j][k] = min(f[i][j][k], f[i - 1][j][k - 1] + wv[i - 1][j])
                if j < cols - 1:
                    f[i][j][k] = min(f[i][j][k], f[i][j + 1][k - 1] + wh[i][j])
                if i < rows - 1:
                    f[i][j][k] = min(f[i][j][k], f[i + 1][j][k - 1] + wv[i][j])
                if j > 0:
                    f[i][j][k] = min(f[i][j][k], f[i][j - 1][k - 1] + wh[i][j - 1])

    # 按原逻辑输出每个单元格的答案
    for i in range(rows):
        row_ans = []
        for j in range(cols):
            if K % 2 == 1:
                row_ans.append("-1")

            else:
                dp = [INF] * (halfK + 1)
                dp[0] = 0
                for k in range(1, halfK + 1):
                    for l in range(0, k):
                        dp[k] = min(dp[k], dp[l] + f[i][j][k - l] * 2)
                row_ans.append(str(dp[halfK]))
        # print(" ".join(row_ans))
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以进行规模实验
    main(20)
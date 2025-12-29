import random

def main(n):
    # n 是规模，用于生成每个颜色数量
    # 为了适配原逻辑需要三个数 n[0], n[1], n[2]
    # 若传入为单个整数，则平均拆成三部分
    if isinstance(n, int):
        a = n // 3
        b = (n - a) // 2
        c = n - a - b
        n = [a, b, c]
    elif isinstance(n, (list, tuple)) and len(n) == 3:
        n = list(n)
    else:
        raise ValueError("n 必须是整数或长度为 3 的列表/元组")

    # 生成测试数据：三组正整数
    u = []
    for size in n:
        # 生成范围可根据需要调整
        u.append([random.randint(1, 1000) for _ in range(size)])

    # 与原程序一致的处理逻辑
    u[0].sort(reverse=True)
    u[1].sort(reverse=True)
    u[2].sort(reverse=True)

    dp = [[[0] * (n[2] + 1) for _ in range(n[1] + 1)] for _ in range(n[0] + 1)]

    for i in range(n[0] + 1):
        for j in range(n[1] + 1):
            for k in range(n[2] + 1):
                cur = dp[i][j][k]
                if i < n[0] and j < n[1]:
                    val = cur + u[0][i] * u[1][j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if j < n[1] and k < n[2]:
                    val = cur + u[1][j] * u[2][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if i < n[0] and k < n[2]:
                    val = cur + u[0][i] * u[2][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val

    res = max(x for u1 in dp for u2 in u1 for x in u2)
    print(res)
    return res

# 示例：当直接运行本文件时，执行一次 main
if __name__ == "__main__":
    main(9)
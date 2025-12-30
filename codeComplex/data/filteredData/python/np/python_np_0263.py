from decimal import Decimal, getcontext
import random

def main(n: int):
    # 设置精度（保留小数的计算精度）
    getcontext().prec = 28

    # 生成测试数据：n x n 的矩阵，元素为 [0,1) 的浮点数
    # 原代码使用 float 读入，这里也用 float 即可
    ar = [[random.random() for _ in range(n)] for _ in range(n)]

    # 初始化 DP 数组
    # 原代码中 dp 大小固定为 [18][1<<18]，这里根据 n 自适应
    dp = [[0.0 for _ in range(1 << n)] for _ in range(n)]

    ans = 0.0
    # 初始状态：所有人都在集合中，起点 0 的概率为 1
    dp[0][(1 << n) - 1] = 1.0

    # 状态压缩 DP
    for i in range((1 << n) - 1, 0, -1):
        for j in range(n):
            if i & (1 << j) == 0:
                continue
            for k in range(n):
                if i & (1 << k) != 0 or j == k:
                    continue
                dp[j][i] = max(
                    dp[j][i],
                    dp[k][i ^ (1 << k)] * ar[k][j] +
                    dp[j][i ^ (1 << k)] * ar[j][k]
                )

    for i in range(n):
        ans = max(ans, dp[i][1 << i])

    print('{:.6f}'.format(ans))


if __name__ == "__main__":
    # 示例：调用 main(3)，可根据需要修改 n
    main(3)
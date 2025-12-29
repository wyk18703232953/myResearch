from math import inf
import random

mod = 10**9 + 7
mod2 = 998244353

def l1d(n, val=0):
    return [val for _ in range(n)]

def l2d(n, m, val=0):
    return [l1d(m, val) for _ in range(n)]

def main(n):
    # 生成测试数据：
    # 将原来的 n, m, k 都与规模参数 n 相关联
    # 这里设置 m = n，k = 2*n（保持偶数以产生非全 -1 输出）
    m = n
    k = 2 * n

    # 生成随机的边权，范围可自行调整
    # hor: n 行，每行 m-1 个数字
    hor = []
    for _ in range(n):
        row = [random.randint(1, 10) for _ in range(m - 1)]
        hor.append(row)

    # ver: n-1 行，每行 m 个数字
    ver = []
    for _ in range(n - 1):
        row = [random.randint(1, 10) for _ in range(m)]
        ver.append(row)

    # 算法主体
    if k % 2:
        ml = l2d(n, m, -1)
        for row in ml:
            print(*row)
        return

    k //= 2
    dp = [l2d(n, m) for _ in range(k + 1)]

    for f in range(1, k + 1):
        for i in range(n):
            for j in range(m):
                a = inf
                if i != 0:
                    a = min(a, 2 * ver[i - 1][j] + dp[f - 1][i - 1][j])
                if i != n - 1:
                    a = min(a, 2 * ver[i][j] + dp[f - 1][i + 1][j])
                if j != 0:
                    a = min(a, 2 * hor[i][j - 1] + dp[f - 1][i][j - 1])
                if j != m - 1:
                    a = min(a, 2 * hor[i][j] + dp[f - 1][i][j + 1])
                dp[f][i][j] = a

    for row in dp[-1]:
        print(*row)


if __name__ == "__main__":
    # 示例调用：规模 n = 4
    main(4)
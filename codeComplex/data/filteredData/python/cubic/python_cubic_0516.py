import random


def main(n):
    # 生成规模参数
    # 为了可控，这里让 m 和 n 相同，也可以根据需要调整生成规则
    m = n
    # k 设为一个偶数步数（若想测试 -1 分支，可改为奇数）
    k = 4

    # 生成测试数据：a 为 n x m，b 为 (n-1) x m
    # 数值范围可根据需要调整
    max_val = 10
    a = [[random.randint(1, max_val) for _ in range(m)] for _ in range(n)]
    if n > 1:
        b = [[random.randint(1, max_val) for _ in range(m)] for _ in range(n - 1)]
    else:
        b = []

    # 以下为原始逻辑的封装，无 input()
    if k % 2 == 1:
        for _ in range(n):
            print(" ".join(["-1"] * m))
    else:
        half_k = k // 2
        pre = [[0 for _ in range(m)] for _ in range(n)]
        for _ in range(half_k):
            curr = [[float("inf") for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if j > 0:
                        curr[i][j] = min(curr[i][j], pre[i][j - 1] + a[i][j - 1])
                    if i < n - 1:
                        curr[i][j] = min(curr[i][j], pre[i + 1][j] + b[i][j])
                    if j < m - 1:
                        curr[i][j] = min(curr[i][j], pre[i][j + 1] + a[i][j])
                    if i > 0:
                        curr[i][j] = min(curr[i][j], pre[i - 1][j] + b[i - 1][j])
            pre = curr
        for i in range(n):
            print(" ".join(str(2 * pre[i][j]) for j in range(m)))


if __name__ == "__main__":
    # 示例：调用 main(5) 进行一次运行
    main(5)
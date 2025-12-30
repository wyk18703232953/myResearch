import random

def main(n):
    # 生成测试数据：随机选择 k，满足 k*(k+1)//2 - (k-1)*k//2 >= n 的大致规模
    # 这里简单取 k 为与 n 同数量级的随机数
    if n <= 0:
        print(-1)
        return

    # 让 k 在 [1, 2n] 区间内随机生成
    k = random.randint(1, max(1, 2 * n))

    # 原逻辑开始
    n_adj, k_adj = n - 1, k - 1

    l = 0
    r = k_adj
    g = k_adj * (k_adj + 1) // 2
    ans = -1

    while l <= r:
        m = (l + r) // 2
        if g - m * (m + 1) // 2 >= n_adj:
            ans = k_adj - m
            l = m + 1
        else:
            r = m - 1

    print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)
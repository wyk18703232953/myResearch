import random

def main(n):
    # 1. 根据规模 n 生成 r, g, b 的大小（1~n）
    r = random.randint(1, n)
    g = random.randint(1, n)
    b = random.randint(1, n)

    # 2. 生成测试数据：三个升序数组
    # 元素值范围可以自行调整，这里用 1~10^6
    ls_r = sorted(random.randint(1, 10**6) for _ in range(r))
    ls_g = sorted(random.randint(1, 10**6) for _ in range(g))
    ls_b = sorted(random.randint(1, 10**6) for _ in range(b))

    # 3. 初始化 dp 数组
    dp = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    def recursive(idx_r, idx_g, idx_b):
        if dp[idx_r][idx_g][idx_b] != -1:
            return dp[idx_r][idx_g][idx_b]

        res_1 = 0
        res_2 = 0
        res_3 = 0

        if idx_r - 1 >= 0 and idx_g - 1 >= 0:
            res_1 = recursive(idx_r - 1, idx_g - 1, idx_b) + ls_r[idx_r - 1] * ls_g[idx_g - 1]
        if idx_g - 1 >= 0 and idx_b - 1 >= 0:
            res_2 = recursive(idx_r, idx_g - 1, idx_b - 1) + ls_g[idx_g - 1] * ls_b[idx_b - 1]
        if idx_r - 1 >= 0 and idx_b - 1 >= 0:
            res_3 = recursive(idx_r - 1, idx_g, idx_b - 1) + ls_r[idx_r - 1] * ls_b[idx_b - 1]

        dp[idx_r][idx_g][idx_b] = max(res_1, res_2, res_3)
        return dp[idx_r][idx_g][idx_b]

    # 4. 计算并输出结果
    result = recursive(r, g, b)
    print(result)

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)
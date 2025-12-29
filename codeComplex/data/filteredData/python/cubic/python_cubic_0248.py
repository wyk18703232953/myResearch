import random

def main(n):
    # 1. 生成测试数据规模
    # 将 n 分成 r, g, b 三种颜色的数量总和不超过 n
    # 简单做法：随机切分
    r = random.randint(0, n)
    g = random.randint(0, n - r)
    b = random.randint(0, n - r - g)

    # 2. 生成三个颜色数组（正整数），并排序
    ls_r = sorted(random.randint(1, 1000) for _ in range(r))
    ls_g = sorted(random.randint(1, 1000) for _ in range(g))
    ls_b = sorted(random.randint(1, 1000) for _ in range(b))

    # 3. DP 数组
    dp = [[[None for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    def recursive(idx_r, idx_g, idx_b):
        if dp[idx_r][idx_g][idx_b] is not None:
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

    result = recursive(r, g, b)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：用 n = 10 作为规模
    main(10)
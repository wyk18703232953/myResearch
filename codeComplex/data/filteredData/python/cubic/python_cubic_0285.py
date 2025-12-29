from random import randint

def main(n):
    """
    n 用作规模参数，用来生成 r, g, b 以及三种颜色的数组长度上限。
    这里简单设置：
      r, g, b 在 [1, n] 内随机
      各数组元素值在 [1, 10^4] 内随机
    """
    # 生成规模（限制在 200 以内，因为原 dp 固定到 205）
    max_len = min(n, 200)
    r = randint(1, max_len)
    g = randint(1, max_len)
    b = randint(1, max_len)

    a = []
    for _ in range(3):
        # 每个数组长度与对应的 r/g/b 一致
        # 第 0 个数组长度 r，第 1 个数组长度 g，第 2 个数组长度 b
        # 为保持通用性，按 max_len 生成足够长度，再只用前 r/g/b 个
        arr_len = max_len
        arr = [randint(1, 10_000) for _ in range(arr_len)]
        arr.sort(reverse=True)
        a.append(arr)

    # 按原逻辑，只使用前 r/g/b 个
    # a[0][:r], a[1][:g], a[2][:b]

    # dp[i][j][k]：使用红 i 个、绿 j 个、蓝 k 个时的最大得分
    # 原代码固定 205，这里沿用
    LIMIT = 205
    dp = [[[0 for _ in range(LIMIT)] for _ in range(LIMIT)] for _ in range(LIMIT)]
    answer = 0

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                cur = dp[i][j][k]
                if i < r and j < g:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        cur + a[0][i] * a[1][j]
                    )
                if i < r and k < b:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        cur + a[0][i] * a[2][k]
                    )
                if j < g and k < b:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        cur + a[1][j] * a[2][k]
                    )
                if cur > answer:
                    answer = cur

    print(answer)


if __name__ == "__main__":
    # 示例：规模 n=50
    main(50)
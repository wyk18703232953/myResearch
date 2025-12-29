import random

def main(n):
    # 随机生成规模参数 k
    k = max(1, n // 5)

    # 生成测试数据：
    # l, f, h 的长度和取值范围可根据 n、k 调整，这里给出一种简单方式
    # l 和 f 的元素值在 [1, n] 范围内
    # h 的长度为 k，元素值在 [1, 10] 范围内
    l = [random.randint(1, n) for _ in range(n)]
    f = [random.randint(1, n) for _ in range(n)]
    h = [random.randint(1, 10) for _ in range(k)]

    # 原始逻辑开始
    d1 = dict({(a, 0) for a in f})
    d2 = dict({(a, 0) for a in f})
    for a in l:
        if a in d1:
            d1[a] += 1
    for a in f:
        d2[a] += 1

    # dp 尺寸的原代码是 [520][520*12] 与 n,k 无关，为保持逻辑不变，仍使用固定大小
    max_x = 520
    max_y = 520 * 12
    dp = [[0 for _ in range(max_y)] for _ in range(max_x)]

    # 注意：原代码循环从 0 到 n+1 / n*k+1 而 dp 真正支持到 519、6239
    # 当 n,k 较大时可能越界；这里直接保留原始逻辑，假定 n,k 不超过 519。
    # 若 n 超界，将截断循环范围以避免越界。
    max_x_loop = min(n, max_x - 1)
    max_y_loop = min(n * k, max_y - 1)

    for x in range(max_x_loop + 1):
        for y in range(max_y_loop + 1):
            for i in range(k + 1):
                nx = x + 1
                ny = y + i
                if nx < max_x and ny < max_y:
                    dp[nx][ny] = max(
                        dp[nx][ny],
                        dp[x][y] + (0 if i == 0 else h[i - 1])
                    )

    ss = 0
    for i in d1:
        cx = d2[i]
        cy = d1[i]
        if cx < max_x and cy < max_y:
            ss += dp[cx][cy]
        # 若越界则忽略该项，与原逻辑一致性不完全保证，但避免崩溃

    print(ss)


if __name__ == "__main__":
    # 示例：指定 n 的测试规模
    main(100)
from math import floor
import random

def main(n):
    # 1. 生成测试数据：n 个 (x, p) 对
    #   要求：x 单调递增，便于体现原题中按 x 排序的场景
    #   p 随机生成，范围可根据需要调整
    a = []
    cur_x = 0
    for _ in range(n):
        cur_x += random.randint(1, 10)  # 保证 x 递增
        p = random.randint(0, 10)       # 任意非负代价
        a.append((cur_x, p))

    # 2. 按照原代码逻辑进行处理
    a.sort()
    dp = [0] * n

    for i in range(n):
        x, p = a[i]
        l = -1
        r = n
        v = x - p
        # 二分查找满足 a[c][0] >= v 的最小下标 r
        while r - l > 1:
            c = (l + r) // 2
            if a[c][0] >= v:
                r = c
            else:
                l = c
        # 按原代码意图：使用找到的 l 来更新 dp[i]
        if l == -1:
            dp[i] = i - l - 1
        else:
            dp[i] = i - l - 1 + dp[l]

    z = 10**9
    for i in range(n):
        z = min(z, dp[i] + n - i - 1)

    print(z)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)
import random

# 原始代码中的 mem 是 201^3 的固定大小，这里按 n 缩放
# 并保持相同的 DP 逻辑，只是 r,g,b 不再通过 input 读入，而是由 n 决定。

def main(n: int):
    # 根据 n 生成规模：
    # 令 r = g = b = n，生成长度为 n 的 R, G, B 三个数组
    r = g = b = n

    # 生成测试数据（可以根据需要调整生成规则）
    # 这里生成 [1, 1000] 范围内的随机整数
    R = sorted([random.randint(1, 1000) for _ in range(r)], reverse=True)
    G = sorted([random.randint(1, 1000) for _ in range(g)], reverse=True)
    B = sorted([random.randint(1, 1000) for _ in range(b)], reverse=True)

    # 由于 r,g,b 可以是任意 n，这里按 (r+1)*(g+1)*(b+1) 的大小开 mem
    mem = [[[-1] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    def dp(i, j, k):
        p = (i == r) + (j == g) + (k == b)
        if p > 1:
            return 0
        if mem[i][j][k] != -1:
            return mem[i][j][k]
        if i == r:
            ans = dp(i, j + 1, k + 1) + G[j] * B[k]
            mem[i][j][k] = ans
            return ans
        elif j == g:
            ans = dp(i + 1, j, k + 1) + R[i] * B[k]
            mem[i][j][k] = ans
            return ans
        elif k == b:
            ans = dp(i + 1, j + 1, k) + R[i] * G[j]
            mem[i][j][k] = ans
            return ans
        else:
            ans = max(
                dp(i + 1, j + 1, k) + R[i] * G[j],
                dp(i, j + 1, k + 1) + G[j] * B[k],
                dp(i + 1, j, k + 1) + R[i] * B[k],
            )
            mem[i][j][k] = ans
            return ans

    print(dp(0, 0, 0))


# 示例：直接运行 main(3)
if __name__ == "__main__":
    main(3)
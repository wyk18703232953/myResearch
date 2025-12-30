import random

def main(n: int):
    # 1. 根据 n 生成规模 r, g, b（这里简单设为 n, n, n，可自行调整为其他函数）
    r = g = b = n

    # 2. 生成测试数据，并按题意从大到小排序
    # 为了保持整数值适中，这里使用 1..1000 范围内的随机数
    R = sorted([random.randint(1, 1000) for _ in range(r)], reverse=True)
    G = sorted([random.randint(1, 1000) for _ in range(g)], reverse=True)
    B = sorted([random.randint(1, 1000) for _ in range(b)], reverse=True)

    # 3. 创建记忆化数组，规模为 (r+1) x (g+1) x (b+1)
    # 注意原程序固定为 201，这里改为依赖 r, g, b
    mem = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    def dp(i, j, k):
        # 若超过任一边界，返回 0（防御式处理，正常逻辑中不会越界）
        if i > r or j > g or k > b:
            return 0

        # 结束条件：如果有两组已经全部用完，则无法再配对
        p = (i == r) + (j == g) + (k == b)
        if p > 1:
            return 0

        if mem[i][j][k] != -1:
            return mem[i][j][k]

        if i == r:
            # 红色已经用完，只能 G-B 配对
            ans = dp(i, j + 1, k + 1) + G[j] * B[k]
        elif j == g:
            # 绿色已经用完，只能 R-B 配对
            ans = dp(i + 1, j, k + 1) + R[i] * B[k]
        elif k == b:
            # 蓝色已经用完，只能 R-G 配对
            ans = dp(i + 1, j + 1, k) + R[i] * G[j]
        else:
            # 三种配对方式中取最大值
            ans = max(
                dp(i + 1, j + 1, k) + R[i] * G[j],   # R-G
                dp(i, j + 1, k + 1) + G[j] * B[k],   # G-B
                dp(i + 1, j, k + 1) + R[i] * B[k]    # R-B
            )

        mem[i][j][k] = ans
        return ans

    result = dp(0, 0, 0)
    print(result)


# 简单示例：当该文件直接运行时，调用 main(3)
if __name__ == "__main__":
    main(3)
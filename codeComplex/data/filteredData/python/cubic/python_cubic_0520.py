def main(n):
    import random

    # 生成规模参数
    # n: 行数
    # m: 列数（这里设为与 n 相同，可按需调整）
    # k: 步数（设为偶数，确保可行，也可改为其他偶数函数）
    m = n
    k = 2 * (n if n > 0 else 1)

    # 生成测试数据：right 和 down 的边权为 1~10 的随机整数
    right = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]
    down = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    if k & 1:
        # 若 k 为奇数，原逻辑输出 -1
        ans = [[-1] * m for _ in range(n)]
        return ans

    # DP 数组
    mem = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            mem[i][j] = 0

    # 迭代 k/2 次
    for _step in range(1, k // 2 + 1):
        mem0 = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                # 上
                if i - 1 >= 0:
                    mem0[i][j] = min(mem0[i][j], mem[i - 1][j] + down[i - 1][j])
                # 下
                if i + 1 < n:
                    mem0[i][j] = min(mem0[i][j], mem[i + 1][j] + down[i][j])
                # 左
                if j - 1 >= 0:
                    mem0[i][j] = min(mem0[i][j], mem[i][j - 1] + right[i][j - 1])
                # 右
                if j + 1 < m:
                    mem0[i][j] = min(mem0[i][j], mem[i][j + 1] + right[i][j])
        mem = mem0

    # 输出结果为 2 * mem[i][j]
    ans = [[mem[i][j] * 2 for j in range(m)] for i in range(n)]
    return ans


# 示例运行
if __name__ == "__main__":
    res = main(4)
    for row in res:
        print(*row)
mod, bits = 998244353, ['00', '01', '10', '11']
pat = [[0, 1, 1, 1],
       [0, 0, 2, 0],
       [0, 2, 0, 0],
       [1, 1, 1, 0]]

add = lambda a, b: (a % mod + b % mod) % mod


def main(n: int) -> int:
    """
    参数 n 为规模，同时自动生成 k 作为测试数据：
    这里示例设定 k = 2 * n，确保状态空间足够大。
    返回原程序对 (n, k) 的计算结果。
    """
    k = 2 * n  # 测试数据生成策略，可按需要修改

    # mem[2][k+1][4]
    mem = [[[0 for _ in range(4)] for _ in range(k + 1)] for _ in range(2)]

    # 初始化 i = 0 行
    for i in range(4):
        val = min(bits[i].count('0'), 1) + min(bits[i].count('1'), 1)
        if val <= k:
            mem[0][val][i] = 1

    # DP 迭代
    for i in range(1, n):
        upper_j = min(i * 2, k)
        for j in range(1, upper_j + 1):
            for k1 in range(4):
                if mem[(i - 1) & 1][j][k1] == 0:
                    continue
                for k2 in range(4):
                    val = j + pat[k1][k2]
                    if val <= k:
                        mem[i & 1][val][k2] = add(
                            mem[(i - 1) & 1][j][k1],
                            mem[i & 1][val][k2]
                        )

        # 清空上一层使用过的状态
        for j in range(1, min(i * 2 + 1, k + 1)):
            for k1 in range(4):
                mem[(i - 1) & 1][j][k1] = 0

    return sum(mem[(n - 1) & 1][k]) % mod


# 示例：直接运行文件时，给一个默认规模
if __name__ == "__main__":
    print(main(5))
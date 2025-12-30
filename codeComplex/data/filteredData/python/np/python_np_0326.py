mod = 998244353
bits = ['00', '01', '10', '11']
pat = [[0, 1, 1, 1],
       [0, 0, 2, 0],
       [0, 2, 0, 0],
       [1, 1, 1, 0]]

add = lambda a, b: (a + b) % mod


def main(n: int) -> int:
    """
    n: 规模（原程序中的 n）
    这里我们依据 n 自动生成 k，可根据需要调整策略。
    当前策略：k = 2 * n（保证有一定可行空间）
    """
    k = 2 * n

    # mem[i][j][t]: 长度为 i+1，使用代价 j，结尾状态为 t 的方案数
    mem = [[[0 for _ in range(4)] for _ in range(k + 1)] for _ in range(n)]

    # 初始化 i = 0
    for i in range(4):
        val = min(bits[i].count('0'), 1) + min(bits[i].count('1'), 1)
        if val <= k:
            mem[0][val][i] = 1

    for i in range(1, n):
        # j 表示前 i 个位置使用的总代价
        for j in range(1, min(k, i * 2) + 1):
            for k1 in range(4):
                if mem[i - 1][j][k1] == 0:
                    continue
                for k2 in range(4):
                    val = j + pat[k1][k2]
                    if val <= k:
                        mem[i][val][k2] = add(mem[i][val][k2], mem[i - 1][j][k1])

    ans = sum(mem[-1][k]) % mod
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)
mod, bits = 998244353, ['00', '01', '10', '11']
pat = [[0, 1, 1, 1],
       [0, 0, 2, 0],
       [0, 2, 0, 0],
       [1, 1, 1, 0]]

add = lambda a, b: (a % mod + b % mod) % mod


def main(n: int):
    """
    n: 序列长度
    测试数据生成策略：
      - 令 k = n，作为规模同阶的参数（可按需要调整）
    """
    k = n  # 根据 n 生成测试参数

    mem = [[[0 for _ in range(4)] for _ in range(k + 1)] for _ in range(n)]

    # 初始化 i = 0 这一层
    for i in range(4):
        val = min(bits[i].count('0'), 1) + min(bits[i].count('1'), 1)
        if val <= k:
            mem[0][val][i] = 1

    # 状态转移
    for i in range(1, n):
        for j in range(1, k + 1):
            for k1 in range(4):
                if mem[i - 1][j][k1] == 0:
                    continue
                for k2 in range(4):
                    val = j + pat[k1][k2]
                    if val <= k:
                        mem[i][val][k2] = add(mem[i - 1][j][k1], mem[i][val][k2])

    ans = sum(mem[-1][k]) % mod
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：以 n = 5 作为测试规模
    main(5)
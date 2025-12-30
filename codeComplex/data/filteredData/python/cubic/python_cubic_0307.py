from random import randint

def main(n: int):
    """
    n 作为规模参数，这里用于控制每种颜色数组的长度上限。
    实际 r,g,b 会在 [1, n] 均匀随机生成。
    数组元素为 [1, 10*n] 间的随机整数。
    """
    # 生成规模
    from random import randint
    r = randint(1, n)
    g = randint(1, n)
    b = randint(1, n)

    # 生成测试数据：随机正整数
    rl = [randint(1, 10 * n) for _ in range(r)]
    gl = [randint(1, 10 * n) for _ in range(g)]
    bl = [randint(1, 10 * n) for _ in range(b)]

    # 原程序对三个数组做降序排序
    rl.sort(reverse=True)
    gl.sort(reverse=True)
    bl.sort(reverse=True)

    # 记忆化 DP 表
    dp_table = [[[-1] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    def solve(i, j, k):
        if dp_table[i][j][k] != -1:
            return dp_table[i][j][k]

        if i < r and j < g and k < b:
            m = max(
                solve(i + 1, j + 1, k) + (rl[i] * gl[j]),
                solve(i + 1, j, k + 1) + (rl[i] * bl[k]),
                solve(i, j + 1, k + 1) + (gl[j] * bl[k]),
            )
            dp_table[i][j][k] = m
            return m

        elif i < r and j < g:
            m = solve(i + 1, j + 1, b) + rl[i] * gl[j]
            dp_table[i][j][k] = m
            return m

        elif i < r and k < b:
            m = solve(i + 1, g, k + 1) + (rl[i] * bl[k])
            dp_table[i][j][k] = m
            return m

        elif j < g and k < b:
            m = solve(r, j + 1, k + 1) + (gl[j] * bl[k])
            dp_table[i][j][k] = m
            return m
        else:
            return 0

    res = solve(0, 0, 0)
    print(res)


if __name__ == "__main__":
    # 示例：n = 5
    main(5)
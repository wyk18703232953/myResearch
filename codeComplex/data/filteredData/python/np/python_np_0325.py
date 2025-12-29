mod = 998244353
bits = ['00', '01', '10', '11']
pat = [[0, 1, 1, 1],
       [0, 0, 2, 0],
       [0, 2, 0, 0],
       [1, 1, 1, 0]]

add = lambda a, b: (a % mod + b % mod) % mod


def main(n: int):
    """
    将原程序参数化：
    - n: 原代码中的长度参数
    - 这里我们生成一个与 n 相关的 k，作为测试数据。
      原本 k 是从输入读入的上界，本质是“代价上界”。
      这里示例：k 取最大可能值，即 2 * n，保证不会截断状态。
    """
    k = 2 * n

    mem = [[[0 for _ in range(4)] for _ in range(k + 1)] for _ in range(n)]

    # 初始化 i = 0
    for i in range(4):
        val = min(bits[i].count('0'), 1) + min(bits[i].count('1'), 1)
        if val <= k:
            mem[0][val][i] = 1

    # 状态转移
    for i in range(1, n):
        # j 至多为 2 * i（原代码：range(1, i * 2 + 1)）
        for j in range(1, i * 2 + 1):
            for k1 in range(4):
                if mem[i - 1][j][k1] == 0:
                    continue
                base = mem[i - 1][j][k1]
                for k2 in range(4):
                    val = j + pat[k1][k2]
                    if val <= k:
                        mem[i][val][k2] = add(base, mem[i][val][k2])

    ans = sum(mem[-1][k]) % mod
    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)
import random
from copy import deepcopy

def main(n):
    # 生成测试数据
    # n: 行数
    # 随机生成 m, k，并生成相应的 lr, ud
    m = max(1, n)  # 简单设定 m 与 n 同规模，也可自行调整
    # 为保证有意义的结果，令 k 为偶数（若想测试 -1 输出，可改为随机奇偶）
    k = random.randint(1, 2 * n)
    if k % 2 == 1:
        k += 1  # 强制改为偶数

    # 生成 lr: n 行，每行 m-1 个水平边权（实际上原代码是每行 m-1 条在中间，被两端哨兵包裹）
    # 为简化，我们随机生成 m-1 个，再在两端加哨兵，长度会变为 m+1，
    # 但原程序中是 [100000001] + m 个数 + [100000001]，因此真实 m 为已读的 m，
    # 我们直接生成 m 个真实边，再加两端哨兵，与原程序一致。
    MAXC = 10**6
    lr = []
    for _ in range(n):
        row = [100000001]  # 左哨兵
        row += [random.randint(1, MAXC) for _ in range(m)]
        row += [100000001]  # 右哨兵
        lr.append(row)

    # 生成 ud: (n+1) 行，每行 m 个竖直边权，中间部分随机，两侧有哨兵行
    ud = [[100000001] * m]  # 上哨兵行
    for _ in range(n - 1):
        ud.append([random.randint(1, MAXC) for _ in range(m)])
    ud.append([100000001] * m)  # 下哨兵行

    # 接下来是原逻辑的实现部分（不再使用 input/sys.stdout）
    if k % 2:
        # 理论上不会走到这里，因为我们强制让 k 为偶数
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return

    # 初始化 o，带边界哨兵
    o = [[1000000001] * (m + 2)]
    for _ in range(n):
        oo = [100000001]
        for _ in range(m):
            oo.append(0)
        oo.append(100000001)
        o.append(oo)
    o.append([100000001] * (m + 2))

    # DP 迭代 k//2 次
    for _ in range(k // 2):
        oo = deepcopy(o)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                oo[i][j] = min(
                    lr[i - 1][j - 1] + o[i][j - 1],   # 左
                    lr[i - 1][j] + o[i][j + 1],       # 右
                    ud[i - 1][j - 1] + o[i - 1][j],   # 上
                    ud[i][j - 1] + o[i + 1][j]        # 下
                )
        o = oo

    # 输出结果
    for i in o[1:n + 1]:
        print(" ".join(str(j * 2) for j in i[1:m + 1]))


if __name__ == "__main__":
    # 示例：调用 main(3)，可以根据需要修改 n
    main(3)
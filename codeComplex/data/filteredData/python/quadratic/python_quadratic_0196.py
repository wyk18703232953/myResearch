from operator import xor
import random


def main(n: int):
    # 1. 生成测试数据
    # 生成长度为 n 的初始数组 a[0]
    a0 = [random.randint(0, 100) for _ in range(n)]

    # 随机生成查询数量 m（至少 1 个，至多 n*(n+1)//2 个）
    max_pairs = n * (n + 1) // 2
    m = min(max_pairs, max(1, n))  # 简单设定：m 与 n 同量级但不超过所有区间数

    # 构造所有合法区间 [l, r] (1-based)
    all_pairs = []
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            all_pairs.append((l, r))

    # 从所有合法区间中随机抽取 m 个作为查询
    # 若 max_pairs < m（理论上不会发生，因为 m <= max_pairs），则全用
    if len(all_pairs) > m:
        qur = random.sample(all_pairs, m)
    else:
        qur = all_pairs

    # 2. 按原逻辑构建数组 a
    # a[i] 是一行列表
    a = [a0]
    # 第一轮：构建异或三角形
    for i in range(1, n):
        prev = a[-1]
        a.append([xor(prev[j], prev[j + 1]) for j in range(len(prev) - 1)])

    # 第二轮：在原三角形基础上做 max 传播
    for i in range(n - 1):
        upper = a[i]
        cur = a[i + 1]
        # 对当前行的每个元素，取其上方和左上方的 max 再和自身取 max
        a[i + 1] = [
            max(upper[j], upper[j + 1], cur[j]) for j in range(len(cur))
        ]

    # 3. 按原逻辑回答查询
    out = []
    for l, r in qur:
        out.append(a[r - l][l - 1])

    # 4. 输出结果（先输出测试数据，便于复现；再输出结果）
    print("n =", n)
    print("a0 =", " ".join(map(str, a0)))
    print("m =", m)
    print("queries:")
    for l, r in qur:
        print(l, r)
    print("answers:")
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    # 示例调用：可自行修改 n
    main(5)
import random

def main(n):
    # 1. 根据规模 n 生成数据
    # 这里假设：
    #   - v 的长度为 n
    #   - 生成 m 条操作，其中一部分为 x==1 的操作，用于生成 h
    # 你可以根据需要更改生成规则
    m = max(1, n)  # 简单设为 m 与 n 同阶
    MAX_VAL = 10**9

    # 生成 v：n 个 [1, MAX_VAL] 的随机整数
    v = [random.randint(1, MAX_VAL) for _ in range(n)]

    # 生成 m 条操作 (x, y, z)，其中 x==1 的操作用于生成 h
    h = []
    for _ in range(m):
        x = random.randint(1, 2)  # 随便取 1 或 2，只有 1 才会影响结果
        y = random.randint(1, MAX_VAL)
        z = random.randint(1, MAX_VAL)  # 实际逻辑中 z 没有用到，但按原代码格式保留
        if x == 1:
            h.append(y)

    # 2. 按原逻辑处理
    h.sort()
    v.sort()
    m = len(h)
    n = len(v)

    if n == 0 or v[n - 1] != MAX_VAL:
        v.append(MAX_VAL)
        n += 1

    mina = 9999999999999
    j = 0
    for i in range(n):
        while j < m and h[j] < v[i]:
            j += 1
        mina = min(mina, i + m - j)

    print(mina)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
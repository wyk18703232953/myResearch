import random

def main(n):
    # 生成规模为 n 的测试数据
    # 这里令 m = n（可按需要调整生成规则）
    m = n

    # 生成 n + m 个坐标，严格递增
    # 随机生成步长，避免重复坐标
    steps = [random.randint(1, 10) for _ in range(n + m)]
    xs = []
    cur = 0
    for step in steps:
        cur += step
        xs.append(cur)

    # 生成 ts：长度为 n + m，含有 m 个 1 和 n 个 0
    ts = [1] * m + [0] * n
    random.shuffle(ts)

    # 保证至少有一个 1（若生成逻辑改变时可防御）
    if 1 not in ts:
        ts[random.randrange(n + m)] = 1

    # 以下为原始算法逻辑
    pos = [-1 for _ in range(n + m)]
    if ts[0]:
        pos[0] = 0
    for i in range(1, n + m):
        pos[i] = pos[i - 1]
        if ts[i]:
            pos[i] += 1

    result = [0 for _ in range(m)]
    left = 0
    leftC = 0  # 保留原变量名但未使用
    right = 0
    rightC = 0  # 保留原变量名但未使用

    for i in range(n + m):
        if ts[i] == 0:
            right = max(i, right)
            while right + 1 < n + m and not ts[right]:
                right += 1
            mP, mD = 0, 20000000
            if ts[left]:
                mP = pos[left]
                mD = xs[i] - xs[left]
            if ts[right] and xs[right] - xs[i] < mD:
                mD = xs[right] - xs[i]
                mP = pos[right]
            result[mP] += 1
        else:
            left = i

    print(*result)


if __name__ == "__main__":
    # 调用示例：规模 n = 5
    main(5)
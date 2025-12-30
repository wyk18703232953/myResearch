import random

def main(n):
    # 这里将 n 作为有“1”的位置的数量，额外随机生成 m 个“0”位置
    # 使得总长度为 n + m
    #
    # 构造规则（可按需要调整）：
    # - 长度 total_len = n + m
    # - 在前 total_len 个下标里随机选择 n 个作为 b[i] == 1，其余为 0
    # - a 为严格递增的正整数序列，方便“距离”比较

    if n <= 0:
        return

    # 可调整：额外的“0”数量 m
    m = n  # 这里示例取 m = n，可按需求调整为其他比例
    total_len = n + m

    # 随机生成严格递增的 a
    # a[i] = a[i-1] + random positive step
    a = []
    cur = random.randint(1, 5)
    for _ in range(total_len):
        a.append(cur)
        cur += random.randint(1, 5)

    # 随机选出 n 个位置作为 b[i] == 1，其余为 0
    indices = list(range(total_len))
    random.shuffle(indices)
    ones_pos = set(indices[:n])

    b = [1 if i in ones_pos else 0 for i in range(total_len)]

    # 以下是原逻辑，仅把 n,m 从输入改为上面构造的 total_len 与 n
    l = [None] * total_len
    r = [None] * total_len
    c = [0] * total_len

    x = None
    for i in range(total_len):
        l[i] = x
        if b[i] == 1:
            x = i

    x = None
    for i in range(total_len - 1, -1, -1):
        r[i] = x
        if b[i] == 1:
            x = i

    for i in range(total_len):
        if b[i] == 0:
            aa = a[i]
            ll = l[i]
            rr = r[i]
            if ll is None:
                if rr is not None:
                    c[rr] += 1
            elif rr is None:
                c[ll] += 1
            else:
                if aa - a[ll] <= a[rr] - aa:
                    c[ll] += 1
                else:
                    c[rr] += 1

    # 按原逻辑，只输出 b[i] == 1 的位置对应的 c[i]
    out = []
    for i in range(total_len):
        if b[i] == 1:
            out.append(str(c[i]))
    print(" ".join(out))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
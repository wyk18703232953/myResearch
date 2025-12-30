import random

def main(n):
    # 随机生成参数
    # 为了保证有意义的范围，这里生成 s 中元素，并基于 s 生成 l, r, x
    s = [random.randint(1, 100) for _ in range(n)]
    total_sum = sum(s)
    min_s, max_s = min(s), max(s)

    # 生成 l, r
    # 确保 1 <= l <= r <= total_sum
    l = random.randint(1, total_sum)
    r = random.randint(l, total_sum)

    # 生成 x (最大值与最小值差的下界)
    x = random.randint(0, max_s - min_s if max_s > min_s else 0)

    # 原始逻辑
    olmps = []
    c = []
    v = 0
    for i in range(1 << n):
        olmps.append([])
        for j in range(n):
            if i & (1 << j):
                olmps[-1].append(s[j])
    for o in olmps:
        if l <= sum(o) <= r:
            c.append(o)
    for z in c:
        if z and max(z) - min(z) >= x:
            v += 1

    print(v)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(5)
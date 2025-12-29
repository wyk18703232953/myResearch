import random

def main(n):
    # 1. 生成测试数据
    # 生成 n 对 (a, b)，以及总容量 m
    # 保证 a >= b >= 0
    pairs = []
    for _ in range(n):
        b = random.randint(0, 1000)
        a = b + random.randint(0, 1000)
        pairs.append([a, b])

    # 生成 m，可以覆盖多种情况：有时足够、有时不够、有时完全不可能
    # 这里简单设为所有 b 的和到所有 a 的和之间的随机值
    sum_a = sum(p[0] for p in pairs)
    sum_b = sum(p[1] for p in pairs)
    if sum_b > sum_a:  # 理论上不会发生，因为构造时 a >= b
        sum_b = min(sum_b, sum_a)

    if sum_b == sum_a:
        m = sum_a
    else:
        m = random.randint(max(0, sum_b - 500), sum_a + 500)

    # 2. 按原逻辑处理
    final = pairs[:]
    final.sort(key=lambda x: x[0] - x[1])

    s1 = 0
    s2 = 0
    for a, b in final:
        s1 += a
        s2 += b

    if s2 > m:
        print(-1)
    else:
        if s1 <= m:
            print(0)
        else:
            i = n - 1
            count = 0
            while s1 > m and i >= 0:
                s1 = s1 - (final[i][0] - final[i][1])
                count += 1
                i -= 1
            print(count)


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)
import random

def main(n):
    # 生成测试数据：
    # n: 元素个数
    # 生成 m 为一个较大的上限，用于测试压缩效果
    # 生成 n 对 (a, b)，确保 a >= b 且为非负整数
    random.seed(0)

    # 生成 a, b
    ab_pairs = []
    sm = 0
    for _ in range(n):
        a = random.randint(0, 10**6)
        b = random.randint(0, a)  # 确保压缩有效：a >= b
        ab_pairs.append((a, b))
        sm += a

    # 生成 m：在 [sm//2, sm + n] 范围内取一个数，保证有可能达成也有可能无法达成
    if sm == 0:
        m = 0
    else:
        low = sm // 2
        high = sm + n
        m = random.randint(low, high)

    # 以下为原逻辑的无 input 版本
    tup = []
    for a, b in ab_pairs:
        diff = a - b
        tup.append([diff, a, b])

    tup.sort(reverse=True)
    ans = 0
    i = 0
    while sm > m and i < n:
        sm -= tup[i][1]
        sm += tup[i][2]
        i += 1
        ans += 1

    if sm <= m:
        print(ans)
    else:
        print(-1)


if __name__ == '__main__':
    # 示例：调用 main，规模 n 可自行调整
    main(10)
from itertools import combinations
import random

def main(n):
    # 生成测试数据
    # 随机生成 n 本书的难度值 a[i]，范围可自行调整
    a = [random.randint(1, 100) for _ in range(n)]
    # 生成区间 [l, r]，以及 x
    # 为了保证有意义，l <= r，范围基于 a 的和
    total_sum = sum(a)
    l = random.randint(0, total_sum // 2)
    r = random.randint(l, total_sum)
    x = random.randint(0, max(a) - min(a) if n > 1 else 0)

    c = []
    for i in range(2, n + 1):
        c += list(combinations(a, i))

    cnt = 0

    for t in c:
        m = min(t)
        M = max(t)
        s = sum(t)
        if M - m >= x and l <= s <= r:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(5)
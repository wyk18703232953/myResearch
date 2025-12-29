import random

def main(n):
    # 参数含义与原程序保持一致：n, l, r, x, c[]
    # 这里根据 n 生成测试数据：
    # - 生成 n 个难度值 c[i]，范围 1~1000
    # - 保证 l, r, x 合理：l <= r，x >= 0
    # 你可根据需要自行调整生成规则
    random.seed(0)

    c = [random.randint(1, 1000) for _ in range(n)]
    c.sort()

    total_sum = sum(c)
    # 生成 l, r
    l = random.randint(0, total_sum // 2 if total_sum > 0 else 0)
    r = random.randint(l, total_sum)
    # 生成 x
    x = random.randint(0, max(c) - min(c) if n > 1 else 0)

    p = 1 << n
    cnt = 0  # no. of ways

    for j in range(p):
        if j > 0 and (j & (j - 1)) != 0:  # 至少两个元素
            subset = []
            for k in range(n):
                if j & (1 << k):
                    subset.append(c[k])
            s = sum(subset)
            if l <= s <= r and subset[-1] - subset[0] >= x:
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
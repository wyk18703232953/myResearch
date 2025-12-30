import random

def main(n: int):
    # 生成测试数据
    # 约束：1 ≤ n ≤ 15（因为原算法是 2^n 枚举）
    # 随机生成 l, r, x 和 c 列表
    # 保证 l <= r，且 x 非负

    # 生成难度值数组 c
    c = [random.randint(1, 10**6) for _ in range(n)]

    # 生成 l, r
    total_sum = sum(c)
    l = random.randint(0, total_sum)
    r = random.randint(l, total_sum)  # 保证 l <= r

    # 生成 x
    max_c = max(c)
    min_c = min(c)
    max_diff = max_c - min_c
    x = random.randint(0, max_diff if max_diff > 0 else 0)

    ans = 0

    # 枚举所有子集
    for mask in range(1 << n):
        cnt, csum = 0, 0
        mn, mx = 10**18, -(10**18)
        for i in range(n):
            if mask & (1 << i):
                cnt += 1
                csum += c[i]
                mn = min(mn, c[i])
                mx = max(mx, c[i])
        if (cnt >= 2) and (l <= csum <= r) and (mx - mn >= x):
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)
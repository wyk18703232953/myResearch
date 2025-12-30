import random

def main(n):
    # 生成测试数据
    # 这里按原题意随机生成 l, r, x 和数组 a
    # 可根据需要自行调整范围
    a = [random.randint(1, 10**6) for _ in range(n)]
    l = random.randint(0, 10**6)
    r = random.randint(l, 10**6)
    x = random.randint(0, 10**6)

    t = 0
    # 遍历所有非空子集（至少两个元素）
    for mask in range(1, 1 << n):
        # 统计子集中元素个数
        count = mask.bit_count()
        if count <= 1:
            continue

        subset_sum = 0
        subset_vals = []
        for j in range(n):
            if mask & (1 << j):
                subset_sum += a[j]
                subset_vals.append(a[j])

        if l <= subset_sum <= r and (max(subset_vals) - min(subset_vals)) >= x:
            t += 1

    print(t)


# 示例调用（提交时可删除或保留）：
# main(5)
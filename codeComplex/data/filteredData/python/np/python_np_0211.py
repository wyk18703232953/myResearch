import random

def main(n: int):
    # 生成测试数据
    # 为了保证有意义的约束，这里按如下方式生成：
    # a[i] 在 [1, 10^6] 内随机
    a = [random.randint(1, 10**6) for _ in range(n)]

    # l, r, x 的生成方式：
    # 先计算数组的最小可能和与最大可能和
    a_sorted = sorted(a)
    min_possible_sum = a_sorted[0] + a_sorted[1] if n >= 2 else a_sorted[0]
    max_possible_sum = sum(a_sorted)
    # 避免边界问题，确保 l <= r
    l = random.randint(min_possible_sum, max_possible_sum)
    r = random.randint(l, max_possible_sum)
    # x 为题意中的“最大值与最小值的最小差值”
    # 设置为数组中大概的跨度一部分，至少 1
    x = random.randint(1, max(1, max(a) - min(a)))

    count = 0
    # 枚举所有子集（原题逻辑）
    for mask in range(1 << n):
        maxc = -1
        minc = -1
        c = 0
        for j in range(n):
            if (mask >> j) & 1 == 1:
                val = a[j]
                c += val
                if maxc == -1 or val > maxc:
                    maxc = val
                if minc == -1 or val < minc:
                    minc = val
        if maxc != -1:  # 至少选择了一个元素
            if l <= c <= r and maxc - minc >= x:
                count += 1

    print(count)


# 示例：直接运行时给一个默认规模
if __name__ == "__main__":
    main(5)
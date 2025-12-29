import random

def main(n: int):
    # 生成测试数据
    # 1. 随机生成数组 numbers，长度为 n，元素范围 [1, 10^9]
    # 2. 随机从数组中选一个位置，将该位置的值设为中位数 m
    if n <= 0:
        return

    # 生成随机数组
    numbers = [random.randint(1, 10**9) for _ in range(n)]
    # 随机选择一个位置作为 m 出现的位置
    median_index = random.randrange(n)
    m = numbers[median_index]

    # 原逻辑开始
    smaller_greater = [(0, 0)]
    for k in numbers:
        s, g = smaller_greater[-1]
        if k < m:
            smaller_greater.append((s + 1, g))
        elif k > m:
            smaller_greater.append((s, g + 1))
        else:
            smaller_greater.append((s, g))

    i = numbers.index(m)
    s_median, g_median = smaller_greater[i]

    difference = {}
    for pack in smaller_greater[i + 1:]:
        s, g = pack
        s -= s_median
        g -= g_median
        key = s - g
        if key in difference:
            difference[key] += 1
        else:
            difference[key] = 1

    count = 0
    for start in range(i + 1):
        s, g = smaller_greater[start]
        s -= s_median
        g -= g_median
        key = s - g
        if key in difference:
            count += difference[key]
        key2 = key - 1
        if key2 in difference:
            count += difference[key2]

    print(count)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
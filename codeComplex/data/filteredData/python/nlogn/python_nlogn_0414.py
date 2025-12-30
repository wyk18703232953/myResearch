import random

def main(n):
    # 1. 生成测试数据：n 个区间 [l, r]
    # 为了简单，这里生成 1 到 2n 范围内的随机区间
    intervals = []
    for _ in range(n):
        l = random.randint(1, 2 * n)
        r = random.randint(1, 2 * n)
        if l > r:
            l, r = r, l
        intervals.append((l, r))

    # 2. 原逻辑实现
    point = {}

    for l, r in intervals:
        r += 1
        if l not in point:
            point[l] = 0
        if r not in point:
            point[r] = 0
        point[l] += 1
        point[r] -= 1

    line = []
    for key in point:
        line.append((key, point[key]))
    line.sort()
    ans = [0] * (n + 1)

    last_index = 0
    last_value = 0

    for index, value in line:
        ans[last_value] += index - last_index
        last_index = index
        last_value += value

    # 输出结果
    for cnt in ans[1:]:
        print(cnt, end=' ')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
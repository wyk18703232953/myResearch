import random

def main(n):
    # 生成测试数据：
    # n 条记录，每条为 (a, b)，其中 a >= b >= 0
    # 同时生成一个上限 m
    entries = []
    for _ in range(n):
        a = random.randint(1, 1000)
        b = random.randint(0, a)  # 保证 a >= b
        entries.append((a, b))
    # 可以根据 entries 生成一个相对合理的 m
    # 例如：m 为所有 a 之和减去一部分
    total_a = sum(x[0] for x in entries)
    m = max(0, total_a - random.randint(0, total_a))

    # 原始逻辑开始
    entries.sort(key=lambda x: x[1] - x[0])

    size = sum(x[0] for x in entries)
    count = 0

    while size > m and count < n:
        size -= entries[count][0] - entries[count][1]
        count += 1

    result = -1 if size > m else count
    print(result)


if __name__ == "__main__":
    # 示例：n=10
    main(10)
import random

def main(n: int):
    # 根据 n 生成测试数据
    # 最大点对距离和 max_dist 与最小点对距离和 min_dist 的计算依赖 n
    # 再随机生成 m 组 (x, d)，规模与 n 相关
    # 可按需要调整 m 的生成方式，这里设为 n（至少为 1）
    m = max(1, n)

    # 随机生成 (x, d) 列表，d 允许为负以覆盖两种分支
    # x 范围与 n 成正比，d 范围与 n 成正比（只是示例生成策略）
    queries = []
    for _ in range(m):
        x = random.randint(-10 * n, 10 * n)
        d = random.randint(-10 * n, 10 * n)
        queries.append((x, d))

    # 以下是原逻辑
    max_dist = (n - 1) * n // 2
    min_dist = max_dist
    curr_value = max_dist

    for i in range(n):
        curr_value = i * (i + 1) // 2 + (n - 1 - i) * (n - i) // 2
        min_dist = min(min_dist, curr_value)

    answer = 0
    add_value = 0

    for x, d in queries:
        answer += x
        if d >= 0:
            add_value += d * max_dist
        else:
            add_value += d * min_dist

    result = answer + (add_value / n)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)
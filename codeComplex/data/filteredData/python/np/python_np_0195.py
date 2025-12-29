import random

def main(n):
    # 生成测试数据
    # 分数范围设定为 1~1000，题目要求参数合理随机
    c = [random.randint(1, 1000) for _ in range(n)]
    c.sort()

    # 为了让条件有一定可行性：
    total_sum = sum(c)
    min_score = c[0]
    max_score = c[-1]

    # l, r 在合理范围内生成
    # l 从 0 ~ total_sum 中间偏下，r 从中间 ~ total_sum
    l = random.randint(0, max(0, total_sum // 2))
    r = random.randint(max(l, total_sum // 2), total_sum)

    # x 在分数差范围内生成
    x = random.randint(0, max_score - min_score if max_score > min_score else 0)

    ways = 0
    for i in range(0, 2 ** n):
        temp = 0
        m = 10 ** 9 + 1
        M = -1
        for j in range(0, n):
            if i & (1 << j):
                temp += c[j]
                m = min(m, c[j])
                M = max(M, c[j])
        if temp >= l and temp <= r and (M - m) >= x:
            ways += 1

    print(ways)

# 示例：手动调用 main(n)
if __name__ == "__main__":
    main(10)
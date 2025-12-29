import random

def main(n):
    # 生成测试数据
    # 设 m 为与 n 同量级的规模
    m = n

    # 生成 m 个整数到数组 a 中
    # 取值范围随 n 缩放，避免过大
    a = [random.randint(1, 10 ** 6) for _ in range(m)]

    # 生成 n 条操作，其中部分为 f == 1 的操作
    # g 的范围与 a 中元素范围一致
    ops = []
    for _ in range(n):
        f = random.choice([1, 2])        # 随机选择操作类型 1 或 2
        g = random.randint(1, 10 ** 6)
        d = random.randint(1, 10 ** 6)   # d 在原代码中未使用，这里仍生成
        ops.append((f, g, d))

    # 原始逻辑开始
    a.append(10 ** 9)
    s = []
    for f, g, d in ops:
        if f == 1:
            s.append(g)

    a.sort()
    s.sort()

    q1 = 0
    min1 = float('inf')
    for q2 in range(len(a)):
        while q1 < len(s) and a[q2] > s[q1]:
            q1 += 1
        if min1 > q2 + len(s) - q1:
            min1 = q2 + len(s) - q1
        if q1 == len(s):
            break

    print(min1)


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)
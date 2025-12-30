import random

def main(n: int):
    # 生成测试数据：n 对 (a, b) 整数对
    # 这里假设 a, b 在 [1, 10^9] 范围内，且无其他约束
    pairs = []
    for _ in range(n):
        a = random.randint(1, 10**9)
        b = random.randint(1, 10**9)
        pairs.append((a, b))

    # 原逻辑开始
    c = []
    for idx, (a, b) in enumerate(pairs):
        c.append((a, b, idx))  # 保留原始下标

    c.sort(key=lambda x: (x[0], -x[1]))

    a = c[0][1]
    b = c[0][2]
    an1 = -1
    an2 = -1
    for i in range(1, n):
        if c[i][1] <= a:
            an2 = b + 1
            an1 = c[i][2] + 1
            break
        else:
            a = c[i][1]
            b = c[i][2]

    print(an1, an2)


if __name__ == "__main__":
    # 可在此修改 n 以测试不同规模
    main(10)
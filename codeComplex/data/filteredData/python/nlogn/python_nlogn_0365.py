import random

def main(n):
    # 生成测试数据：
    # 随机生成 k（1 到 10）
    k = random.randint(1, 10)
    # 随机生成 n 个整数（1 到 100）
    t = [random.randint(1, 100) for _ in range(n)]

    # 原逻辑开始
    t.sort()

    f = {}
    for j in t:
        if j not in f:
            f[j] = 1
        else:
            f[j] += 1

    p = 0
    for j in range(n):
        if j < n - 1:
            if t[j + 1] > t[j] and t[j] + k >= t[j + 1]:
                p += f[t[j]]

    print(n - p)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
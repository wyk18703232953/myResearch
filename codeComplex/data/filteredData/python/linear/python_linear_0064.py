import random

def main(n):
    # 生成测试数据：
    # n 行 (f, t)，以及初始 s
    # 假设 f, t, s 在 0~10^6 范围内
    s = random.randint(0, 10**6)
    data = []
    for _ in range(n):
        f = random.randint(0, 10**6)
        t = random.randint(0, 10**6)
        data.append((f, t))

    # 原逻辑：给定 n, s 和 n 对 (f, t)，求 max(s, max(f + t))
    maxi = s
    for f, t in data:
        maxi = max(maxi, f + t)

    print(maxi)

if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)
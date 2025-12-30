import random

def main(n):
    # 1. 随机生成规模
    # n: 男生数量
    # m: 女生数量，设为 n 或 n+1，保证 m >= 1
    m = max(1, n + random.randint(0, 2))  # m 在 [n, n+2] 内

    # 2. 生成测试数据
    # 生成 b 和 g，保证长度分别为 n 和 m
    # 元素为正整数，这里取 1~10^3 的随机值
    b = [random.randint(1, 1000) for _ in range(n)]
    g = [random.randint(1, 1000) for _ in range(m)]

    # 3. 原逻辑
    b.sort()
    g.sort()
    if b[-1] > g[0]:
        print(-1)
        return
    if b[-1] == g[0]:
        print(sum(g) + m * (sum(b) - b[-1]))
        return
    if n == 1:
        print(-1)
        return
    print(sum(g) + b[-1] + b[-2] * (m - 1) + m * (sum(b) - b[-1] - b[-2]))


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需调整
    main(5)
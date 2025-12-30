import random

def main(n: int):
    # 生成参数 a, b，满足 1 <= a < b < n
    if n < 2:
        raise ValueError("n must be at least 2")
    a = random.randint(1, n - 2)
    b = random.randint(a + 1, n - 1)

    # 生成 n 个随机身高，范围可自行调整
    h = [random.randint(1, 10**9) for _ in range(n)]
    h.sort()

    # 原题逻辑：输出 h[b] - h[b-1]
    print(h[b] - h[b - 1])

if __name__ == "__main__":
    # 示例：用 n=10 运行一次
    main(10)
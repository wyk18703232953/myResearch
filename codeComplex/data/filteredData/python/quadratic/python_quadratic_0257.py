import random

def main(n: int):
    # 生成测试数据：根据 n 构造 a, b
    # 保持题意有代表性：随机在 1 和 n 之间
    if n < 2:
        n = 2
    a = random.randint(1, n)
    b = random.randint(1, n)

    if min(a, b) > 1 or ((n, a, b) in ((2, 1, 1), (3, 1, 1))):
        print("NO")
        return

    res = [[0] * n for _ in range(n)]
    for i in range(0, n - max(a, b)):
        res[i][i + 1] = res[i + 1][i] = 1
    if a == 1:
        res = [[e ^ 1 for e in row] for row in res]

    print("YES")
    for i in range(n):
        res[i][i] = 0
        print(*res[i], sep='')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
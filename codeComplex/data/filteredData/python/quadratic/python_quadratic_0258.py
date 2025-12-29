import random

def main(n):
    # 根据规模 n 生成测试数据 (n, a, b)
    # 这里生成 1 <= a, b <= n，用户可按需要调整生成策略
    if n < 2:
        n = 2
    a = random.randint(1, min(3, n))  # 控制 a、b 不至于太大，便于观察
    b = random.randint(1, min(3, n))

    if min(a, b) > 1 or ((n, a, b,) in ((2, 1, 1), (3, 1, 1))):
        print("NO")
        return

    res = [[0] * n for _ in range(n)]
    for i in range(0, n - max(a, b)):
        res[i][i + 1] = res[i + 1][i] = 1
    if a == 1:
        res = [[e ^ 1 for e in l] for l in res]

    print("YES")
    for i in range(n):
        res[i][i] = 0
        print(*res[i], sep='')


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需要修改或在外部调用 main(n)
    main(5)
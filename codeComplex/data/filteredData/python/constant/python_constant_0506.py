import random

def main(n):
    # 生成规模为 n 的测试数据
    q = n  # 这里将查询数量设为 n，可根据需要调整生成策略
    Q = []
    for _ in range(q):
        # 生成 n, m, k，保证范围合理；可按需要修改生成规则
        k = random.randint(1, 10 ** 6)
        a = random.randint(1, k)
        b = random.randint(1, k)
        Q.append((a, b, k))

    # 原逻辑
    for n_, m, k in Q:
        if n_ > k or m > k:
            print(-1)
            continue

        x = max(n_, m) - min(n_, m)
        y = k - max(n_, m)

        if x % 2 == 0 and y % 2 == 0:
            print(k)
        elif x % 2 == 0 and y % 2 == 1:
            print(k - 2)
        elif x % 2 == 1 and y % 2 == 0:
            print(k - 1)
        elif x % 2 == 1 and y % 2 == 1:
            print(k - 1)


if __name__ == "__main__":
    # 示例：调用 main，规模为 5
    main(5)
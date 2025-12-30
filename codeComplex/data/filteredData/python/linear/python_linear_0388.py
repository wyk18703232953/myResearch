import random

def main(n):
    # 生成测试数据：
    # 将 m 设为与 n 同数量级，这里简单设为 n（至少为 1）
    m = max(1, n)

    # X 和 D 的取值范围可按需要调整
    # 这里示例：X 在 [-10^3, 10^3]，D 在 [-10^3, 10^3]
    X = [random.randint(-10**3, 10**3) for _ in range(m)]
    D = [random.randint(-10**3, 10**3) for _ in range(m)]

    summ = n * sum(X)

    for i in range(m):
        d = D[i]
        if d < 0:
            if n % 2 == 1:
                summ += d * (n // 2) * (n // 2 + 1)
            else:
                summ += d * (n // 2) * (n // 2)
        else:
            summ += d * (n - 1) * n // 2

    print(summ / n)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此修改
    main(10)
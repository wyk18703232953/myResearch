import random

def main(n):
    # 生成测试数据：n个升序整数构成数组a，以及k（1 <= k <= n）
    # 为保持与原算法语义一致，构造一个非降序数组
    base = random.randint(0, 10)
    a = [base]
    for _ in range(n - 1):
        a.append(a[-1] + random.randint(0, 10))
    k = random.randint(1, n)

    # 原始逻辑
    if k == 1:
        print(max(a) - min(a))
        return

    dif = []
    for i in range(n - 1):
        dif.append(a[i + 1] - a[i])
    dif = sorted(dif)
    print(sum(dif[:-k + 1]))


if __name__ == "__main__":
    # 示例：运行规模为 n = 10
    main(10)
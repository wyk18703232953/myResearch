import random

def main(n, k=2, value_range=(1, 10**6), seed=0):
    """
    n: 数组规模
    k: 给定的除数
    value_range: 生成随机整数的取值范围 [low, high]
    seed: 随机种子，便于复现
    """
    random.seed(seed)

    # 生成测试数据：长度为 n 的整数数组 a
    low, high = value_range
    a = [random.randint(low, high) for _ in range(n)]

    # 原逻辑
    a.sort()
    s = set()
    for i in range(n):
        if a[i] % k != 0:
            s.add(a[i])
        elif a[i] / k not in s:
            s.add(a[i])

    print(len(s))


if __name__ == "__main__":
    # 示例：n=10
    main(10)
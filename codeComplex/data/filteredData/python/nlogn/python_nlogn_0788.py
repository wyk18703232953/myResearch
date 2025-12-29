import random

def main(n, k=None, value_range=(0, 10**9)):
    """
    n: 规模，数组长度
    k: 分组数（若不提供则随机生成 1..n）
    value_range: 生成数组元素的取值范围 (low, high)
    """
    if n <= 0:
        return 0

    if k is None:
        k = random.randint(1, n)
    else:
        k = max(1, min(k, n))  # 保证 1 <= k <= n

    # 生成测试数据：严格递增数组 a
    low, high = value_range
    if high - low + 1 < n:
        high = low + n + 10  # 调整范围以保证可生成递增序列

    # 生成随机递增数组
    a = sorted(random.sample(range(low, high + 1), n))

    # 原逻辑
    b = []
    for i in range(n - 1):
        b.append(a[i + 1] - a[i])
    b.sort()
    ans = sum(b[:len(b) - k + 1])

    # 输出结果（可根据需要返回）
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：n=10，可自行修改
    main(10)
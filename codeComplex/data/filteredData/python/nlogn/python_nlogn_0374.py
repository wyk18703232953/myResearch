import random

def main(n, k=None, value_range=(1, 10**6), seed=None):
    """
    n: 规模，即数组长度
    k: 差值阈值，不给则随机生成
    value_range: 生成数组元素的取值范围 [low, high]
    seed: 随机种子，便于复现
    """
    if seed is not None:
        random.seed(seed)

    if k is None:
        # 让 k 的数量级与值域相关
        low, high = value_range
        k = random.randint(0, max(1, (high - low) // 10))

    # 生成测试数据：长度为 n 的随机数组
    low, high = value_range
    a = [random.randint(low, high) for _ in range(n)]

    # 原逻辑开始（去掉 input，改用生成的数据）
    a, j = sorted(a), 0
    ans = n
    for i in a:
        while j < n and i > a[j]:
            if i <= a[j] + k:
                ans -= 1
            j += 1

    print(ans)


if __name__ == "__main__":
    # 示例：n=10，可自行修改
    main(10)
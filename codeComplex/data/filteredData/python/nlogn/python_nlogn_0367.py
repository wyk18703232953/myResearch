import random

def main(n, k=None, value_range=(1, 1000), seed=0):
    """
    n: 规模（数组长度）
    k: 参数，不给则随机生成
    value_range: 生成数组元素的取值范围 (low, high)
    seed: 随机种子，便于复现
    """
    random.seed(seed)

    if k is None:
        # 随机生成 k，范围可根据需要调整
        k = random.randint(0, value_range[1] - value_range[0])

    # 生成测试数据：长度为 n 的随机数组 l
    l = [random.randint(value_range[0], value_range[1]) for _ in range(n)]

    # 原逻辑开始
    l.sort()
    a = 0
    i = 0
    while i < (n - 1):
        j = i + 1
        while j < n and l[j] == l[i]:
            j += 1
        if j == n:
            break
        else:
            if l[j] <= l[i] + k:
                a += (j - i)
        i = j
    result = n - a

    # 输出结果
    print(result)


if __name__ == "__main__":
    # 示例：n = 10，可根据需要修改
    main(10)
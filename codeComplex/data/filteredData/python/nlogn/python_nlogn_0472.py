import random

def main(n, k=None, value_range=(1, 10**9), seed=None):
    """
    n: 数组长度
    k: 选择的最大元素个数，若为 None，则随机生成 1 <= k <= n
    value_range: 生成随机整数的取值范围 [low, high]
    seed: 随机种子，便于复现
    """
    if seed is not None:
        random.seed(seed)

    if n <= 0:
        return

    if k is None:
        k = random.randint(1, n)
    else:
        k = max(1, min(k, n))  # 保证 1 <= k <= n

    # 生成测试数据：n 个随机整数
    low, high = value_range
    a = [random.randint(low, high) for _ in range(n)]

    # -------- 原逻辑开始 --------
    p = sorted(a)
    p = p[-k:]
    s = sum(p)
    print(s)

    idx = 0
    i = 0
    count = 0
    ans = []
    p_work = p[:]  # 为了不影响后续逻辑，使用副本

    while len(ans) < k - 1:
        idx += 1
        count += 1
        if a[i] in p_work:
            p_work.remove(a[i])
            ans.append(count)
            count = 0
        i += 1

    for x in ans:
        print(x, end=" ")
    print(n - idx)
    # -------- 原逻辑结束 --------


if __name__ == "__main__":
    # 示例：n=10 时运行一次
    main(10)
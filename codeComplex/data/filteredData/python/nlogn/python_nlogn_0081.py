import random

def main(n, k=None, seed=0):
    """
    n: 数据规模
    k: 下标（1-based），若为 None，则随机生成合法的 k
    seed: 随机种子，保证复现性
    """
    random.seed(seed)

    # 生成测试数据 A：长度为 n 的 (x, y) 元组列表
    # 按原逻辑，A 是若干整数对，这里取值范围可自行调整
    A = []
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        A.append((x, y))

    # 若未给出 k，则在 [1, n] 中随机选择
    if k is None:
        k = random.randint(1, n)

    # 按原程序排序：x 降序，y 升序
    A_sorted = sorted(A, key=lambda x: (-x[0], x[1]))

    # 统计 A_sorted 中等于 A_sorted[k-1] 的元素个数
    target = A_sorted[k - 1]
    ans = A_sorted.count(target)

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：n=10，k=None（随机），固定随机种子
    main(10)
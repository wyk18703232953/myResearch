import random

def main(n, k=None, seed=0):
    """
    :param n: 规模（数组长度）
    :param k: 选择的元素个数，默认为 n//2，且不超过 n
    :param seed: 随机种子，保证可复现
    """
    random.seed(seed)

    if k is None:
        k = max(1, n // 2)
    k = min(k, n)

    # 生成测试数据：长度为 n 的随机整数数组
    # 数值范围可根据需要调整
    a = [random.randint(1, 100) for _ in range(n)]

    # 原逻辑开始
    mark, b = [], []
    for x in a:
        b.append(x)
        mark.append(False)
    b.sort(reverse=True)
    idx, profit = 0, 0
    while idx < k:
        profit += b[idx]
        for i in range(n):
            if not mark[i] and a[i] == b[idx]:
                mark[i] = True
                break
        idx += 1
    print(profit)
    prev, counter = -1, 0
    for i in range(n):
        if counter == (k - 1):
            break
        if mark[i]:
            print(i - prev, end=' ')
            prev = i
            counter += 1
    print(n - prev - 1)

if __name__ == "__main__":
    # 示例运行
    main(10)
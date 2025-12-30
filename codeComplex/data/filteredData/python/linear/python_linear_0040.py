import random

def main(n, k=None):
    # 若未给定 k，则随机生成 1..n 之间的 k
    if k is None:
        k = random.randint(1, n)

    # 生成测试数据：长度为 n 的数组，元素在 1..max(2k, n) 范围内
    max_val = max(2 * k, n)
    values = [random.randint(1, max_val) for _ in range(n)]

    # 原始逻辑开始
    single, l, r = set(), -1, -1
    for i in range(n):
        single.add(values[i])
        if len(single) == k:
            l, r = 1, i + 1
            break

    single = set()
    for i in range(r - 1, max(-1, l - 2), -1):
        single.add(values[i])
        if len(single) == k:
            l = i + 1
            break

    if len(single) < k:
        print(-1, -1)
    else:
        print(l, r)


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)
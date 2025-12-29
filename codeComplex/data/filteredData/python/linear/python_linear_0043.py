import random

def main(n, k=None, max_val=10**5):
    # 生成测试数据：长度为 n 的数组，元素范围 [1, max_val]
    # 尽量保证不同元素个数 >= k（如果可能）
    if k is None:
        # 默认取一个相对合理的 k
        k = max(1, min(n, 5))
    k = min(k, n)

    # 构造前 k 个元素互不相同，后面随便填
    base_vals = list(range(1, k + 1))
    arr = base_vals + [random.randint(1, max_val) for _ in range(n - k)]

    # 原逻辑开始
    count = [0] * (max_val + 1)

    for x in arr:
        count[x] += 1

    # 不同元素个数
    s = sum(1 for c in count if c > 0)
    if s < k:
        print('-1 -1')
        return

    r = n - 1
    while True:
        if count[arr[r]] == 1:
            s -= 1
            if s < k:
                s += 1
                break
        count[arr[r]] -= 1
        r -= 1

    l = 0
    while True:
        if count[arr[l]] == 1:
            s -= 1
            if s < k:
                s += 1
                break
        count[arr[l]] -= 1
        l += 1

    print(l + 1, r + 1)


if __name__ == "__main__":
    # 示例：n=10，k=3
    main(10, 3)
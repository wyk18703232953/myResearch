import random

def next_idx(k, arr):
    i = k + 1
    while i < len(arr) and arr[i] != 1:
        i += 1
    return i

def main(n):
    # 生成测试数据
    # 约定：m 为 b 中 1 的个数，且 1 的位置从左到右出现，至少有一个 1
    if n < 2:
        n = 2

    # 随机生成 m（1 到 n//2，至少为 1）
    m = max(1, min(n // 2, random.randint(1, n)))

    # 生成严格递增的 a（或非降序也可）
    a = [0]
    for _ in range(1, n):
        a.append(a[-1] + random.randint(0, 3))  # 差值小点以便更有意义

    # 生成 b：长度 n，恰好有 m 个 1，其他为 0
    b = [0] * n
    ones_positions = sorted(random.sample(range(n), m))
    for pos in ones_positions:
        b[pos] = 1

    # 按原逻辑计算答案
    ans = [0] * (m + 1)

    k = -1
    k = next_idx(k, b)
    ans[1] = k
    for i in range(2, m + 1):
        kk = next_idx(k, b)
        for j in range(k + 1, kk):
            if a[j] - a[k] <= a[kk] - a[j]:
                ans[i - 1] += 1
            else:
                ans[i] += 1
        k = kk

    ans[m] += (n + m - 1 - k)

    # 输出结果（与原程序兼容，只输出 ans）
    for i in range(1, m + 1):
        print(ans[i], end=' ')

if __name__ == "__main__":
    # 示例运行：n 可根据需要修改
    main(10)
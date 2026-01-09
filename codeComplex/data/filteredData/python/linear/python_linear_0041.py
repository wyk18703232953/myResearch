def main(n):
    # n 表示数组长度，同时也用于生成 k
    # 保证 1 <= k <= n
    if n <= 0:
        return
    # 确定性生成 k：例如 k = n // 3 + 1，但不超过 n
    k = max(1, min(n, n // 3 + 1))

    # 确定性生成数组 a，元素取值范围适中以产生重复
    # 例如元素在 [1, n//2 + 1] 范围内循环
    if n == 0:
        a = []

    else:
        m = max(1, n // 2 + 1)
        a = [(i % m) + 1 for i in range(n)]

    d = {}
    r = l = -2

    # 第一段逻辑：找到最早使得不同元素个数达到 k 的位置 r
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
        if len(d) == k:
            r = i
            break

    # 若从未达到 k 种不同元素，模仿原逻辑输出 ( -1, -1 )
    if r == -2:
        # print(-1, -1)
        pass
        return

    # 第二段逻辑：从左侧缩小区间，找到最早的 l
    for i in range(r + 1):
        if d[a[i]] == 1:
            l = i
            break
        d[a[i]] -= 1

    # print(l + 1, r + 1)
    pass
if __name__ == "__main__":
    # 示例：使用若干固定规模调用以便做时间复杂度实验
    for size in [10, 100, 1000]:
        main(size)
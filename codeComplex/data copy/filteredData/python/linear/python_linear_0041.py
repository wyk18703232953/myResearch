def main(n):
    # n 作为数组长度；k 设为 n//2（至少为 1，至多为 n）
    if n <= 0:
        return
    k = max(1, n // 2)

    # 构造确定性数组 a：在 1..k 范围内循环取值
    a = [(i % k) + 1 for i in range(n)]

    d = {}
    r = l = -2

    # 与原逻辑一致：寻找最小前缀，使得不同元素个数达到 k
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
        if len(d) == k:
            r = i
            break

    # 若没能达到 k 个不同元素，原代码会输出 (-1, -1)
    if r == -2:
        # print(-1, -1)
        pass
        return

    # 从左侧缩短区间，使得区间仍包含 k 个不同元素
    for i in range(r + 1):
        if d[a[i]] == 1:
            l = i
            break
        d[a[i]] -= 1

    # print(l + 1, r + 1)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)
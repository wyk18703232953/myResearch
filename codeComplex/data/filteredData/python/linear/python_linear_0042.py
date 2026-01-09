def main(n):
    # 确定性数据生成
    # 这里将 n 同时作为数组长度和 k 的上界部分来源
    if n <= 0:
        # print(-1, -1)
        pass
        return

    # 构造数组 A，元素分布在 [1, m] 内
    # m 至少为 1，至多为 min(100000, n)
    m = min(100000, max(1, n // 2))
    A = [(i % m) + 1 for i in range(n)]

    # 确定性地设定 k：在 [1, min(m, n)] 内
    k = min(m, max(1, n // 3))

    C = [0] * 100001
    l = 0
    r = 0
    p = 0

    while r < n and p < k:
        val = A[r]
        C[val] += 1
        if C[val] == 1:
            p += 1
        r += 1

    if p != k:
        # print(-1, -1)
        pass

    else:
        while p == k:
            val = A[l]
            C[val] -= 1
            if C[val] == 0:
                p -= 1
            l += 1

        l -= 1
        # print(l + 1, r)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 进行规模实验
    main(100000)
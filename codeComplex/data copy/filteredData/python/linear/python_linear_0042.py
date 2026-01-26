def main(n):
    # 生成确定性输入：
    # n: 数组长度
    # k: 取值为 n//2（至少为 1，至多为 n）
    if n <= 0:
        return
    k = max(1, n // 2)
    # 生成数组 A，元素范围控制在 [1, 100000] 内
    # 使用简单模式：A[i] = (i % k) + 1，确保前缀中尽快出现 k 个不同值
    A = [i % k + 1 for i in range(n)]

    C = [0] * 100001
    l = 0
    r = 0
    p = 0

    while r < n and p < k:
        C[A[r]] += 1
        if C[A[r]] == 1:
            p += 1
        r += 1

    if p != k:
        # print('-1', '-1')
        pass

    else:
        while p == k:
            C[A[l]] -= 1
            if C[A[l]] == 0:
                p -= 1
            l += 1
        l -= 1
        # print(l + 1, r)
        pass
if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次固定规模的调用
    main(10)